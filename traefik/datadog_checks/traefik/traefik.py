# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import requests

from datadog_checks.checks import AgentCheck
from datadog_checks.errors import CheckException


class TraefikCheck(AgentCheck):

    def check(self, instance):
        host = instance.get('host')
        port = instance.get('port', '8080')
        path = instance.get('path', '/health')

        if not host:
            self.warning("Configuration error, please fix traefik.yaml")
            raise CheckException("Configuration error, please fix traefik.yaml")

        try:
            url = 'http://{}:{}{}'.format(host, port, path)
            response = requests.get(url)
            response_status_code = response.status_code

            if response_status_code == 200:
                self.service_check('traefik.health', self.OK)

                payload = response.json()

                if 'total_status_code_count' in payload:
                    values = payload['total_status_code_count']

                    for status_code in values:
                        self.gauge('traefik.total_status_code_count', values[status_code], ['status_code:' + status_code])

                else:
                    self.log.warn('Field total_status_code_count not found in response.')

                if 'total_count' in payload:
                    self.gauge('traefik.total_count', payload['total_count'])
                else:
                    self.log.warn('Field total_count not found in response.')

            else:
                self.service_check('traefik.health', self.CRITICAL, message="Traefik health check return code is not 200")

        except requests.exceptions.ConnectionError:
            self.service_check('traefik.health', self.CRITICAL, message="Traefik endpoint unreachable")

        except Exception as e:
            self.service_check('traefik.health', self.UNKNOWN, message="UNKNOWN exception" + str(e))
# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest
import os

from datadog_checks.dev import docker_run

from .common import HERE


@pytest.fixture(scope="session")
def eventstore_server():
    with docker_run(
        compose_file=os.path.join(HERE, "compose", "docker-compose.yml"),
        sleep=10
    ):
        yield

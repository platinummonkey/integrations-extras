# (C) Calastone Ltd. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

ALL_METRICS = [
    {
        "json_path": "proc.mem",
        "json_type": "int",
        "metric_name": "eventstore.proc.mem",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.cpu",
        "json_type": "float",
        "metric_name": "eventstore.proc.cpu",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.cpuScaled",
        "json_type": "float",
        "metric_name": "eventstore.proc.cpu_scaled",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.threadsCount",
        "json_type": "int",
        "metric_name": "eventstore.proc.threads",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.contentionsRate",
        "json_type": "float",
        "metric_name": "eventstore.proc.contentions_rate",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.thrownExceptionsRate",
        "json_type": "float",
        "metric_name": "eventstore.proc.thrown_exceptions_rate",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.diskIo.readBytes",
        "json_type": "int",
        "metric_name": "eventstore.proc.disk.read_bytes",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.diskIo.writtenBytes",
        "json_type": "int",
        "metric_name": "eventstore.proc.disk.write_bytes",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.diskIo.readOps",
        "json_type": "int",
        "metric_name": "eventstore.proc.disk.read_ops",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.diskIo.writeOps",
        "json_type": "int",
        "metric_name": "eventstore.proc.disk.write_ops",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.connections",
        "json_type": "int",
        "metric_name": "eventstore.tcp.connections",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.receivingSpeed",
        "json_type": "float",
        "metric_name": "eventstore.tcp.receiving_speed",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.sendingSpeed",
        "json_type": "float",
        "metric_name": "eventstore.tcp.sending_speed",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.inSend",
        "json_type": "int",
        "metric_name": "eventstore.tcp.in_send",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.measureTime",
        "json_type": "datetime",
        "metric_name": "eventstore.tcp.measure_time",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.pendingReceived",
        "json_type": "int",
        "metric_name": "eventstore.tcp.pending_received",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.pendingSend",
        "json_type": "int",
        "metric_name": "eventstore.tcp.pending_send",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.receivedBytesSinceLastRun",
        "json_type": "int",
        "metric_name": "eventstore.tcp.received_bytes.since_last_run",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.receivedBytesTotal",
        "json_type": "int",
        "metric_name": "eventstore.tcp.received_bytes.total",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.sentBytesSinceLastRun",
        "json_type": "int",
        "metric_name": "eventstore.tcp.sent_bytes.since_last_run",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.tcp.sentBytesTotal",
        "json_type": "int",
        "metric_name": "eventstore.tcp.sent_bytes.total",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.allocationSpeed",
        "json_type": "float",
        "metric_name": "eventstore.gc.allocation_speed",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.gen0ItemsCount",
        "json_type": "float",
        "metric_name": "eventstore.gc.items_count.gen0",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.gen0Size",
        "json_type": "float",
        "metric_name": "eventstore.gc.size.gen0",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.gen1ItemsCount",
        "json_type": "float",
        "metric_name": "eventstore.gc.items_count.gen1",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.gen1Size",
        "json_type": "float",
        "metric_name": "eventstore.gc.size.gen1",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.gen2ItemsCount",
        "json_type": "float",
        "metric_name": "eventstore.gc.items_count.gen2",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.gen2Size",
        "json_type": "float",
        "metric_name": "eventstore.gc.size.gen2",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.largeHeapSize",
        "json_type": "int",
        "metric_name": "eventstore.gc.large_heap_size",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.timeInGc",
        "json_type": "float",
        "metric_name": "eventstore.gc.time_in_gc",
        "metric_type": "gauge"
    },
    {
        "json_path": "proc.gc.totalBytesInHeaps",
        "json_type": "int",
        "metric_name": "eventstore.gc.total_bytes_in_heaps",
        "metric_type": "gauge"
    },
    {
        "json_path": "sys.cpu",
        "json_type": "float",
        "metric_name": "eventstore.sys.cpu",
        "metric_type": "gauge"
    },
    {
        "json_path": "sys.freeMem",
        "json_type": "int",
        "metric_name": "eventstore.sys.free_mem",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.queue.*.avgItemsPerSecond",
        "json_type": "int",
        "metric_name": "eventstore.es.queue.avg_items_per_second",
        "metric_type": "histogram",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.queue.*.avgProcessingTime",
        "json_type": "float",
        "metric_name": "eventstore.es.queue.avg_processing_time",
        "metric_type": "histogram",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.queue.*.currentIdleTime",
        "json_type": "datetime",
        "metric_name": "eventstore.es.queue.current_idle_time",
        "metric_type": "gauge",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.queue.*.currentItemProcessingTime",
        "json_type": "datetime",
        "metric_name": "eventstore.es.queue.current_processing_time",
        "metric_type": "gauge",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.queue.*.idleTimePercent",
        "json_type": "float",
        "metric_name": "eventstore.es.queue.idle_time_percent",
        "metric_type": "gauge",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.queue.*.length",
        "json_type": "int",
        "metric_name": "eventstore.es.queue.length",
        "metric_type": "histogram",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.queue.*.lengthCurrentTryPeak",
        "json_type": "int",
        "metric_name": "eventstore.es.queue.length_current_try_peak",
        "metric_type": "gauge",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.queue.*.lengthLifetimePeak",
        "json_type": "int",
        "metric_name": "eventstore.es.queue.length_lifetime_peak",
        "metric_type": "gauge",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.queue.*.totalItemsProcessed",
        "json_type": "int",
        "metric_name": "eventstore.es.queue.total_items_processed",
        "metric_type": "gauge",
        "tag_by": [
            "es.queue.*.queueName",
            "es.queue.*.groupName"
        ]
    },
    {
        "json_path": "es.writer.lastFlushSize",
        "json_type": "int",
        "metric_name": "eventstore.es.writer.flush_size.last",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.writer.lastFlushDelayMs",
        "json_type": "float",
        "metric_name": "eventstore.es.writer.flush_delay_ms.last",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.writer.meanFlushSize",
        "json_type": "int",
        "metric_name": "eventstore.es.writer.flush_size.mean",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.writer.meanFlushDelayMs",
        "json_type": "float",
        "metric_name": "eventstore.es.writer.flush_delay_ms.mean",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.writer.maxFlushSize",
        "json_type": "int",
        "metric_name": "eventstore.es.writer.flush_size.max",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.writer.maxFlushDelayMs",
        "json_type": "float",
        "metric_name": "eventstore.es.writer.flush_delay_ms.max",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.writer.queuedFlushMessages",
        "json_type": "int",
        "metric_name": "eventstore.es.writer.queued_flush_messages",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.readIndex.cachedRecord",
        "json_type": "int",
        "metric_name": "eventstore.es.read_index.cached_record",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.readIndex.notCachedRecord",
        "json_type": "int",
        "metric_name": "eventstore.es.read_index.not_cached_record",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.readIndex.cachedStreamInfo",
        "json_type": "int",
        "metric_name": "eventstore.es.read_index.cached_stream_info",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.readIndex.notCachedStreamInfo",
        "json_type": "int",
        "metric_name": "eventstore.es.read_index.not_cached_stream_info",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.readIndex.cachedTransInfo",
        "json_type": "int",
        "metric_name": "eventstore.es.read_index.cached_trans_info",
        "metric_type": "gauge"
    },
    {
        "json_path": "es.readIndex.notCachedTransInfo",
        "json_type": "int",
        "metric_name": "eventstore.es.read_index.not_cached_trans_info",
        "metric_type": "gauge"
    },
]

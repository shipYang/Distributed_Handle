# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/5 5:38 PM
# @Author  : zhaoyang
# @Site    : 
# @File    : celeryconfig.py
# @Software: PyCharm
# 注意，celery4版本后，CELERY_BROKER_URL改为BROKER_URL
from kombu import Queue
# broker_url = 'amqp://guest@localhost//'
BROKER_URL='amqp://guest@localhost//'
# 指定结果的接受地址
CELERY_RESULT_BACKEND='test'
# CELERY_TASK_SERIALIZER = 'msgpack'
# # 指定结果序列化方式
# CELERY_RESULT_SERIALIZER = 'msgpack'
# # 任务过期时间,CELERY任务执行结果的超时时间
# CELERY_TASK_RESULT_EXPIRES = 60 * 20
# # 指定任务接受的序列化类型.
# CELERY_ACCEPT_CONTENT = ["msgpack"]
# # 任务发送完成是否需要确认，这一项对性能有一点影响
# CELERY_ACKS_LATE = False
# # 压缩方案选择，可以是ZLIB, BZIP2，默认是发送没有压缩的数据
# CELERY_MESSAGE_COMPRESSION = 'zlib'
# # 规定完成任务的时间
# CELERYD_TASK_TIME_LIMIT = 5  # 在5S内完成任务，否则执行该任务的WORKER将被杀死，任务移交给父进程
# # CELERY WORKER的并发数，默认是服务器的内核数目,也是命令行-C参数指定的数目
# CELERYD_CONCURRENCY = 4
# # CELERY WORKER 每次去RABBITMQ预取任务的数量
# CELERYD_PREFETCH_MULTIPLIER = 4
# # 每个WORKER执行了多少任务就会死掉，默认是无限的
# CELERYD_MAX_TASKS_PER_CHILD = 40
# # 设置默认的队列名称，如果一个消息不符合其他的队列就会放在默认队列里面，如果什么都不设置的话，数据都会发送到默认的队列中
# CELERY_DEFAULT_QUEUE = "default"
# 指定任务序列化方式
celery_task_serializer = 'msgpack'
# 指定结果序列化方式
celery_result_serializer = 'msgpack'
# 任务过期时间,celery任务执行结果的超时时间
celery_task_result_expires = 600 * 200
# 指定任务接受的序列化类型.
celery_accept_content = ["msgpack"]
# 任务发送完成是否需要确认，这一项对性能有一点影响
celery_acks_late = False
# 压缩方案选择，可以是zlib, bzip2，默认是发送没有压缩的数据
celery_message_compression = 'zlib'
# 规定完成任务的时间
celeryd_task_time_limit = 5  # 在5s内完成任务，否则执行该任务的worker将被杀死，任务移交给父进程
# celery worker的并发数，默认是服务器的内核数目,也是命令行-c参数指定的数目
celeryd_concurrency = 4
# celery worker 每次去rabbitmq预取任务的数量
celeryd_prefetch_multiplier = 4
# 每个worker执行了多少任务就会死掉，默认是无限的
celeryd_max_tasks_per_child = 40
# 设置默认的队列名称，如果一个消息不符合其他的队列就会放在默认队列里面，如果什么都不设置的话，数据都会发送到默认的队列中
celery_default_queue = "default"
# 设置详细的队列
# 最后，为不同的task指派不同的队列
# 将所有的task组成dict，key为task的名称，即task所在的模块，及函数名
# 如async_send_email所在的模块为handlers.async_tasks
# 那么task名称就是handlers.async_tasks.async_send_email
# 每个task的value值也是为dict，设定需要指派的队列name，及对应的routing_key
# 这里的name和routing_key需要和CELERY_QUEUES设定的完全一致
CELERY_QUEUES = (
    Queue(name='defalut', routing_key='task.#'),
    Queue(name='add', routing_key='add'),
    Queue(name='func', routing_key='func'),
)

# 最后，为不同的task指派不同的队列
# 将所有的task组成dict，key为task的名称，即task所在的模块，及函数名
# 如async_send_email所在的模块为handlers.async_tasks
# 那么task名称就是handlers.async_tasks.async_send_email
# 每个task的value值也是为dict，设定需要指派的队列name，及对应的routing_key
# 这里的name和routing_key需要和CELERY_QUEUES设定的完全一致
CELERY_ROUTES = {
    'default': {
        'queue': 'defaut',
        'routing_key': 'task.#',
    },
    'App.task.add': {
        'queue': 'add',
        'routing_key': 'add',
    },
    'App.task.func': {
        'queue': 'func',
        'routing_key': 'func',
    }
}

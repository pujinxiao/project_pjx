# -*- coding: utf-8 -*-
__author__ = 'bobby'

import redis
redis_cli = redis.StrictRedis()
redis_cli.incr("jobbole_count")


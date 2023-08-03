# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Axual B.V.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
from os.path import dirname, abspath
from time import gmtime
import json
from confluent_kafka import Producer

logger = logging.getLogger('')  # Root logger, to catch all submodule logs
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s.%(msecs)03d|%(levelname)s|%(filename)s| %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
formatter.converter = gmtime  # Log UTC time

if len(logger.handlers) == 0:
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)


def _full_path_of(path):
    base_dir = dirname(dirname(dirname(abspath(__file__))))
    return f'{base_dir}{path}'


def delivery_callback(error, msg) -> None:
    """
    Per-message delivery callback (triggered by poll() or flush())

    :param error: None if the message was successfully delivered
    :param msg: Message metadata
    :return: None
    """
    if error is not None:
        logger.error(f'Failed to deliver message: {error}')
    else:
        logger.info(f'Produced record to topic {msg.topic()} partition [{msg.partition()}] @ offset {msg.offset()}')


def produce_data(configuration,topic,row,logger):

    producer = Producer(configuration)


    try:
        logger.info(f'Starting kafka producer to produce to topic: {topic}. ^C to exit.')
        record_key = f'key_1'
        value_str = json.dumps(row)  # Serialize dictionary to JSON string
        value_bytes = bytes(value_str, encoding='utf-8')

        producer.poll(0)
        producer.produce(topic, key=record_key, value=value_bytes, on_delivery=delivery_callback)

        logger.info('Done producing.')
    except KeyboardInterrupt:
        logger.info('Caught KeyboardInterrupt, stopping.')
    finally:
        if producer is not None:
            logger.info('Flushing producer.')
            producer.flush()


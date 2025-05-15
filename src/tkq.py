from taskiq import TaskiqScheduler
from taskiq_redis import RedisAsyncResultBackend,RedisStreamBroker
from taskiq.schedule_sources import LabelScheduleSource
from dotenv import load_dotenv
import os

load_dotenv()
redis_url = os.getenv("REDIS_URL")
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


broker = RedisStreamBroker(redis_url).with_result_backend(RedisAsyncResultBackend(redis_url))
scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)]
)
from src.tkq import broker
import taskiq_fastapi

taskiq_fastapi.init(broker, "src.__main__:get_app")
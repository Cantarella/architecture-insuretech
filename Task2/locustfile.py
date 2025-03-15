from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Время между запросами

    @task
    def load_test(self):
        self.client.get("/")  # Отправляем GET-запрос на корневой путь
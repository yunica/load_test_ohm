from locust import HttpUser, task, between
import random

locations = [
    "3/66.86/-70.14",
    "3/19.48/-54.49",
    "4/ 46.68/ 10.28",
    "5/28.768/127.969",
    "5/67.153/-53.525",
    "3/42.42/4.75",
    "3/-27.53/56.95"
]


class OSMUser(HttpUser):
    wait_time = between(1, 3)  # Tiempo de espera entre las tareas en segundos

    @task
    def view_dynamic_url(self):
        years = range(1543, 2023, 5)
        loc = random.choice(locations)
        for year in years:
            url = f"/#map={loc}&layers=O&date={year}-01-01&daterange=1523-01-01,2023-12-31"
            self.client.get(url, name=f"ohm - year {year}")

    @task
    def view_traces(self):
        self.client.get("/traces", name="traces")

    @task
    def view_diary(self):
        self.client.get("/diary", name="diary")

    @task
    def view_export(self):
        self.client.get("/export#map=5/-12.683/30.410&layers=O", name="export")
    @task
    def view_history(self):
        self.client.get("/history?list=1&bbox=-175.078125%2C-57.32652122521708%2C175.78125%2C72.60712040027555", name="history")

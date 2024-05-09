import random
from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth

class NextcloudUser(HttpUser):
    auth = None
    user_name = None
    wait_time = between(2, 10)

    # users to test this with.
    def on_start(self):
        user_idx = random.randrange(0, 25)
        self.user_name = f'locust_user{user_idx}'
        self.auth = HTTPBasicAuth(self.user_name, 'test_password1234!')
    
    # Upload small files
    @task(10)
    def upload_file_1kb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1kb_file_{random.randrange(0, 10)}"
        with open("/mnt/locust/file_1kb", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)
            self.client.delete(remote_path, data=file, auth=self.auth)

    # Upload medium files
    @task(10)
    def upload_file_1mb(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/1mb_file_{random.randrange(0, 10)}"
        with open("/mnt/locust/file_1mb", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)
            self.client.delete(remote_path, data=file, auth=self.auth)

    # Upload Introduction to Quantum Mechanics by our Savior David J. Griffiths
    @task(5)
    def upload_QMpdf(self):
        remote_path = f"/remote.php/dav/files/{self.user_name}/Introduction_to_Quantum_Mechanichs_{random.randrange(0, 10)}.pdf"
        with open("/mnt/locust/Introduction_to_Quantum_Mechanichs.pdf", "rb") as file:
            self.client.put(remote_path, data=file, auth=self.auth)
            self.client.delete(remote_path, data=file, auth=self.auth)
# Cloud Storage System Deployment Guide

Here's a concise guide for setting up the infrastructure using Docker:

## Quick Setup Guide

### Step 1: Install Docker and Docker Compose

- Ensure Docker and Docker Compose are installed on your system.

### Step 2: Clone the Repository

- Clone the [cloud_basic_exam](https://github.com/Gabrynho/cloud_basic_exam) repository to get the required directories and volume setup.

### Step 3: Run Docker Compose

- Navigate to the repository directory and start the services with:

```[bash]

docker-compose up -d

```

**Services Overview:**

- **Nextcloud**: File hosting service accessible at `http://localhost:8080`.
- **MySQL (MariaDB)**: Database for Nextcloud's data storage.
- **Locust**: Load testing service, requires `locustfile.py` in the specified directory.

### Step 4: Configure Testing Environment

- Disable Nextcloud's security measures for testing purposes:
  - Execute the following command to add `nextcloud` to trusted domains:

    ```[bash]
    docker exec --user www-data nextcloud php /var/www/html/occ config:system:set trusted_domains 2 --value=nextcloud
    ```

  - Add these lines to `config.php` to disable rate limiting and file locking:

    ```[php]
    'ratelimit.protection.enabled' => false,
    'filelocking.enabled' => false,
    ```

### Step 5: Clean Up

- Stop and remove all services with:

  ```[bash]
  docker-compose down
  ```

- To remove volumes and preserve data, use:

  ```[bash]
  docker-compose down --volumes
  ```
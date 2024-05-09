for i in {0..24}
do
  docker exec --user www-data nextcloud /bin/bash -c "rm /var/www/html/data/locust_user$i/**/*_file_*"
done
for i in {0..24}
do
  docker exec -e OC_PASS=test_password1234! --user www-data nextcloud /var/www/html/occ user:add --password-from-env locust_user$i
done
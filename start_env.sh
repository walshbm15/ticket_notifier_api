set -e
echo checking for environment vars files
echo If execution stops you need to setup .env

# Start Postgres
echo start first postgres, please make sure no other postgres are running on port 5432
docker-compose up -d postgres

echo environment setup successfully

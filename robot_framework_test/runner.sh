sudo docker compose up --build -d selenium

echo "Waiting for selenium to be ready..."
until curl -s http://localhost:4444/wd/hub/status | grep -q "ready"; do
  echo "Waiting..."
  sleep 3
done

sudo docker compose up  --build robot

sudo docker compose run --rm robot robot --version
sudo docker compose run --rm robot pip show robotframework-seleniumlibrary
sudo docker compose run --rm robot pip show selenium
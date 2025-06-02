# sudo docker run -d -p 4444:4444 --name selenium selenium/standalone-firefox:latest


# sudo docker build -t robot_framework_test ./

# sudo docker container run -it -v "./output:/app/output" robot_framework_test bash
# # sudo docker run -it -v "./output:/app/output" robot_framework_test

# sudo docker compose up -d
# sudo docker compose run --rm robot robot robot_test.robot


sudo docker compose up --build -d selenium

echo "Waiting for selenium to be ready..."
until curl -s http://localhost:4444/wd/hub/status | grep -q "ready"; do
  echo "Waiting..."
  sleep 3
done

sudo docker compose up  --build robot
sudo docker compose run --rm robot robot --outputdir /app/output robot_test.robot

sudo docker build -t robot_framework_test ./

# sudo docker container run -it robot_framework_test bash
sudo docker run -it -v "./output:/app/output" robot_framework_test
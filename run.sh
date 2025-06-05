#!/bin/bash

SERVICE="$1"
COMMAND="$2"

start_selenium_if_needed() {
    if ! docker ps --filter "name=selenium" --filter "status=running" | grep -q selenium; then
        echo "Starting Selenium..."
        docker compose up --build -d selenium
    fi

    echo "Waiting for Selenium to be ready..."
    until curl -s http://localhost:4444/wd/hub/status | grep -q "ready"; do
        echo "Waiting for Selenium..."
        sleep 3
    done
}

case "$SERVICE" in
    python_oop_and_testing)
        start_selenium_if_needed
        if [[ "$COMMAND" == "test" ]]; then
            docker compose build python_oop_and_testing
            docker compose run --rm python_oop_and_testing pytest
        else
            docker compose up --build python_oop_and_testing
        fi
        ;;
    
    robot_framework_test)
        start_selenium_if_needed
        docker compose up --build robot_framework_test
        ;;

    *)
        echo "Usage:"
        echo "    ./run.sh robot_framework_test             # task 1: Run Robot Framework"
        echo "    ./run.sh python_oop_and_testing           # task 2: Run Robot Framework with Python Keywords"
        echo "    ./run.sh python_oop_and_testing test      # task 2: Run pytest"
        exit 1
        ;;
esac

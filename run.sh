#!/bin/bash

SERVICE="$1"
COMMAND="$2"

case "$SERVICE" in
    python_oop_and_testing)
        if [[ "$COMMAND" == "test" ]]; then
            docker compose build python_oop_and_testing
            docker compose run --rm python_oop_and_testing pytest
        else
            docker compose up --build python_oop_and_testing
        fi
        ;;
    
    robot_framework_test)
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

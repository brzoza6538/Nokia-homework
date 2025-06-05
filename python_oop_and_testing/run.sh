#!/bin/bash

sudo docker compose up --build -d selenium

echo "Waiting for selenium to be ready..."
until curl -s http://localhost:4444/wd/hub/status | grep -q "ready"; do
  echo "Waiting..."
  sleep 3
done

if [[ "$1" == "test" ]]; then
  # Uruchom pytest w kontenerze robot
  sudo docker compose run --rm robot pytest
else
  # Domyślnie uruchom robot framework testy
  sudo docker compose up --build robot
fi

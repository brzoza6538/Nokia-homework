#!/bin/bash
sudo docker compose up --build -d selenium

echo "Waiting for selenium to be ready..."
until curl -s http://localhost:4444/wd/hub/status | grep -q "ready"; do
  echo "Waiting..."
  sleep 3
done

sudo docker compose up  --build robot

max_retries=100
attempt=1

while [ $attempt -le $max_retries ]; do
  echo "===== Test Attempt: $attempt ====="
  
  # Uruchom testy i zapisz wyjście
  output=$(sudo docker compose run --rm robot 2>&1)
  echo "$output"

  # Sprawdź czy testy zakończyły się błędem
  if echo "$output" | grep -q "| FAIL |"; then
    echo "❌ Test failed on attempt $attempt"
  elif echo "$output" | grep -q "| PASS |"; then
    echo "✅ Test passed on attempt $attempt"
  else
    echo "⚠️ Nie rozpoznano wyniku, powtarzam..."
  fi

  ((attempt++))
done

# Sprawdź wersję robotframework i bibliotek
sudo docker compose run --rm robot robot --version
sudo docker compose run --rm robot pip show robotframework-seleniumlibrary
sudo docker compose run --rm robot pip show selenium
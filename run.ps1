param (
    [string]$Service,
    [string]$Command
)

function Start-SeleniumIfNeeded {
    $seleniumRunning = docker ps --filter "name=selenium" --filter "status=running" | Select-String "selenium"
    if (-not $seleniumRunning) {
        Write-Host "Starting Selenium..."
        docker compose up --build -d selenium
    }

    Write-Host "Waiting for Selenium to be ready..."
    do {
        Start-Sleep -Seconds 3
        $status = Invoke-RestMethod -Uri http://localhost:4444/wd/hub/status -UseBasicParsing -ErrorAction SilentlyContinue
    } while ($null -eq $status -or $status.value.ready -ne $true)
}

switch ($Service) {
    "python_oop_and_testing" {
        Start-SeleniumIfNeeded

        if ($Command -eq "test") {
            docker compose build python_oop_and_testing
            docker compose run --rm python_oop_and_testing pytest
        } else {
            docker compose up --build python_oop_and_testing
        }
    }
    "robot_framework_test" {
        Start-SeleniumIfNeeded
        docker compose up --build robot_framework_test
    }
    default {
        Write-Host "Usage:"
        Write-Host "    ./run.ps1 robot_framework_test             # task 1: Run Robot Framework"
        Write-Host "    ./run.ps1 python_oop_and_testing           # task 2: Run Robot Framework with Python Keywords"
        Write-Host "    ./run.ps1 python_oop_and_testing test      # task 2: Run pytest"
        exit 1
    }
}

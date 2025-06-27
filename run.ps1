param (
    [string]$Service,
    [string]$Command
)

switch ($Service) {
    "python_oop_and_testing" {

        if ($Command -eq "test") {
            docker compose build python_oop_and_testing
            docker compose run --rm python_oop_and_testing pytest
        } else {
            docker compose up --build python_oop_and_testing
        }
    }
    "robot_framework_test" {
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

#!/usr/bin/env bash

# wait for Postgres to start
function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="przedszkole", user="postgres", password="postgres", host="127.0.0.1")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}


  >&2 echo "Postgres is unavailable - sleeping"
  sleep 15




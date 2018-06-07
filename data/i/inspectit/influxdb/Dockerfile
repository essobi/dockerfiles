FROM influxdb:1.0.0  
HEALTHCHECK \--interval=5s CMD wget http://localhost:8086/ping -qO /dev/null
|| exit 1


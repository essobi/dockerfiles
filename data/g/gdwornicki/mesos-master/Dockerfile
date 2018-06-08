from mesosphere/mesos-master:1.3.0  
add entrypoint.sh /entrypoint.sh  
add gen_hosts.sh /gen_hosts.sh  
run apt-get update ; apt-get install cron cronutils -y  
expose 5050  
env MESOS_PORT=5050 MESOS_QUORUM=1 MESOS_REGISTRY=replicated_log
MESOS_LOG_DIR=/var/log/mesos MESOS_WORK_DIR=/var/tmp/mesos  
entrypoint /entrypoint.sh  


from mesosphere/mesos-slave:1.3.0  
run apt-get update ; curl -sSL https://dl.bintray.com/emccode/dvdcli/install |
sh -s stable ; apt-get install cron cronutils -y  
add entrypoint.sh /entrypoint.sh  
add gen_hosts.sh /gen_hosts.sh  
expose 5051  
env MESOS_PORT=5051 MESOS_LOG_DIR=/var/log/mesos MESOS_WORK_DIR=/var/tmp/mesos
MESOS_CONTAINERIZERS=docker,mesos MESOS_SWITCH_USER=0  
entrypoint /entrypoint.sh  


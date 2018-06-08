from mesosphere/zookeeper  
run apt-get update && apt-get install openjdk-7-jdk curl cron cronutils -y &&
mkdir /opt/exhibitor  
add defaults.conf /opt/exhibitor/defaults.conf  
add exhibitor.jar /opt/exhibitor/exhibitor.jar  
add slf4j-log4j12-1.6.1.jar /opt/exhibitor/slf4j-log4j12-1.6.1.jar  
add gen_hosts.sh /gen_hosts.sh  
add entrypoint.sh /entrypoint.sh  
expose 2181 3888 8181  
entrypoint /entrypoint.sh  


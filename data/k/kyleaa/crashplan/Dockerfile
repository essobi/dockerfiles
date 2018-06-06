FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y wget && apt-get clean  
ADD CrashPlan_3.7.0_Linux.tgz /tmp/  
ADD install-unattended.sh /tmp/CrashPlan-install/install-unattended.sh  
RUN ls /tmp/CrashPlan-install  
RUN cd /tmp/CrashPlan-install/ && ./install-unattended.sh  
  
EXPOSE 4243 4242  
VOLUME /mnt/crashplan  
  
# Add modified CrashPlan startup script to keep process in the foreground  
ADD CrashPlanEngine /usr/local/crashplan/bin/CrashPlanEngine  
CMD ["/usr/local/crashplan/bin/CrashPlanEngine","start"]  


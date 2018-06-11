FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y --no-install-recommends\  
build-essential\  
wget\  
ruby\  
git\  
cron\  
net-tools  
  
COPY dotbashrc /root/.bashrc  
COPY motd /etc/  
COPY tabfile /etc/  
COPY uvstartd /  
  
ENTRYPOINT ["/uvstartd","-l","/tmp/my.log","/etc/tabfile"]  


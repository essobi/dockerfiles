FROM mongo:latest  
  
RUN apt-get update \  
&& apt-get install -y git \  
&& apt-get install -y cron  
  
ADD entrypoint.sh logrotate.sh backup.sh restore.sh mongo.sh github_com /bck/  
  
WORKDIR /bck  
  
VOLUME /data  
  
ENTRYPOINT /bck/entrypoint.sh  


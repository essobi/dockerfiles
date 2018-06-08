FROM mongo  
  
WORKDIR /root  
  
COPY lib.sh entrypoint.sh /root/  
  
RUN apt-get update \  
&& apt-get install -y sshfs logrotate cron \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
ENTRYPOINT ./entrypoint.sh  


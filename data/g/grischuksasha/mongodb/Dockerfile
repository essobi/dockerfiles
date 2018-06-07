FROM mongo:3.6  
ENV AUTH yes  
ENV STORAGE_ENGINE wiredTiger  
ENV JOURNALING yes  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends logrotate \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD ./logrotate/mongodb /etc/logrotate.d/mongodb  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
ADD set_mongodb_password.sh /set_mongodb_password.sh  
RUN chmod +x /set_mongodb_password.sh  
  
CMD ["/run.sh"]


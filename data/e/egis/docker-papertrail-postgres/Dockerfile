FROM egis/docker-postgres  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y monit && rm -rf /var/lib/apt/lists/*  
  
COPY * /opt/  
  
RUN chmod 0700 /opt/monitrc  
  
EXPOSE 80  
CMD ["/opt/start.sh"]  


FROM debian:jessie  
  
RUN apt-get update && apt-get -y install --no-install-recommends \  
gearman-job-server \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4730  
USER gearman  
  
CMD ["gearmand", "-l", "/var/log/gearman-job-server/gearmand.log"]  


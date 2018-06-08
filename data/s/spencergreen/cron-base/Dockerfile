FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends --no-install-suggests \  
cron  
  
CMD ["cron", "-f"]


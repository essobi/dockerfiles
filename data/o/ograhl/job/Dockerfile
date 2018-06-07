FROM ubuntu:16.04  
# APT-GET Installs  
# - ca-certificates (make wget https work without --no-check-certificate)  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
ca-certificates \  
cron \  
vim \  
wget \  
&& \  
rm -r /var/lib/apt/lists/*  
  
### Copy files  
# Scripts  
COPY scripts/*.sh /  
  
### Final RUN steps  
# - /*.sh: Make executable  
RUN chmod 744 /*.sh  
  
# ENTRYPOINT and CMD  
CMD ["/init.sh"]  
  


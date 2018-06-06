FROM mariadb:latest  
MAINTAINER Pedro Mendes pmendes@homeit.pt  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y git ssh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY scripts/init.sh /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/init.sh  
  
CMD bash -C '/usr/local/bin/init.sh';'bash'  


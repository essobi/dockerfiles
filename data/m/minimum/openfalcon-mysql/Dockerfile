FROM mysql:5.6  
MAINTAINER minimum@cepave.com  
  
# Install Open-Falcon Database  
RUN \  
apt-get update && \  
apt-get install -y git && \  
git clone https://github.com/Cepave/scripts.git && \  
apt-get remove -y git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
# Port  
EXPOSE 3306  
# Run MySQL  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mysqld"]  


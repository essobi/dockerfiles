FROM mongo:3.4  
RUN apt-get update && apt-get install -y python-pip && \  
rm -rf /var/lib/apt/lists/* && pip install awscli && \  
apt-get -y remove python-pip && rm -rf /var/lib/apt/lists/*  
  
ADD ./backup.sh /backup.sh  
ADD ./restore.sh /restore.sh  
CMD ["/backup.sh"]  


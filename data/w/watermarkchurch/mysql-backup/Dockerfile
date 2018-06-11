FROM mysql:5  
MAINTAINER "Watermark Dev Team <dev@watermark.org>"  
RUN apt-get update -y -q && \  
apt-get install -y python2.7 python-pip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install awscli  
  
ADD backup.sh /backup.sh  
RUN chmod 0755 /backup.sh  
  
ENTRYPOINT ["/backup.sh"]  
  


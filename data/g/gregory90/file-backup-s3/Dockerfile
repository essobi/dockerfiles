FROM gregory90/base  
  
RUN mkdir /app && \  
apt-get update && \  
apt-get install -y -q python-setuptools && \  
easy_install pip && \  
pip install awscli  
  
RUN mkdir /backup  
  
ADD run /app/run  
ADD restore /app/restore  
ADD s3cfg /.s3cfg  
  
RUN chmod +x /app/run  
RUN chmod +x /app/restore  


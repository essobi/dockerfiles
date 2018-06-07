FROM gregory90/mysql-backup  
  
RUN apt-get update && \  
apt-get install -y -q python-setuptools && \  
easy_install pip && \  
pip install awscli  
  
ADD run /app/run  
ADD restore /app/restore  
ADD my.cnf /app/my.cnf  
ADD s3cfg /.s3cfg  
  
RUN chmod +x /app/run  
RUN chmod +x /app/restore  


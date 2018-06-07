FROM alpine  
ADD localtime /etc/localtime  
  
ADD . /webapp/  
  
WORKDIR /webapp  
  
RUN apk add --update python python-dev py-pip && \  
pip install flask flask-sqlalchemy pymysql docker-py && \  
chmod u+x "entry.sh" && \  
rm /var/cache/apk/*  
  
EXPOSE 8080  
ENTRYPOINT ["./entry.sh"]  
  


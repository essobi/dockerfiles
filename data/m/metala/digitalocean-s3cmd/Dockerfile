FROM alpine:latest  
  
ENV DATACENTER_REGION=AMS3 \  
ACCESS_KEY= \  
SECRET_KEY= \  
ENCRYPTION_PASSWORD=  
  
ADD ./s3cfg /.s3cfg  
ADD ./entrypoint.sh /  
RUN apk update && \  
apk add python py-pip gnupg && \  
pip install s3cmd && \  
chmod 666 /.s3cfg && \  
ln -s /.s3cfg /root/.s3cfg  
  
WORKDIR /mnt  
ENTRYPOINT ["/entrypoint.sh"]  


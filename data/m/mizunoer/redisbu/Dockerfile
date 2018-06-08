FROM redis:3  
  
RUN apt-get update && \  
apt-get -y install apt-utils && \  
apt-get -y install python-pip && \  
apt-get -y install curl && \  
pip install awscli --upgrade --user && \  
mkdir -p /root/.aws  
  
COPY backup.sh /root/backup.sh  
COPY awsbu.sh /root/awsbu.sh  
COPY curl.sh /root/curl.sh  
COPY credentials /root/.aws/credentials  
COPY config /root/.aws/config  
RUN chmod -R +x /root/backup.sh && \  
chmod -R +x /root/awsbu.sh  
CMD /root/backup.sh  
#CMD ./root/awsbu.sh  


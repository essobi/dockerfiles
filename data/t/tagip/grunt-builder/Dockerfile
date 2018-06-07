FROM tagip/grunt-builder  
  
RUN apk --update --no-cache add \  
sudo \  
python \  
py-pip \  
openssl \  
ca-certificates  
  
RUN apk --update --virtual build-dependencies add \  
python-dev libffi-dev openssl-dev build-base && \  
pip install --upgrade pip cffi && \  
pip install ansible==1.9.4 && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /etc/ansible && \  
echo 'localhost' > /etc/ansible/hosts  


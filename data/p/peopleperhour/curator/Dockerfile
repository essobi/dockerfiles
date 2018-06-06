FROM alpine:3.3  
RUN apk add --no-cache bash python python-dev openssl py-pip gettext && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python  
#apk del build-dependencies  
WORKDIR /opt  
  
## Install AWS CLI  
#RUN pip install awscli  
# Install Curator.  
RUN pip install elasticsearch-curator==3.5.1  
  
# Launch Elastalert when a container is started.  
ENTRYPOINT ["curator"]  


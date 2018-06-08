FROM node:6-onbuild  
# node modules from package.json are automatically installed by the 6-onbuild  
ADD install.sh /tmp/install.sh  
RUN sh -e /tmp/install.sh  
  
RUN mkdir -p /app  
WORKDIR /app  
RUN git clone https://github.com/awslabs/amazon-kinesis-client-python.git  
WORKDIR /app/amazon-kinesis-client-python  
RUN python3 setup.py install  
  
WORKDIR /app  


FROM golang:1.9  
MAINTAINER KASKO Ltd, sysarch@kasko.io  
  
RUN apt-get -y update && apt-get install unzip  
  
COPY .docker/config.json /tmp/.docker/config.json  
  
RUN mkdir -p src/github.com/awslabs/amazon-ecr-credential-helper/ && \  
wget -O src/github.com/awslabs/amazon-ecr-credential-helper/master.zip --no-
check-certificate https://github.com/awslabs/amazon-ecr-credential-
helper/archive/master.zip  
  
WORKDIR /go/src/github.com/awslabs/amazon-ecr-credential-helper/  
RUN unzip master.zip && \  
mv amazon-ecr-credential-helper-master/* . && \  
rm -rf amazon-ecr-credential-helper-master && \  
rm -f master.zip  
  
CMD /usr/bin/make && cp -r /tmp/.docker /data  


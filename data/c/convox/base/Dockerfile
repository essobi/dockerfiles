FROM convox/alpine:3.1  
RUN apk-install curl zip  
  
RUN curl -L
https://dl.bintray.com/mitchellh/packer/packer_0.7.5_linux_amd64.zip -o
/tmp/packer.zip  
RUN unzip /tmp/packer.zip -d /usr/local/bin  
  
ADD . /runtime  
WORKDIR /runtime  
  
CMD ["packer", "build", "data/packer.json"]  


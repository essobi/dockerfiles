# VERSION 0.1  
# DOCKER-VERSION 0.8.0  
# AUTHOR: Dr Nic Williams <drnicwilliams@gmail.com>  
# DESCRIPTION: Image with gnatsd project and dependecies  
# TO_BUILD: git submodule update --init && docker build -t gnatsd .  
# TO_RUN: docker run -p 4222:4222 -p 4244:4244 -p 8222:8222 -v $(pwd):/config
-v $(pwd)/log:/log gnatsd  
FROM miksago/ubuntu-go  
  
RUN mkdir -p /tmp/src/github.com/apcera  
ADD gnatsd /tmp/src/github.com/apcera/gnatsd  
  
RUN export GOPATH=/tmp ;\  
go install github.com/apcera/gnatsd ;\  
mv /tmp/bin/gnatsd /usr/bin/  
  
RUN gnatsd --version  
  
EXPOSE 4222  
EXPOSE 4244  
EXPOSE 8222  
VOLUME /config  
VOLUME /log  
  
CMD ["gnatsd", "-c", "/config/gnatsd.conf"]  


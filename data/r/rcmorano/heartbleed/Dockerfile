FROM jayofdoom/docker-ubuntu-14.04  
MAINTAINER Roberto C. Morano rcmova@gmail.com  
RUN apt-get update  
RUN apt-get install -y golang git  
RUN mkdir /tmp/go  
RUN GOPATH=/tmp/go go get github.com/FiloSottile/Heartbleed  
RUN GOPATH=/tmp/go go install github.com/FiloSottile/Heartbleed  
RUN ln -s /tmp/go/bin/Heartbleed /usr/local/bin/  


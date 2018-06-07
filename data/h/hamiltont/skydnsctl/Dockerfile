FROM stackbrew/ubuntu  
MAINTAINER Hamilton Turner <hamiltont@gmail.com>  
  
ENV HOME /root  
ENV GOPATH /root/go  
  
RUN apt-get update  
RUN apt-get install -y git-core  
RUN apt-get install -y golang  
RUN mkdir /root/go  
  
RUN git clone https://github.com/skynetservices/skydns.git  
RUN cd /skydns && GOPATH=/root/go go get -d -v ./...  
RUN cd /skydns/skydnsctl/ && GOPATH=/root/go go build  
RUN mv /skydns/skydnsctl/skydnsctl /usr/local/bin/  
  
ENV SKYDNS 0.0.0.0:8080  
ENTRYPOINT ["skydnsctl"]


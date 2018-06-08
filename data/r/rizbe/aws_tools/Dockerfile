FROM golang  
MAINTAINER Rizbe  
  
RUN apt update  
RUN apt-get install python-dev build-essential python-pip -y  
RUN pip install awscli  
RUN go get -v github.com/barnybug/cli53/cmd/cli53  
  
CMD sleep infinity  


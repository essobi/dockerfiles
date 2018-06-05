# Has known vulnerabilities: you shouldn't use this in production, if you like
yourself.  
FROM golang:1.8-jessie  
MAINTAINER Jack Mannino <jack@nvisium.com>  
  
RUN apt-get update && apt-get install -y apt-transport-https  
# Install vulnerable bash version for ShellShock.  
RUN apt-get install -y build-essential wget  
RUN wget https://ftp.gnu.org/gnu/bash/bash-4.3.tar.gz && \  
tar zxvf bash-4.3.tar.gz && \  
cd bash-4.3 && \  
./configure && \  
make && \  
make install  
  
RUN mkdir /app  
ADD . /app/  
WORKDIR /app  
RUN go build -o main .  
CMD ["/app/main"]


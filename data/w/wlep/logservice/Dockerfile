FROM golang:latest  
ADD . /go/src/logservice  
RUN cd /go/src/logservice && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \  
echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-get update && \  
apt-get install -y mongodb-org && \  
systemctl enable mongod.service && \  
systemctl start mongod.service  
ENTRYPOINT /go/bin/logservice  
EXPOSE 9002


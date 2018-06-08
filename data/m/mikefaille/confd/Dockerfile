FROM nuagebec/etcd:latest  
MAINTAINER Michaël Faille <michael.faille@nuagebec.ca>  
ADD supervisor-confd.conf /etc/supervisor/conf.d/confd.conf  
  
# go get confd and prepare confd directories  
#RUN go get github.com/kelseyhightower/confd && mkdir -p /etc/confd/conf.d &&
mkdir -p /etc/confd/templates  
RUN wget
https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-
amd64 -O /usr/local/bin/confd && chmod +x /usr/local/bin/confd  
  
CMD ["/data/run.sh"]  


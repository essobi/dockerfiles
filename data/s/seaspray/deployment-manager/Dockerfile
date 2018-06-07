FROM golang  
#  
# https://github.com/adnanh/webhook  
RUN go get github.com/adnanh/webhook  
RUN mkdir -p /webhook  
RUN mkdir -p /var/webhook  
RUN chmod 777 /var/webhook  
  
# Ansible  
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367  
RUN apt-get update && apt-get install -y ansible  
  
# Gearman  
RUN apt-get update && apt-get install -y wget build-essential libboost-all-dev
gperf libevent-dev uuid-dev  
WORKDIR /tmp  
RUN wget
https://github.com/gearman/gearmand/releases/download/1.1.15/gearmand-1.1.15.tar.gz  
RUN tar xvzf gearmand-1.1.15.tar.gz  
WORKDIR /tmp/gearmand-1.1.15  
RUN ./configure  
RUN make && make install  
RUN LD_LIBRARY_PATH=/usr/local/lib ldconfig  
RUN rm -rf /tmp/gearmand-1.1.15.tar.gz /tmp/gearmand-1.1.15  
  
# Port  
EXPOSE 9000  
WORKDIR /var/webhook  
CMD []  
ENTRYPOINT ["/go/bin/webhook", "-hooks", "/webhook/hooks.json", "--verbose"]  
  


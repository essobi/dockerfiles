FROM ubuntu:trusty  
MAINTAINER Jordan Li  
RUN apt-get -y update  
RUN apt-get install -y -q python-software-properties software-properties-
common  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get -y update  
RUN apt-get install -y -q nodejs haproxy  
  
ADD ./haproxy-marathon-bridge /root/haproxy-marathon-bridge  
RUN chmod u+x /root/haproxy-marathon-bridge  
  
ADD ./app.js /data/app.js  
ADD ./package.json /data/package.json  
  
WORKDIR /data  
  
RUN npm install  
  
ADD ./run.sh /usr/local/bin/start-ha  
RUN chmod u+x /usr/local/bin/start-ha  
  
CMD /usr/local/bin/start-ha  


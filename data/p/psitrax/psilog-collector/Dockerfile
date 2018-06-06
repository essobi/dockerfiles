FROM webhippie/nodejs:latest  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
RUN apk update && apk add git  
  
WORKDIR /root  
RUN git clone https://github.com/psi-4ward/psilog-collector.git  
  
WORKDIR /root/psilog-collector  
RUN /usr/bin/npm install  
  
VOLUME ["/root/psilog-collector-config"]  
  
CMD ["/usr/bin/node", "/root/psilog-collector/bin/psilog-collector", "--
configdir" ,"/root/psilog-collector/conf.d", "--configdir", "/root/psilog-
collector-config"]  


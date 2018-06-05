FROM ubuntu:14.04  
RUN apt-get update && apt-get -y install build-essential libjansson-dev
libssl-dev libmicrohttpd-dev git jq  
  
RUN mkdir -p /opt/brubeck  
  
RUN git clone https://github.com/mhr3/brubeck.git /opt/brubeck/src  
  
RUN cd /opt/brubeck/src && ./script/bootstrap  
  
RUN cp /opt/brubeck/src/brubeck /opt/brubeck/  
  
RUN rm -rf /opt/brubeck/src  
  
ADD config.template.json /opt/brubeck/config.template.json  
  
ADD run_brubeck.sh /opt/brubeck/run_brubeck.sh  
  
EXPOSE 8080 8125/udp  
  
ENTRYPOINT ["/opt/brubeck/run_brubeck.sh"]  


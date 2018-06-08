FROM ubuntu:16.04  
MAINTAINER Andre da Silva Mesquita<andre@o2br.net>  
# Based off work by Patrick Valsecchi<patrick.valsecchi@camptocamp.com>  
#COPY build /build/scripts  
RUN apt-get -y update && apt-get install -y kimagemapeditor  
RUN apt-get autoclean -y  
  
ENV DISPLAY 192.168.99.1:0.0  
CMD ["/usr/bin/kimagemapeditor"]  
  
## private and public mapping  
#EXPOSE 80:8080  
## private only  
#EXPOSE 80  
#ENTRYPOINT ["/usr/bin/rethinkdb"]  
#CMD ["--help"]  


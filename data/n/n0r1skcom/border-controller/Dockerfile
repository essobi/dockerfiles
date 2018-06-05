FROM nginx  
  
MAINTAINER Mario Kleinsasser "mario.kleinsasser@gmail.com"  
MAINTAINER Bernhard Rausch "rausch.bernhard@gmail.com"  
RUN apt-get update && apt-get -y install dnsutils net-tools procps curl
inetutils-ping telnet  
  
COPY border-controller /data/border-controller  
RUN chmod 755 /data/border-controller  
  
COPY example/border-controller-config.tpl /config/border-controller-config.tpl  
COPY example/border-controller.yml /config/border-controller.yml  
  
CMD ["/data/border-controller"]  


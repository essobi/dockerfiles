FROM ubuntu:16.04  
MAINTAINER Mario Kleinsasser "mario.kleinsasser@gmail.com"  
MAINTAINER Bernhard Rausch "rausch.bernhard@gmail.com"  
ADD echo.py /echo.py  
RUN chmod 755 /echo.py  
  
# ToDo: Add parameters for not showing GUI warnings!  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get -y install python3 python3-netifaces net-tools
telnet dnsutils netcat curl  
  
EXPOSE 3333  
EXPOSE 3333/udp  
  
CMD ["python3", "-u", "/echo.py"]  


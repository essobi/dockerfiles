FROM java:8-jre-alpine  
MAINTAINER Bruno Wowk "bruno.wowk@gmail.com"  
ADD https://github.com/lightbody/browsermob-
proxy/releases/download/browsermob-proxy-2.1.2/browsermob-proxy-2.1.2-bin.zip
/home/  
WORKDIR /home  
RUN unzip browsermob-proxy-2.1.2-bin.zip && rm browsermob-proxy-2.1.2-bin.zip  
EXPOSE 8080-8200  
CMD /home/browsermob-proxy-2.1.2/bin/browsermob-proxy  


FROM openjdk:8-jre-alpine  
  
RUN apk update && apk add curl  
  
RUN mkdir -p /opt \  
&& cd /opt \  
&& curl -sSL http://ftp.ps.pl/pub/apache//jmeter/binaries/apache-
jmeter-3.1.tgz | tar -zxvf -  
  
ENV PATH=/opt/apache-jmeter-3.1/bin:$PATH  
WORKDIR /root  
CMD ["sh"]  


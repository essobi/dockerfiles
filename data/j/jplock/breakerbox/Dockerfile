FROM java:openjdk-8-jre-alpine  
MAINTAINER Justin Plock <justin@plock.net>  
  
ARG VERSION=0.4.3  
LABEL name="breakerbox" version=$VERSION  
  
RUN mkdir /opt \  
&& wget -q -O -
https://github.com/yammer/breakerbox/releases/download/breakerbox-
parent-$VERSION/breakerbox-$VERSION.tar.gz | tar -xzf - -C /opt  
  
EXPOSE 8080 8081  
WORKDIR /opt  
  
VOLUME ["/opt"]  
  
ENTRYPOINT ["java", "-jar", "breakerbox-service-0.4.3.jar"]  
CMD ["server", "breakerbox.yml"]  


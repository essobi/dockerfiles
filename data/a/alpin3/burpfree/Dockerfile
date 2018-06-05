FROM openjdk:8-jre-alpine  
MAINTAINER kost - https://github.com/kost  
  
ENV BURP_VERSION 1.7.06  
RUN apk --update add openssl ca-certificates ttf-dejavu && rm -f
/var/cache/apk/* && \  
mkdir -p /opt/burp /work && adduser -D -s /bin/sh user user && chown -R user
/work && \  
wget -q -O /opt/burp/burpsuite.jar
"https://portswigger.net/Burp/Releases/Download?productId=100&version=$BURP_VERSION&type=Jar"  
  
ADD config/ /home/user/  
RUN chown -R user /home/user/.*  
USER user  
WORKDIR /work  
  
ENTRYPOINT ["java", "-jar", "/opt/burp/burpsuite.jar"]  


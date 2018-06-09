FROM openjdk:10-jdk-slim  
  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
RUN apt-get update && \  
apt-get install -y curl tzdata imagemagick ttf-dejavu && \  
cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \  
echo "Europe/Moscow" > /etc/timezone && \  
apt-get clean  


FROM anapsix/alpine-java  
MAINTAINER Adrian Hobbs <adrianhobbs@gmail.com>  
ENV PACKAGE "tzdata"  
# Update packages in base image, avoid caching issues by combining statements,
install build software and deps  
RUN apk add --no-cache $PACKAGE && \  
cp /usr/share/zoneinfo/Australia/Sydney /etc/localtime && \  
echo "Australia/Sydney" > /etc/timezone && \  
# Add a user to run as non root  
adduser -D -g '' openhab  
  
# Add certificates  
ADD cacerts /opt/jdk/jre/lib/security/  
USER openhab  
WORKDIR /opt/openhab  
  
CMD ["/opt/openhab/start.sh"]  
  


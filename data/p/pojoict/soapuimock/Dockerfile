FROM openjdk:8-jdk-alpine  
  
MAINTAINER Pojo-ict  
  
ENV VERSION=5.2.1  
RUN apk update > /dev/null && \  
apk add curl && \  
mkdir /soapui && \  
curl -Lks
http://cdn01.downloads.smartbear.com/soapui/${VERSION}/SoapUI-${VERSION}-linux-
bin.tar.gz | \  
tar -xz -C /soapui && \  
mv /soapui/SoapUI-${VERSION}/* /soapui && \  
rmdir /soapui/SoapUI-${VERSION}  
ADD run.sh /  
CMD sh /run.sh  


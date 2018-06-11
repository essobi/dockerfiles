FROM openjdk:8-jre-alpine  
  
RUN apk --no-cache add bash procps  
RUN adduser -S knox  
  
ENV KNOX_VERSION 0.11.0  
RUN wget -q -O /knox-${KNOX_VERSION}.zip
http://download.nextag.com/apache/knox/${KNOX_VERSION}/knox-${KNOX_VERSION}.zip
&& unzip /knox-${KNOX_VERSION}.zip && rm knox-${KNOX_VERSION}.zip && ln -nsf
/knox-${KNOX_VERSION} /knox && chmod +x /knox/bin/*.sh && chown -R knox /knox/  
  
ADD master /knox/data/security/master  
RUN chown -R knox /knox/data/security  
  
ADD ldap.sh /ldap.sh  
RUN chmod 744 /ldap.sh  
ADD gateway.sh /gateway.sh  
RUN chmod 744 /gateway.sh  
  
USER knox  
WORKDIR /knox  


FROM haproxy  
MAINTAINER Christophe Burki, christophe.burki@gmail.com  
  
ENV CONFD_VERSION 0.11.0  
# Install confd  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 /usr/local/bin/confd  
RUN chmod a+x /usr/local/bin/confd  
  
# Install configuration and templates  
COPY confd/ /etc/confd/  
  
ENTRYPOINT ["confd"]  


# radiantbluetechnologies/rialto-proxyserver  
FROM radiantbluetechnologies/rialtobase-centos  
MAINTAINER mpg@flaxen.com  
  
ENV RIALTO_BRANCH=dev  
  
EXPOSE 8080  
RUN true  
  
COPY proxy.py /usr/local/bin/  
  
CMD /usr/local/bin/proxy.py 8080  


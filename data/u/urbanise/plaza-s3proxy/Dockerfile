FROM java:8-jre  
  
RUN mkdir -p /opt/s3proxy/data && cd /opt/s3proxy/ && wget
https://s3.amazonaws.com/plaza-deployment/s3proxy  
RUN chmod a+x /opt/s3proxy/s3proxy  
ADD ./s3proxy.conf /opt/s3proxy/s3proxy.conf  
  
VOLUME /data  
EXPOSE 10001  
WORKDIR /opt/s3proxy  
CMD ["java", "-jar", "s3proxy", "--properties", "./s3proxy.conf"]  


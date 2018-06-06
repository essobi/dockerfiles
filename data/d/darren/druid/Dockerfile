FROM java:jre  
  
ENV DRUID_VER 0.6.165  
WORKDIR /druid  
  
RUN curl -L "http://static.druid.io/artifacts/releases/druid-
services-$DRUID_VER-bin.tar.gz" \  
| tar -xzvf - --strip=1  
  
EXPOSE 8000  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  


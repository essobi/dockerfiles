FROM java:8  
RUN mkdir /code  
WORKDIR /code  
ADD . /code  
  
RUN adduser --disabled-password --gecos "" -u 1000 chronix && chown -R
chronix:chronix /code  
  
USER chronix  
  
  
RUN ./gradlew --no-daemon clean build copyIntegrationRuntimeLibs  
  
CMD ["./gradlew", "--no-daemon", "startSolrForeground"]  


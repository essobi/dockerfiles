FROM aeonproject/openjdk-jre  
  
ARG VERSION=0.7.0  
ARG RESPOSITORY_URL=https://dl.bintray.com/ptrthomas/karate/karate-
netty-$VERSION-all.jar  
RUN echo "using karate netty mock server version $RESPOSITORY_URL"  
RUN mkdir -p /opt/karatemock &&\  
wget -O /opt/karatemock/karate.jar $RESPOSITORY_URL  
  
COPY feature/ /opt/karatemock/feature/  
  
WORKDIR /opt/karatemock  
  
# expose ports.  
EXPOSE 8032  
ENTRYPOINT ["java","-jar","/opt/karatemock/karate.jar","-m","./feature/demo-
mock.feature","-p","8032"]  


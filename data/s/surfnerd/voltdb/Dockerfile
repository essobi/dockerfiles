FROM java:openjdk-7-jdk  
  
RUN gpg --keyserver pgpkeys.mit.edu --recv-key 379CE192D401AB61 && \  
gpg -a --export 379CE192D401AB61 | apt-key add -  
  
RUN apt-get update && apt-get install apt-transport-https  
  
RUN echo "deb https://dl.bintray.com/msuret/deb stable main" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install voltdb-community  
  
ENTRYPOINT ["voltdb", "create"]  
  
EXPOSE 21212 21211 8080 3021 4560 9090 5555 7181  


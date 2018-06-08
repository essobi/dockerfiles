FROM java:latest  
MAINTAINER Pierre Laperdrix  
  
ADD website /opt/tmp/  
WORKDIR /opt/tmp/  
RUN ./activator stage && cp -r target/universal/stage/ /opt/website/ &&
./activator clean && rm -r /opt/tmp/ /root/.sbt/ /root/.ivy2/  
WORKDIR /opt/website/  
  
CMD ["./bin/website"]  


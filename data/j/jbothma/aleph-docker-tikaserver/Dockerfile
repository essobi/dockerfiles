FROM tesseractshadow/tesseract4re  
MAINTAINER mark.nganga@andela.com  
  
COPY . /tika-server  
WORKDIR /tika-server  
  
RUN apt-get update \  
&& apt-get install -y openjdk-8-jre-headless \  
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 9998  
ENTRYPOINT java -jar tika-server-1.15-SNAPSHOT.jar -h 0.0.0.0  


FROM develar/java:8u45  
  
MAINTAINER Firdaus Ismail Sholeh (firdaus_is@yahoo.com)  
  
ADD jar/KafkaTaxiProducer.jar /root/KafkaTaxiProducer.jar  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/urandom"]  
  
# Define default command.  
# CMD ["-jar", "/root/KafkaTaxiProducer.jar",
"lovelymachine1.cloudapp.net:9092", "taxi", "/debs/sorted_data.csv.gz", "0"]  


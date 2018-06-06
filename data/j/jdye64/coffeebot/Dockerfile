FROM jdye64/coffeebot:baseline  
MAINTAINER Jeremy Dyer  
  
ENV GIT_HADOOP_SUMMIT_HOME /HadoopSummit  
  
# Install the Custom NiFi processors that will be ran on the Docker container
for the device connected to the USB scale.  
RUN git clone https://github.com/jdye64/HadoopSummit.git  
  
# Installs the custom processors on the local Apache NiFi instance  
RUN cd $GIT_HADOOP_SUMMIT_HOME/CoffeeBot/NiFiCustomProcessors/nifi-usb && mvn
clean install package && cp ./nifi-usb-nar/target/nifi-usb-nar-0.6.1.nar
$NIFI_HOME/lib


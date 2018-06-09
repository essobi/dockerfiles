FROM jdye64/hadoopsummit:summit_baseline  
MAINTAINER Jeremy Dyer  
  
# FYI - GIT_HADOOP_SUMMIT_HOME & NIFI_HOME ENV variales are defined in parent
Docker image  
RUN apt-get install -y libv4l-dev dv4l v4l-utils mysql-client-5.6  
  
# Adds the custom NiFi processors  
ADD nifi/lib /nifi-0.6.1/lib  
  
# Clones the Github repo to the local container  
#RUN git clone https://github.com/jdye64/HadoopSummit.git  
# Build the "nifi-opencv" custom processor and add to local installation  
#RUN cd $GIT_HADOOP_SUMMIT_HOME/NiFiCustomProcessors/nifi-opencv && mvn clean
install package -DskipTests && cp ./nifi-opencv-nar/target/nifi-opencv-
nar-0.6.1.nar $NIFI_HOME/lib  
# Build the "nifi-ocr" custom processor and add to local installation  
#RUN cd $GIT_HADOOP_SUMMIT_HOME/NiFiCustomProcessors/nifi-ocr && mvn clean
install package -DskipTests && cp ./nifi-ocr-nar/target/nifi-ocr-nar-0.6.1.nar
$NIFI_HOME/lib  
# Build the "nifi-barcode" custom processor and add to local installation  
#RUN cd $GIT_HADOOP_SUMMIT_HOME/NiFiCustomProcessors/nifi-barcode && mvn clean
install package && cp ./nifi-barcode-nar/target/nifi-barcode-nar-0.6.1.nar
$NIFI_HOME/lib  
# Add test image assets  
ADD images /images  
  
EXPOSE 9090  
EXPOSE 9091  
# Set NiFi configuration  
RUN rm -rf ./nifi-0.6.1/conf  
ADD nifi/conf /nifi-0.6.1/conf  
ADD nifi/extras /nifi-0.6.1/extras  
ADD mysql/Data.csv /


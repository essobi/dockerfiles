FROM dockerfile/java:oracle-java8  
MAINTAINER gingerbeard <kulishovt@gmail.com>  
  
RUN wget http://download-aws.ej-
technologies.com/jprofiler/jprofiler_linux_8_1_2.tar.gz -P /tmp/ &&\  
tar -xzf /tmp/jprofiler_linux_8_1_2.tar.gz -C /usr/local &&\  
rm /tmp/jprofiler_linux_8_1_2.tar.gz  
  
ENV
JPAGENT_PATH="-agentpath:/usr/local/jprofiler8/bin/linux-x64/libjprofilerti.so=nowait"  
EXPOSE 8849  
CMD ["bash"]  
  


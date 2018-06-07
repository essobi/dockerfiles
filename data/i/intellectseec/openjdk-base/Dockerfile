FROM openjdk:8-jdk  
  
RUN apt-get update  
  
RUN curl -L -O
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.6.3-amd64.deb
\  
&& dpkg -i filebeat-5.6.3-amd64.deb && rm -f filebeat-5.6.3-amd64.deb  
  
###LOG Configuration##################  
RUN mkdir /Intellect-Logs  
ENV INTELLECT_LOG_LOC /Intellect-Logs  
ENV INTELLECT_LOG_FILENAME log-file-name-here-without-extension  
######################################


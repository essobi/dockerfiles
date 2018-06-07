FROM nginx  
  
###############################################################################  
# INSTALLATION  
###############################################################################  
  
ENV FILEBEAT_VERSION 5.0.0  
  
RUN apt-get update -qq \  
&& apt-get install -qqy curl \  
&& apt-get clean  
  
RUN curl -L -O
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-amd64.deb
\  
&& dpkg -i filebeat-${FILEBEAT_VERSION}-amd64.deb \  
&& rm filebeat-${FILEBEAT_VERSION}-amd64.deb  
  
  
###############################################################################  
# CONFIGURATION  
###############################################################################  
  
ADD filebeat.yml /etc/filebeat/filebeat.yml  
ADD GeoLiteCity.dat /usr/share/GeoIP/GeoLiteCity.dat  
  
###############################################################################  
# START  
###############################################################################  
  
ADD ./start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
CMD [ "/usr/local/bin/start.sh" ]  


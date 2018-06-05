FROM openjdk:8-jdk  
  
MAINTAINER Adaptris  
  
EXPOSE 8080  
EXPOSE 5555  
  
ADD docker-entrypoint.sh /  
RUN mkdir -p /opt/interlok/logs  
WORKDIR /opt/interlok/  
  
RUN wget -q https://development.adaptris.net/installers/Interlok/3.7.2/base-
filesystem.zip && \  
wget -q https://development.adaptris.net/installers/Interlok/3.7.2/runtime-
libraries.zip && \  
wget -q
https://development.adaptris.net/installers/Interlok/3.7.2/javadocs.zip && \  
unzip -o -q javadocs.zip && \  
unzip -o -q runtime-libraries.zip && \  
unzip -o -q base-filesystem.zip && \  
rm -rf /opt/interlok/optional && \  
rm -rf /opt/interlok/docs/javadocs/optional && \  
chmod +x /docker-entrypoint.sh && \  
rm -rf *.zip  
  
VOLUME [ "/opt/interlok/config", "/opt/interlok/logs" , "/opt/interlok/ui-
resources" ]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  


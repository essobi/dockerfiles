FROM openjdk:latest  
  
LABEL build="201802101315"  
LABEL maintainer "marc.jakob@bs.ch"  
  
COPY start.sh /  
  
RUN cd /opt/ && \  
wget http://download.oracle.com/glassfish/5.0/release/glassfish-5.0.zip && \  
unzip glassfish-5.0.zip -x "glassfish5/glassfish/domains/*" && \  
rm -f glassfish-5.0.zip && \  
ln -s /opt/glassfish5 /opt/glassfish && \  
chmod 0750 /start.sh  
  
EXPOSE 8080 8181 4848  
VOLUME ["/opt/glassfish/glassfish/domains"]  
ENTRYPOINT ["/start.sh"]  


FROM java:8  
MAINTAINER uchhatre@gmail.com  
EXPOSE 6080  
RUN curl -SL http://central.maven.org/maven2/com/newrelic/agent/java/newrelic-
java/3.36.0/newrelic-java-3.36.0.zip -o /tmp/nr.zip && \  
unzip /tmp/nr.zip -d /opt/ && \  
rm /tmp/nr.zip  
COPY run.sh /  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  


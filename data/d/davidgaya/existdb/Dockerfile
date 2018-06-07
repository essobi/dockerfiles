FROM java:8-jre  
MAINTAINER David Gaya  
  
# eXistDB needs ant to automate common tasks like backup/restore or importing  
RUN apt-get update; apt-get -y install ant ant-optional; apt-get clean  
  
# install exist and cleanup  
RUN wget -q -O '/opt/exist.jar'
'https://bintray.com/artifact/download/existdb/releases/eXist-db-
setup-2.2.jar' && \  
echo 'INSTALL_PATH=/opt/exist' > '/opt/options.txt' && \  
java -jar '/opt/exist.jar' -options '/opt/options.txt' && \  
rm -f '/opt/exist.jar' '/opt/options'  
  
ENV MAX_MEMORY 512  
RUN sed -i "s/Xmx%{MAX_MEMORY}m/Xmx\${MAX_MEMORY}m/g"
/opt/exist/bin/functions.d/eXist-settings.sh  
# prefix java command with exec to force java being process 1 and receiving
docker signals  
RUN sed -i 's/^\"${JAVA_RUN/exec \"${JAVA_RUN/' /opt/exist/bin/startup.sh  
  
ADD entrypoint.sh /entrypoint.sh  
CMD ["/entrypoint.sh"]  
ENV EXIST_HOME /opt/exist  
VOLUME /opt/exist/webapp/WEB-INF/data/  
  
EXPOSE 8080 8443  


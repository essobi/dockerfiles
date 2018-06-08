FROM nukesz/java:latest  
MAINTAINER Norbert Benczur, norbert.benczur@gmail.com  
RUN wget --max-redirect=1 http://bit.ly/1oVscoT -O /opt/payara41.zip  
RUN unzip /opt/payara41.zip -d /opt  
RUN rm /opt/payara41.zip  
ENTRYPOINT /opt/payara41/glassfish/bin/asadmin start-domain --verbose  
EXPOSE 4848 8080


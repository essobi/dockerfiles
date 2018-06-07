# Base image with Caucho Resin running on Oracle JDK 8  
FROM expertsystems/oracle-jdk8:u74  
  
# Install Resin  
RUN curl -O
http://caucho.com/download/rpm-6.5/4.0.40/x86_64/resin-4.0.40-1.x86_64.rpm &&
\  
yum localinstall -y resin-4.0.40-1.x86_64.rpm && \  
yum clean all && \  
rm resin-4.0.40-1.x86_64.rpm  
  
# Set RESIN_HOME  
ENV RESIN_HOME=/usr/local/share/resin-4.0.40  
# Add MySQL JDBC driver Connector/J  
RUN cd /var/resin/webapp-jars && \  
yum -y install unzip && \  
yum clean all && \  
curl -LO http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.38.zip && \  
unzip -j mysql-connector-java-5.1.38.zip mysql-connector-java-5.1.38/mysql-
connector-java-5.1.38-bin.jar && \  
rm mysql-connector-java-5.1.38.zip  
  
# Configure entrypoint and default argument  
# (Alternative java -jar ${RESIN_HOME}/lib/resin.jar")  
ENTRYPOINT ["/usr/local/share/resin-4.0.40/bin/resinctl"]  
CMD ["console"]


FROM lucee/lucee5:latest  
  
# Add Lib to server  
COPY ./com/mongodb/lib/cfmongodb.jar /opt/lucee/server/lucee-
server/context/lib/cfmongodb.jar  
COPY ./com/mongodb/lib/mongo-java-driver-2.13.1.jar /opt/lucee/server/lucee-
server/context/lib/mongo-java-driver-2.13.1.jar  
COPY ./com/mongodb/lib/mxunit-ant.jar /opt/lucee/server/lucee-
server/context/lib/mxunit-ant.jar  
COPY ./com/mongodb/lib/javaloader /opt/lucee/server/lucee-
server/context/lib/javaloader  
# Add lib to web  
COPY ./com/mongodb/lib/cfmongodb.jar /opt/lucee/web/lib/cfmongodb.jar  
COPY ./com/mongodb/lib/mongo-java-driver-2.13.1.jar /opt/lucee/web/lib/mongo-
java-driver-2.13.1.jar  
COPY ./com/mongodb/lib/mxunit-ant.jar /opt/lucee/web/lib/mxunit-ant.jar  
COPY ./com/mongodb/lib/javaloader /opt/lucee/web/lib/javaloader  
# Create Lucee configs  
COPY lucee-web.xml.cfm /opt/lucee/web/lucee-web.xml.cfm  
COPY lucee-server.xml /opt/lucee/server/lucee-server/context/lucee-server.xml  
COPY server.xml /usr/local/tomcat/conf/server.xml  
  
RUN mkdir www  
ADD . /var/www  
VOLUME /var/www


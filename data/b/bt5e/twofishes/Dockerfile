FROM alpine:3.2  
RUN apk add --update openjdk7-jre unzip bash  
RUN mkdir -p /opt/twofishes \  
&& wget http://twofishes.net/binaries/server-assembly-0.84.9.jar -P
/opt/twofishes \  
&& wget http://twofishes.net/indexes/revgeo/2015-03-05.zip -P /opt/twofishes \  
&& unzip /opt/twofishes/2015-03-05.zip -d /opt/twofishes \  
&& rm /opt/twofishes/2015-03-05.zip  
  
EXPOSE 8080 8081 8082 8083  
CMD java -jar /opt/twofishes/server-assembly-0.84.9.jar --hfile_basepath
/opt/twofishes/2015-03-05-20-05-30.753698


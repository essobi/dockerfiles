FROM java:8-jre-alpine  
MAINTAINER Vlad Nemes <me@vladnem.es>  
  
WORKDIR /var/workbench  
  
RUN apk add --no-cache unzip curl && \  
rm -rf /var/cache/apk/* && \  
mkdir /var/driver && \  
curl -o /var/driver/athena.jar https://s3.amazonaws.com/athena-
downloads/drivers/AthenaJDBC41-1.0.0.jar && \  
curl -o /tmp/workbench.zip http://www.sql-workbench.net/Workbench-Build121.zip
&& \  
unzip /tmp/workbench.zip -d /var/workbench && \  
rm -f /tmp/workbench.zip && \  
apk del unzip curl  
  
ENTRYPOINT ["java", \  
"-jar", "sqlworkbench.jar", \  
"-driver=com.amazonaws.athena.jdbc.AthenaDriver", \  
"-driverjar=/var/driver/athena.jar", \  
"-displayResult=true"]  


FROM openjdk:8-jre AS build-env  
LABEL maintainer="Gokhan Sengun <gokhansengun@gmail.com>"  
  
ADD https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-4.0.zip
/apache-jmeter.zip  
RUN unzip /apache-jmeter.zip -d /  
  
RUN curl -L -o /usr/bin/jq
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && chmod
u+x /usr/bin/jq  
  
FROM openjdk:8-jre AS runtime-env  
COPY \--from=build-env /apache-jmeter-4.0 /jmeter  
COPY \--from=build-env /usr/bin/jq /usr/bin/jq  
  
RUN ln -s /jmeter/bin/jmeter /usr/local/bin/jmeter  
  
# Copy plugins folder under ext folder  
COPY plugins/ /jmeter/lib/ext/  
  
# Copy MSSQL and PostgreSQL JDBC Drivers  
COPY jdbc/postgresql-9.4.1209.jre7.jar /jmeter/lib/  
COPY jdbc/sqljdbc4.jar /jmeter/lib/  
  
# Change workdir to /jmeter  
WORKDIR /jmeter  
  
CMD [ "jmeter", "--help" ]  


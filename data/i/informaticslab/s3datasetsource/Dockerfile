FROM maven:3  
RUN mkdir /build  
COPY . /build  
WORKDIR /build  
RUN mvn clean install  
RUN ls /build/target/s3datasetsource-1.0-SNAPSHOT-jar-with-dependencies.jar  
CMD echo "done"  
  
FROM unidata/thredds-docker:4.6.10  
RUN apt-get update && apt-get install -y python3 python3-pip  
RUN pip3 install boto3 jinja2  
COPY ingest.py /usr/local/src/ingest.py  
COPY threddsConfig.xml /usr/local/tomcat/content/thredds/threddsConfig.xml  
COPY ./src/templates/ /usr/local/src/templates/  
COPY go.sh /go.sh  
COPY \--from=0 /build/target/s3datasetsource-1.0-SNAPSHOT-jar-with-
dependencies.jar /usr/local/tomcat/webapps/thredds/WEB-
INF/lib/s3datasetsource-1.0-SNAPSHOT-jar-with-dependencies.jar  
ENTRYPOINT [""]  
CMD ["/go.sh"]


FROM tomcat:8.0-jre8-alpine  
MAINTAINER Vishwa <hello@vishwa.be>  
  
# Env's  
ENV WEBPROTEGE_URL
https://github.com/protegeproject/webprotege/releases/download/v2.6.0/webprotege-2.6.0.war  
  
RUN apk add --update --no-cache \  
vim \  
unzip \  
wget  
  
RUN mkdir -p /data/webprotege  
  
WORKDIR /usr/local/tomcat/webapps  
RUN rm -rf * \  
&& wget ${WEBPROTEGE_URL} -O webprotege.war  
RUN unzip -q webprotege.war -d ROOT \  
&& rm webprotege.war \  
&& sed -i 's/#mongodb.host=localhost/mongodb.host=mongo/g' ROOT/WEB-
INF/classes/webprotege.properties  
COPY webprotege.properties ROOT/webprotege.properties  
  
VOLUME /data/webprotege  
EXPOSE 8080  
CMD ["catalina.sh", "run"]


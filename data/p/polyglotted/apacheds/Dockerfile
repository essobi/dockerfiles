FROM polyglotted/java-base  
MAINTAINER pgtdev@polyglotted.io  
  
ENV DS_VER M23  
ENV DS_NAME apacheds-2.0.0-${DS_VER}  
WORKDIR /tmp  
  
RUN apk add --update zip unzip openldap-clients wget && \  
mkdir -p /opt && \  
cd /opt && \  
wget --no-check-certificate
https://www.apache.org/dist/directory/apacheds/dist/2.0.0-${DS_VER}/${DS_NAME}.zip
&& \  
unzip ${DS_NAME}.zip && \  
apk del zip unzip && \  
rm ${DS_NAME}.zip  
  
WORKDIR /opt/${DS_NAME}  
  
COPY files/config.ldif /opt/${DS_NAME}/instances/default/conf/  
COPY files/sample.ldif /tmp/  
  
RUN chmod ugo+x bin/apacheds.sh && \  
bin/apacheds.sh start && sleep 20 && \  
ldapmodify -h 127.0.0.1 -p 10389 -x -a -v < /tmp/sample.ldif && \  
bin/apacheds.sh stop && sleep 5 && \  
rm /tmp/sample.ldif  
  
EXPOSE 10389  
CMD ["bin/apacheds.sh", "default", "run"]  


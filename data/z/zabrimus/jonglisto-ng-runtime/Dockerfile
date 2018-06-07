FROM anapsix/alpine-java:8u152b16_server-jre  
  
ENV PATH /usr/local/tomee/bin:$PATH  
RUN mkdir -p /usr/local/tomee  
  
WORKDIR /usr/local/tomee  
  
RUN set -x \  
&& apk upgrade \--update \  
&& apk add \--no-cache curl \  
&& curl -fSL https://repo.maven.apache.org/maven2/org/apache/tomee/apache-
tomee/7.0.4/apache-tomee-7.0.4-webprofile.tar.gz -o tomee.tar.gz \  
&& tar -zxf tomee.tar.gz \  
&& mv apache-tomee-webprofile-7.0.4/* /usr/local/tomee \  
&& rm -Rf apache-tomee-webprofile-7.0.4 \  
&& rm bin/*.bat \  
&& rm tomee.tar.gz* \  
&& rm -Rf /usr/local/tomee/webapps/* \  
&& mkdir /etc/jonglisto \  
&& mkdir /var/jonglisto-ng \  
  
&& curl -fSL https://github.com/Zabrimus/jonglisto-
ng/releases/download/v0.2.3/jonglisto-ng-0.2.3.tar.gz -o /tmp/jonglisto-
ng.tar.gz \  
&& cd /tmp \  
&& tar -zxf jonglisto-ng.tar.gz \  
&& mv jonglisto-ng*war /usr/local/tomee/webapps/jonglisto-ng.war \  
  
&& echo "#!/bin/sh" > /usr/local/bin/start_tomee.sh \  
&& echo "if [ ! -f /etc/jonglisto/jonglisto-ng.xml ]; then" >>
/usr/local/bin/start_tomee.sh \  
&& echo " cp /tmp/jonglisto-ng.xml /etc/jonglisto/jonglisto-ng.xml" >>
/usr/local/bin/start_tomee.sh \  
&& echo "fi" >> /usr/local/bin/start_tomee.sh \  
  
&& echo "if [ ! -f /etc/jonglisto/security.ini ]; then" >>
/usr/local/bin/start_tomee.sh \  
&& echo " cp /tmp/security.ini /etc/jonglisto/security.ini" >>
/usr/local/bin/start_tomee.sh \  
&& echo "fi" >> /usr/local/bin/start_tomee.sh \  
  
&& echo "if [ ! -f /etc/jonglisto/remote.xml ]; then" >>
/usr/local/bin/start_tomee.sh \  
&& echo " cp /tmp/remote.xml /etc/jonglisto/remote.xml" >>
/usr/local/bin/start_tomee.sh \  
&& echo "fi" >> /usr/local/bin/start_tomee.sh \  
&& echo "cd /usr/local/tomee/bin" >> /usr/local/bin/start_tomee.sh \  
  
&& echo "./catalina.sh run" >> /usr/local/bin/start_tomee.sh \  
  
&& chmod +x /usr/local/bin/start_tomee.sh  
  
EXPOSE 8080  
CMD ["/usr/local/bin/start_tomee.sh"]  


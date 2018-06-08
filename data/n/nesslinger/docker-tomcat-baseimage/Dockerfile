FROM nesslinger/docker-java-baseimage  
  
MAINTAINER Michael Neßlinger <Michael.Nesslinger@gmx.de>  
  
# Define al the variables needed later in this docker file  
# Define default username and password for admin user.  
# You should override these by providing them as parameters  
ENV AdminUser admin  
ENV AdminPassword admin  
  
ENV TOMCAT_MAJOR_VERSION 8  
ENV TOMCAT_MINOR_VERSION 8.0.21  
ENV CATALINA_HOME /usr/local/tomcat/apache-tomcat-${TOMCAT_MINOR_VERSION}  
  
ENV MD5_SUM 7972dfc3a1e9b9a78738379f7e755a11 *apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz  
  
ENV LOGSTASH_MAJOR_VERSION 2  
ENV LOGSTASH_MINOR_VERSION 2.3  
RUN mkdir -p /opt/config /var/log/supervisor  
  
# Copy configuration template for apt  
ADD ./configuration/apt_template.conf /opt/config/apt_template.conf  
RUN chmod a+r /opt/config/apt_template.conf  
  
# Copy configuration template for curl  
ADD ./configuration/.curlrc_template /opt/config/.curlrc_template  
RUN chmod a+r /opt/config/.curlrc_template  
  
# Copy script to update the configuration  
ADD ./configuration/Fix_Proxy_Settings.sh /opt/config/Fix_Proxy_Settings.sh  
RUN chmod a+x /opt/config/Fix_Proxy_Settings.sh  
  
RUN sudo apt-get -q update && sudo apt-get -q -y install gettext-base
supervisor  
  
COPY ./configuration/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Fix proxy seetings depended on the existence of the following varibales:  
# DOCKER_CONTAINER_PROXY_PROTOCOL  
# DOCKER_CONTAINER_PROXY_HOST  
# DOCKER_CONTAINER_PROXY_PORT  
RUN /opt/config/Fix_Proxy_Settings.sh  
  
# INSTALL LOGSTASH  
RUN curl -s -o key https://packages.elastic.co/GPG-KEY-elasticsearch  
RUN sudo apt-key add key  
RUN echo "deb http://packages.elastic.co/logstash/2.3/debian stable main" |
sudo tee -a /etc/apt/sources.list  
  
RUN sudo apt-get update && sudo apt-get install logstash  
  
# INSTALL TOMCAT  
RUN mkdir -p /usr/local/tomcat  
RUN curl -o /tmp/apache-tomcat-${TOMCAT_MINOR_VERSION}.tar.gz
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz  
RUN echo "$MD5_SUM"  
RUN echo "$MD5_SUM" > /tmp/apache-tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5  
RUN cat /tmp/apache-tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5  
RUN cd /tmp/; md5sum --check -w /tmp/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5  
RUN tar zxf /tmp/apache-tomcat-${TOMCAT_MINOR_VERSION}.tar.gz -C
/usr/local/tomcat  
RUN rm /tmp/apache-tomcat-${TOMCAT_MINOR_VERSION}.tar.gz  
  
ADD ./configuration/tomcat-users.xml ${CATALINA_HOME}/conf/tomcat-users.xml  
  
RUN sed -i -e"s/%AdminUser%/$AdminUser/" $CATALINA_HOME/conf/tomcat-users.xml  
RUN sed -i -e"s/%AdminPassword%/$AdminPassword/" $CATALINA_HOME/conf/tomcat-
users.xml  
  
EXPOSE 8080  
CMD ["/usr/bin/supervisord"]  


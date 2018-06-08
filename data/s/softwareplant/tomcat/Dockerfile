# Pull base image.  
FROM softwareplant/base:centos  
  
RUN yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel
java-1.8.0-openjdk-debuginfo httpd zip  
  
#Chrome & Node install  
#RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
#RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install  
#RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
#RUN apt-get install -y nodejs  
#RUN npm install -g --allow-root --unsafe-perm=true puppeteer@1.0.0  
#RUN echo "export NODE_PATH=$(npm root --quiet -g)" >> /etc/profile.d/lib.sh  
#RUN echo "alias node='node -e \"\\`cat $1 | sed \"s/var config = {};/var
config = {args: \\[\'--no-sandbox\'\\]};/\"\\`' " >> /etc/profile.d/lib.sh  
# Tomcat installation  
RUN set -x && \  
groupadd tomcat && \  
useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat && \  
cd /tmp && \  
wget --progress=dot:mega
http://ftp.man.poznan.pl/apache/tomcat/tomcat-8/v8.0.52/bin/apache-
tomcat-8.0.52.tar.gz && \  
tar xzvf apache-tomcat-8*tar.gz -C /opt/tomcat --strip-components=1 && \  
cd /opt/tomcat && \  
chgrp -R tomcat /opt/tomcat && \  
chmod -R g+r conf && \  
chmod g+x conf && \  
chown -R tomcat /opt/tomcat  
  
# Add files  
COPY ./tomcat-users.xml /opt/tomcat/conf  
COPY ./manager.xml /opt/tomcat/conf/Catalina/localhost  
COPY ./server.xml /opt/tomcat/conf  
COPY ./biggantt.properties /opt/tomcat  
COPY ./jmxremote.password /opt/tomcat/conf  
COPY ./jmxremote.access /opt/tomcat/conf  
COPY ./httpd.conf /etc/httpd/conf  
COPY ./00_app.conf /etc/httpd/conf.d  
  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
EXPOSE 80  
EXPOSE 10001  
EXPOSE 10002  
EXPOSE 6666  
EXPOSE 8080  
EXPOSE 8009  
#VOLUME "/opt/tomcat/webapps"  
WORKDIR /opt/tomcat  
  
RUN rm -rf /opt/tomcat/ROOT.war && rm -rf /opt/tomcat/ROOT  
  
# Copy webapps  
COPY ./m3-java-capstone-1.0.war /opt/tomcat/webapps  
COPY ./app/ROOT.war /opt/tomcat/webapps  
#RUN unzip ./app/ROOT.war -d /opt/tomcat/webapps/ROOT  
RUN set -x && \  
chgrp -R tomcat /opt/tomcat && \  
chown -R tomcat /opt/tomcat && \  
chmod -R 755 conf  
  
# Timezone fix  
RUN ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime  
  
# Docker entry  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
RUN chmod 755 /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD [""]  


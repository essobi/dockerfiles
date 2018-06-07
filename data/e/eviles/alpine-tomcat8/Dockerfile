FROM eviles/alpine-oracle-jdk8  
  
ARG TOMCAT_VERSION=8.5.15  
ENV CATALINA_HOME=/usr/local/tomcat  
ENV CLASSPATH=$CLASSPATH:$CATALINA_HOME/common/lib  
ENV PATH=$PATH:$CATALINA_HOME/bin  
  
RUN curl -s -L --url
"http://www.us.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz" | tar xz -C /usr/local \  
&& ln -s /usr/local/apache-tomcat-${TOMCAT_VERSION} /usr/local/tomcat \  
&& sed -i 's/redirectPort="8443"/redirectPort="8443" URIEncoding="UTF-8"/g'
/usr/local/tomcat/conf/server.xml \  
&& echo "CATALINA_HOME=$CATALINA_HOME" >> /etc/profile \  
&& echo "CLASSPATH=\$CLASSPATH:\$CATALINA_HOME/common/lib" >> /etc/profile \  
&& echo "PATH=\$PATH:\$CATALINA_HOME/bin" >> /etc/profile \  
&& echo "export PATH CLASSPATH CATALINA_HOME" >> /etc/profile \  
&& echo "[program:tomcat]" >> /etc/supervisord.conf \  
&& echo "command=/usr/local/tomcat/bin/catalina.sh run" >>
/etc/supervisord.conf  
  
EXPOSE 8080  
VOLUME /usr/local/tomcat/webapps  


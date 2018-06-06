FROM combro2k/debian-debootstrap:8  
ENV HOME /root  
ENV DJIGZO_VERSION 2.10.0-3  
RUN apt-get update && \  
apt-get install postgresql postfix openjdk-7-jre openjdk-7-jre-headless
tzdata-java ant ant-optional mktemp wget libsasl2-modules symlinks sudo
tomcat7 -yq && \  
adduser --system --group --home /usr/local/djigzo --disabled-password --shell
/bin/false djigzo && \  
usermod -a -G adm djigzo && \  
mkdir /usr/local/djigzo-web  
RUN chown djigzo:djigzo /usr/local/djigzo-web  
  
WORKDIR /tmp  
  
RUN wget https://www.ciphermail.com/downloads/djigzo-
release-${DJIGZO_VERSION}/djigzo_${DJIGZO_VERSION}.tar.gz  
RUN wget https://www.ciphermail.com/downloads/djigzo-
release-${DJIGZO_VERSION}/djigzo-web_${DJIGZO_VERSION}.tar.gz  
  
RUN sudo -u djigzo tar zxvf djigzo_${DJIGZO_VERSION}.tar.gz --directory
/usr/local/djigzo  
RUN sudo -u djigzo tar zxvf djigzo-web_${DJIGZO_VERSION}.tar.gz --directory
/usr/local/djigzo-web  
  
WORKDIR /var/lib/postgresql/9.3/main  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
RUN cd /usr/local/djigzo && sudo -u djigzo ant  
  
RUN /etc/init.d/postgresql start &&\  
sudo -u postgres psql --command "CREATE USER djigzo NOCREATEUSER NOCREATEDB
ENCRYPTED PASSWORD 'md5b720bc9de4ca53d53a4059882a0868b9';" &&\  
sudo -u postgres createdb --owner djigzo djigzo &&\  
sudo -u djigzo psql djigzo < /usr/local/djigzo/conf/djigzo.sql  
  
RUN bash -c 'echo "DJIGZO_HOME=/usr/local/djigzo"' >> /etc/default/djigzo  
RUN ln -s /usr/local/djigzo/scripts/djigzo /etc/init.d/  
  
RUN echo "JAVA_OPTS=\"\$JAVA_OPTS -Djigzo-web.home=/user/local/djigzo-web\""
>> /etc/default/tomcat7  
RUN echo "TOMCAT7_SECURITY=no" >> /etc/default/tomcat7  
RUN chown tomcat7:djigzo /usr/local/djigzo-web/ssl/sslCertificate.p12  
  
RUN cp /usr/local/djigzo-web/conf/tomcat/server.xml /etc/tomcat7/server.xml  
RUN sed 's#/share/djigzo-web/#/local/djigzo-web/#' /etc/tomcat7/server.xml
--in-place  
  
RUN echo "<Context docBase=\"/usr/local/djigzo-web/djigzo.war\"
unpackWAR=\"false\"/>" > /etc/tomcat7/Catalina/localhost/djigzo.xml  
RUN echo "<Context docBase=\"/usr/local/djigzo-web/djigzo-portal.war\"
unpackWAR=\"false\"/>" > /etc/tomcat7/Catalina/localhost/web.xml  
  
RUN /etc/init.d/postgresql stop  
RUN chmod -R +x /usr/local/djigzo/scripts/*  
  
WORKDIR /usr/local/djigzo/resources/certificates  
  
RUN wget https://www.ciphermail.com/downloads/roots.p7b  
RUN wget https://www.ciphermail.com/downloads/intermediates.p7b  
  
RUN chown -R djigzo:djigzo ./  
  
ADD init.sh /root/init.sh  
RUN chmod +x /root/init.sh  
  
EXPOSE 8443  
VOLUME ["/var/lib/postgresql"]  
  
WORKDIR /root  
  
CMD /root/init.sh  


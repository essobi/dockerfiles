FROM okieoth/d_jre7:0.1  
RUN apt-get update  
  
RUN apt-get install -y locales wget curl unzip imagemagick net-tools && \  
locale-gen "de_DE.UTF-8" && dpkg-reconfigure locales && \  
rm -rf /var/lib/apt/lists/* && \  
find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true && \  
find /usr/share/doc -empty|xargs rmdir || true && \  
rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* && \  
rm -rf /usr/share/lintian/* /usr/share/linda/* /var/cache/man/*  
  
ENV LANG de_DE.utf8  
  
  
RUN cd /opt && \  
curl http://tomcat.apache.org/download-70.cgi 2>/dev/null | grep ".zip" | head
-n 1 | sed -e 's-<a href=\"--' -e 's-\"--' | awk '{print $1}' | xargs wget &&
\  
unzip apache-tomcat*.zip && \  
rm -f apache-tomcat*.zip && \  
ls -d apache-tomcat* | xargs bash -c 'ln -s $0 tomcat'  
  
RUN rm -rf /opt/tomcat/webapps/* && chmod u+x /opt/tomcat/bin/*.sh  
  
RUN mkdir -p /opt/tomcat/conf/Catalina/localhost  
COPY postgresql-8.4-702.jdbc4.jar /opt/tomcat/lib/  
COPY startTomcat.sh /startTomcat.sh  
# Logging anpassen  
RUN cd /opt/tomcat/conf && mv logging.properties logging.properties.bak  
COPY logging.properties /opt/tomcat/conf/  
  
ADD extraFiles /opt/vera/extraFiles  
  
RUN echo 'LANG=de_DE.UTF-8' > /etc/default/locale  
  
ENTRYPOINT ["/startTomcat.sh"]  
  
CMD ["run"]  


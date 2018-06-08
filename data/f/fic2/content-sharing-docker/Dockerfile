FROM tomcat:7  
RUN rm -rf /usr/local/tomcat/webapps/* \  
&& wget https://www.dropbox.com/s/olk95ij46igbmmk/feedsync.war?dl=1 -O
/usr/local/tomcat/webapps/feedsync.war \  
&& sed -i 's/8080/8083/g' /usr/local/tomcat/conf/server.xml  
  
RUN echo '78984e3cad0d2993b9a0b03b58f2b0a1
/usr/local/tomcat/webapps/feedsync.war' | md5sum -c -  
  
EXPOSE 8083


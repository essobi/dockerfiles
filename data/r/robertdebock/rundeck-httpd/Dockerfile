FROM httpd  
  
COPY rundeck.conf /usr/local/apache2/conf/extra/rundeck.conf  
COPY generate-ssl-certificate.sh /root/generate-ssl-certificate.sh  
COPY httpd-ssl.conf /usr/local/apache2/conf/extra/httpd-ssl.conf  
COPY httptohttps.conf /usr/local/apache2/conf/extra/httptohttps.conf  
  
ENV SERVERNAME rundeck.meinit.nl:443  
ENV SERVERADMIN robert@meinit.nl  
ENV SSL_COUNTRY NL  
ENV SSL_STATE UTRECHT  
ENV SSL_LOCATION Breukelen  
ENV SSL_ORGANIZATION Me in IT Consultancy  
ENV SSL_ORGANIZATIONAL_UNIT IT Department  
ENV SSL_COMMONNAME rundeck.meinit.nl  
  
RUN echo "ServerName localhost" >> /usr/local/apache2/conf/httpd.conf  
RUN echo "Include conf/extra/httpd-ssl.conf" >>
/usr/local/apache2/conf/httpd.conf  
RUN echo "Include conf/extra/rundeck.conf" >>
/usr/local/apache2/conf/httpd.conf  
RUN echo "Include conf/extra/httptohttps.conf" >>
/usr/local/apache2/conf/httpd.conf  
RUN sed -i "s/ServerName .*/ServerName ${SERVERNAME}/"
/usr/local/apache2/conf/extra/httpd-ssl.conf  
RUN sed -i "s/ServerAdmin .*/ServerAdmin ${SERVERADMIN}/"
/usr/local/apache2/conf/extra/httpd-ssl.conf  
RUN apt-get update && \  
apt-get install -y libapache2-mod-proxy-html openssl && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
CMD /bin/sh /root/generate-ssl-certificate.sh && httpd-foreground  


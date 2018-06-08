FROM java:7  
RUN wget -O /usr/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 && chmod +x /usr/bin/confd  
  
ENV RUN_DECK_VERSION 2.6.2-1-GA  
  
RUN wget http://dl.bintray.com/rundeck/rundeck-
deb/rundeck-${RUN_DECK_VERSION}.deb && dpkg -i rundeck-${RUN_DECK_VERSION}.deb
&& rm -f rundeck-${RUN_DECK_VERSION}.deb  
  
ADD entrypoint.sh /entrypoint.sh  
  
ADD conf/* /etc/confd/conf.d/  
ADD templates/* /etc/confd/templates/  
  
CMD ["/entrypoint.sh"]  
  
EXPOSE 4440  
VOLUME /etc/rundeck  
VOLUME /var/rundeck


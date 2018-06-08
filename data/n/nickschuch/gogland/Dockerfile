FROM java:7-jre  
  
ENV GOGLAND_VERSION=171.4694.35  
RUN wget https://download-cf.jetbrains.com/go/gogland-$GOGLAND_VERSION.tar.gz
&& \  
tar -zxf gogland-$GOGLAND_VERSION.tar.gz && \  
mv Gogland-$GOGLAND_VERSION /usr/share/gogland && \  
rm -f gogland-$GOGLAND_VERSION.tar.gz  
  
CMD ["/usr/share/gogland/bin/gogland.sh"]  


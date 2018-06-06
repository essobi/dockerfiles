FROM openjdk:8-jre  
  
RUN wget -q "https://www.crushftp.com/early8/CrushFTP8_PC.zip" -O
/var/opt/CrushFTP.zip \  
&& unzip -q /var/opt/CrushFTP.zip -d /var/opt/ \  
&& rm -rf /var/opt/CrushFTP.zip /tmp/*  
  
WORKDIR /var/opt/CrushFTP8_PC  
  
ADD ./start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  


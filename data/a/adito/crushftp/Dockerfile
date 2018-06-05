FROM anapsix/alpine-java:8_jdk_unlimited  
  
LABEL maintainer "Brian Tkatch, brian@briantkatch.com"  
  
ADD https://www.crushftp.com/early8/CrushFTP8_PC.zip /tmp/CrushFTP8_PC.zip  
ADD ./setup.sh /var/opt/setup.sh  
ADD ./crushftp_init_nobackground.sh /var/opt/run_crushftp.sh  
  
RUN chmod +x /var/opt/setup.sh && \  
chmod +x /var/opt/run_crushftp.sh && \  
unzip /tmp/CrushFTP8_PC.zip -d /var/opt/ && \  
rm /tmp/CrushFTP8_PC.zip && \  
cd /var/opt/CrushFTP8_PC && java -jar /var/opt/CrushFTP8_PC/CrushFTP.jar -a
"fadmin" "admin" && \  
mkdir /config && \  
cp -Rf /var/opt/CrushFTP8_PC/* /config/  
  
ENTRYPOINT /var/opt/setup.sh  
  
# FTP Server  
EXPOSE 21  
# HTTPS Server  
EXPOSE 443  
# FTP PASV transfers  
EXPOSE 2000-2010  
# SSH Server  
EXPOSE 2222  
# HTTP Servers  
EXPOSE 8080 9090


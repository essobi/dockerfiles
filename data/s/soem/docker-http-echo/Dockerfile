FROM ruby:2.3.1  
ENV NC_PORT=80  
RUN curl http://ftp.us.debian.org/debian/pool/main/n/netcat/netcat-
traditional_1.10-41_amd64.deb -o /tmp/netcat-traditional_1.10-41_amd64.deb; \  
dpkg -i /tmp/netcat-traditional_1.10-41_amd64.deb; \  
rm /tmp/netcat-traditional_1.10-41_amd64.deb  
  
COPY http-echo.rb /opt/http-echo.rb  
  
EXPOSE 80  
CMD while :; do nc -e /opt/http-echo.rb -l -p $NC_PORT; done  


FROM ubuntu:16.04  
WORKDIR /tmp  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget xz-utils fontconfig
libfontconfig1 libfreetype6 libjpeg-turbo8 libx11-6 libxext6 libxrender1
xfonts-base xfonts-75dpi && \  
wget -q
http://download.gna.org/wkhtmltopdf/0.12/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \  
mv wkhtmltox/bin/* /usr/bin/ && \  
apt-get purge -y wget xz-utils && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
WORKDIR /  
  
RUN apt-get update && \  
apt-get install -y wget && \  
wget -qO- https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y --no-install-recommends nodejs && \  
npm install -g forever && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
RUN npm install wkhtmltopdf wkhtmltoimage  
  
ADD server.js /opt/server.js  
  
EXPOSE 5001  
ENTRYPOINT ["forever"]  
CMD ["/opt/server.js"]


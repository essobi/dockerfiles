FROM node:9.4.0  
  
RUN apt update && \  
apt install -y wget libxrender1 xfonts-utils xfonts-base xfonts-75dpi
libfontenc1 x11-common xfonts-encodings libxfont1 fontconfig && \  
wget \--quiet
https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz && \  
mkdir -p /opt && \  
tar -xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz -C /opt && \  
rm -rf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \  
ln /opt/wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf && \  
ln /opt/wkhtmltox/bin/wkhtmltoimage /usr/local/bin/wkhtmltoimage && \  
echo "# Clean" && \  
apt-get remove -y wget && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /tmp/*  


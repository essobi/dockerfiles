FROM ubuntu:14.04  
MAINTAINER Timothy Zorn <tim@zornco.com>  
  
RUN sudo apt-get update && sudo apt-get install -y software-properties-common
&& sudo add-apt-repository multiverse && \  
(echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections) && \  
apt-get update && \  
apt-get install -y wget xorg xz-utils fontconfig libxrender1 libxext6 libx11-6
openssl xfonts-base ttf-mscorefonts-installer xfonts-75dpi && \  
wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
tar Jxf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \  
cp -r wkhtmltox/bin/* /usr/local/bin/ && cp -r wkhtmltox/lib/* /usr/lib/ && cp
-r wkhtmltox/include/* /usr/include/  
  
WORKDIR /data  
ENTRYPOINT ["/usr/local/bin/wkhtmltopdf"]  
CMD ["-h"]  


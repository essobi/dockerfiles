FROM ubuntu:16.04  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get -y install
build-essential xorg libssl-dev libxrender-dev wget  
  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz && \  
tar xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz  
  
ADD ./start.sh /start.sh  
  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  


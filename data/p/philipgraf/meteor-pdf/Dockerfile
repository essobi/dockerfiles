FROM meteorhacks/meteord:base  
MAINTAINER Philip Graf <philip.graf@novapo.net>  
  
RUN mkdir -p /dependencies  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libpng12-0 \  
libjpeg8 \  
libxrender1 \  
xfonts-base \  
xfonts-75dpi \  
pdftk \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
wheezy-amd64.deb -o /dependencies/wkhtmltox.deb  
RUN dpkg -i /dependencies/wkhtmltox.deb  


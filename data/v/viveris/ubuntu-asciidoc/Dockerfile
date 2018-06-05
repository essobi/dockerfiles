FROM ubuntu:17.10  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get --yes install build-essential xorg libssl-dev libxrender-dev wget
gdebi && \  
apt-get --yes install asciidoctor && \  
apt-get --yes install pdftk && \  
apt-get --yes install zlib1g-dev libpng-dev libfontconfig1 libx11-dev
xfonts-75dpi && \  
apt-get --yes install git curl && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget
http://security.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.50-1ubuntu2.14.04.2_amd64.deb
&& \  
gdebi --n libpng12-0_1.2.50-1ubuntu2.14.04.2_amd64.deb  
  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb && \  
gdebi --n wkhtmltox-0.12.2.1_linux-trusty-amd64.deb  
  
RUN gem install asciidoctor-pdf --pre && \  
gem install --no-document rake rouge coderay thread_safe slim haml tilt
pygments.rb  
  
CMD ["/bin/bash"]  


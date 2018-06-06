FROM ubuntu:16.04  
MAINTAINER Niko Lehtovirta  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
# Create a default user  
RUN useradd automation --shell /bin/bash --create-home  
  
# Update the repositories  
# Install utilities  
# Install XVFB and TinyWM  
# Install fonts  
# Install Python  
RUN apt-get -yqq update && \  
apt-get -yqq install xvfb tinywm && \  
apt-get -yqq install fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic && \  
apt-get -yqq install supervisor chromium-browser chromium-chromedriver && \  
rm -rf /var/lib/apt/lists/*  
  
# Configure Supervisor  
ADD ./etc/supervisord.conf /etc/  
ADD ./etc/supervisor /etc/supervisor  
  
# Default configuration  
ENV DISPLAY :20.0  
ENV SCREEN_GEOMETRY "1440x900x24"  
ENV CHROMEDRIVER_PORT 9515  
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"  
ENV CHROMEDRIVER_URL_BASE ''  
EXPOSE 9515  
VOLUME [ "/var/log/supervisor" ]  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  


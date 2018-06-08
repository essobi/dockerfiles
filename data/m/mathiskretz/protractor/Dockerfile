FROM debian:testing  
  
MAINTAINER mathis.kretz@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# ffmpeg is hosted at deb-multimedia.org  
RUN curl http://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-
multimedia-keyring_2016.8.1_all.deb \  
-o /tmp/deb-multimedia-keyring_2015.6.1_all.deb && \  
dpkg -i /tmp/deb-multimedia-keyring_2015.6.1_all.deb && \  
rm /tmp/deb-multimedia-keyring_2015.6.1_all.deb && \  
echo "deb http://www.deb-multimedia.org stretch main non-free" >>
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
openjdk-8-jre \  
xvfb \  
libgconf-2-4 \  
libexif12 \  
chromium \  
supervisor \  
netcat-traditional \  
curl \  
ffmpeg \  
gnupg && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && \  
apt-get install -y nodejs && \  
rm -rf /var/lib/apt/lists/*  
  
#RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g protractor@4.0.x  
  
# Install Selenium and Chrome driver  
RUN webdriver-manager update  
  
# Add main configuration file  
ADD supervisord.conf /etc/supervisor/supervisor.conf  
  
# Add service defintions for Xvfb, Selenium and Protractor runner  
ADD supervisord/*.conf /etc/supervisor/conf.d/  
  
# Container's entry point, executing supervisord in the foreground  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisor.conf"]  


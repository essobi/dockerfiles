FROM debian:sid  
  
MAINTAINER rafal.krzewski@caltha.pl  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
supervisor \  
netcat-traditional \  
xvfb \  
openjdk-8-jre \  
chromium \  
firefox \  
ffmpeg \  
curl \  
gnupg \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get update && \  
apt-get install -y nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Protractor and initialized Webdriver  
RUN npm install -g protractor@5.3 && \  
webdriver-manager update  
  
# Add a non-privileged user for running Protrator  
RUN adduser --home /project --uid 1000 \  
\--disabled-login --disabled-password --gecos node node  
  
# Add main configuration file  
ADD supervisord.conf /etc/supervisor/supervisor.conf  
  
# Add service defintions for Xvfb, Selenium and Protractor runner  
ADD supervisord/*.conf /etc/supervisor/conf.d/  
  
# By default, tests in /data directory will be executed once and then the
container  
# will quit. When MANUAL envorinment variable is set when starting the
container,  
# tests will NOT be executed and Xvfb and Selenium will keep running.  
ADD bin/run-protractor /usr/local/bin/run-protractor  
  
# Container's entry point, executing supervisord in the foreground  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisor.conf"]  
  
# Protractor test project needs to be mounted at /project  


# Dockerfile for Base container  
# Details:  
# - Debian 8 x64  
# - English only  
# - Assuming Europe/London timezone  
##  
# Pull from Debian 8.4 base image  
FROM debian:8.4  
# Maintainer  
MAINTAINER Cam Logie <mail+dockermaint@userze.ro>  
  
# Add in dpkg config to stop docs being installed  
# Only use English language in locales  
COPY 01_nodoc 02_nolocales /etc/dpkg/dpkg.cfg.d/  
# Set build-time args here  
ARG TERM=linux  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN echo "Starting base image build"\  
# Security updates are good  
&& apt-get update\  
&& apt-get -y upgrade\  
# Some core tools that we need  
&& apt-get install -y wget curl\  
# Remove unnecessary orphaned packages  
&& apt-get autoremove -y\  
# Sloppin-out time. Save space used by apt repo package lists and logs  
&& rm -rf /var/lib/apt/lists/*\  
&& rm -rf /var/log/*\  
# Remove the documentation and manpages  
&& find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true\  
&& find /usr/share/doc -empty|xargs rmdir || true\  
&& rm -rf /usr/share/man /usr/share/groff /usr/share/info /usr/share/lintian
/usr/share/linda /var/cache/man\  
# Remove non-english locales  
&& find /usr/share/locale -mindepth 1 -maxdepth 1 ! -name 'en' | xargs rm -r\  
# Set timezone to London  
&& echo "Europe/London" | tee /etc/timezone\  
&& dpkg-reconfigure tzdata\  


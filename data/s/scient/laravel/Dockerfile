# Build image  
FROM php:7.1.1  
# Maintainer  
MAINTAINER Ivo Krooswijk "ivo@krooswijk.com"  
# For debugging  
# ENV TERM xterm  
# Install system packages  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# Install system packages  
RUN apt-get update && \  
apt-get install -y \  
jq \  
bc \  
unzip \  
git-core \  
build-essential \  
nodejs  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Add phing channel  
RUN pear channel-discover pear.phing.info  
  
# Add phpseclib channel  
RUN pear channel-discover phpseclib.sourceforge.net  
  
# Install dependencies  
RUN pear install phing/phing HTTP_Request2 phpseclib/Net_SFTP  


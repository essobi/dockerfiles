FROM debian:jessie  
MAINTAINER drupal-docker <info@drupaldocker.org>  
  
ENV PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
chrpath \  
libssl-dev \  
libxft-dev \  
libfreetype6 \  
libfreetype6-dev \  
libfontconfig1 \  
libfontconfig1-dev \  
curl \  
&& rm -r /var/lib/apt/lists/* \  
&& curl -LO
https://github.com/Medium/phantomjs/releases/download/v2.1.1/${PHANTOM_JS}.tar.bz2
\  
&& tar -xvjf ${PHANTOM_JS}.tar.bz2 \  
&& mv $PHANTOM_JS /usr/local/share \  
&& ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin  
  
EXPOSE 8643  
CMD ["phantomjs", "--webdriver=8643"]  


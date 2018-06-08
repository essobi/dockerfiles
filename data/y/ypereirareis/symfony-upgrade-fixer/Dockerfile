FROM php:7-cli  
  
MAINTAINER Yannick PEREIRA-REIS <yannick.pereira.reis@gmail.com>  
  
ENV HOME /root  
WORKDIR /app  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nano \  
git \  
curl \  
wget \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& apt-get purge -y --auto-remove  
  
RUN wget https://github.com/umpirsky/Symfony-Upgrade-
Fixer/releases/download/v0.1.6/symfony-upgrade-fixer.phar -O
/usr/local/bin/symfony-upgrade-fixer \  
&& chmod a+x /usr/local/bin/symfony-upgrade-fixer  
  
ENTRYPOINT ["symfony-upgrade-fixer", "--ansi"]  
  


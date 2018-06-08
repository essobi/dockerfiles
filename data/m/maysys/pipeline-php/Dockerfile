FROM php:7  
MAINTAINER Jean-Marc Lagace <jmlagace@maysys.com>  
  
ENV BUILD_TOOL_URL
https://gist.githubusercontent.com/jmlagace/3206fbfdb8b09fe0876c53280ffe2459/raw  
# we need git for the auto commit script  
RUN apt-get update && apt-get install -y git-core \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sSL $BUILD_TOOL_URL/autotag1.sh?`date +%s` >
/usr/local/bin/autotag1.sh \  
&& curl -sSL $BUILD_TOOL_URL/php-check.sh?`date +%s` > /usr/local/bin/php-
check.sh \  
&& chmod +x /usr/local/bin/*  


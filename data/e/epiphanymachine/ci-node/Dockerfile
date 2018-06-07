FROM node:boron  
MAINTAINER EpiphanyMachine@gmail.com  
  
# Install Chromium  
RUN set -xe \  
&& curl -SL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable \  
&& rm -rf /var/lib/apt/lists/*  
# Install the aptible toolbelt
https://www.aptible.com/support/toolbelt/#download-ubuntu  
RUN set -xe \  
&& curl -o aptible-cli.deb https://omnibus-aptible-
toolbelt.s3.amazonaws.com/aptible/omnibus-aptible-
toolbelt/master/132/pkg/aptible-
toolbelt_0.8.4%2B20170125114552%7Eubuntu.16.04-1_amd64.deb \  
&& dpkg -i aptible-cli.deb \  
&& apt-get install -f \  
&& rm aptible-cli.deb  
  
# Install heroku client  
RUN set -xe \  
&& curl -O https://cli-assets.heroku.com/branches/stable/heroku-linux-
amd64.tar.gz \  
&& mkdir -p /usr/local/lib /usr/local/bin \  
&& tar -xvzf heroku-linux-amd64.tar.gz -C /usr/local/lib \  
&& ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku  
# Define working directory.  
WORKDIR /data  


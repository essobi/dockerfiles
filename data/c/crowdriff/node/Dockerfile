# Version 1.2  
FROM crowdriff/redis  
  
MAINTAINER Abhinav Ajgaonkar <abhi@crowdriff.com>  
  
# Install Python, git & node  
RUN \  
apt-get update; \  
apt-get install -y -qq python git; \  
wget -O - http://nodejs.org/dist/v0.10.38/node-v0.10.38-linux-x64.tar.gz | tar
xzf - --strip-components=1 --exclude="README.md" \--exclude="LICENSE"
\--exclude="ChangeLog" -C "/usr/local"; \  
npm install -g npm; \  
npm install --silent --quiet -g grunt-cli bower forever;  
  
WORKDIR /src;  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  


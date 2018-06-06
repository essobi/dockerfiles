FROM phusion/baseimage:0.9.16  
MAINTAINER peter@codebuffet.co  
  
EXPOSE 3001 6001  
RUN apt-get update  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get update  
RUN apt-get -y install nodejs supervisor imagemagick sendmail build-essential
unzip wget  
RUN cd /opt \  
&& wget https://github.com/Countly/countly-
server/releases/download/16.06/countly-community-edition-v16.06.zip \  
&& unzip countly-community-edition-v16.06.zip \  
&& rm countly-community-edition-v16.06.zip  
  
RUN cd /opt/countly/api \  
&& sudo npm install time  
  
#install grunt & npm modules  
RUN cd /opt/countly \  
&& npm install -g grunt-cli --unsafe-perm; npm install  
  
COPY config/api.js /opt/countly/api/config.js  
COPY config/frontend.js /opt/countly/frontend/express/config.js  
COPY config/javascripts.js
/opt/countly/frontend/express/public/javascripts/countly/countly.config.js  
  
# Move to baseimage run system  
ADD /scripts/countly-api.sh /etc/service/countly-api/run  
ADD /scripts/countly-dashboard.sh /etc/service/countly-dashboard/run  
  
#Install user  
RUN useradd -r -M -U -d /opt/countly -s /bin/false countly && \  
echo "countly ALL=(ALL) NOPASSWD: /usr/bin/sv restart countly-api countly-
dashboard" > /etc/sudoers.d/countly  
  
# Install plugins  
RUN cp /opt/countly/plugins/plugins.default.json
/opt/countly/plugins/plugins.json  
  
RUN bash /opt/countly/bin/scripts/countly.install.plugins.sh  
  
# Compile assets  
RUN cd /opt/countly; grunt dist-all  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  


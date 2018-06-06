FROM doalitic/cypress-base:8  
  
LABEL maintainer="Moss team <devops@moss.sh>"  
  
USER root  
  
# install Chrome  
RUN \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list \  
&& apt-get update \  
&& apt-get install -y dbus-x11 google-chrome-stable \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# "fake" dbus address to prevent errors  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  


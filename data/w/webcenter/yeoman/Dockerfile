FROM webcenter/nodejs:0.12.7  
MAINTAINER Sebastien Langoureaux <linuxworkgroup@hotmail.com>  
  
USER root  
  
# Install git and xfce-terminal and chrome  
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
&& \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list && \  
apt-get update && \  
apt-get install xfce4-terminal git google-chrome-beta unzip -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Install yeoman  
RUN npm install -g yo bower grunt-cli gulp  
  
# Install generator for angular and angular-fullstack  
RUN npm install -g generator-angular  
RUN npm install -g generator-angular-fullstack  
  
USER dev  
  
WORKDIR /app  
  
EXPOSE 9000  
# Workspace to run git and yeoman command line  
VOLUME ["/app"]  
  
# User home directory to store git setting  
VOLUME ["/home/dev"]  
  
CMD ["xfce4-terminal", "--command", "'/bin/bash'", "--title", "'Yeoman
Shell'"]  


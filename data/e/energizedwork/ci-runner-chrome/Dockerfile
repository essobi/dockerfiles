FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
git \  
openjdk-8-jdk \  
xvfb \  
libgtk-3-dev \  
wget \  
ttf-freefont  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
  
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" >> /etc/apt/sources.list.d/google-chrome.list'  
  
RUN apt-get update && apt-get install -y \  
google-chrome-stable  
  
COPY google-chrome.sh /usr/bin/google-chrome  
  
RUN chmod +x /usr/bin/google-chrome  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
CMD ["/bin/bash"]  


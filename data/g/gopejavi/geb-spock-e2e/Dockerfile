FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
git \  
openjdk-8-jdk \  
xvfb \  
curl \  
bzip2 \  
libgtk-3-dev \  
wget \  
mariadb-client-core-10.0  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
  
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" >> /etc/apt/sources.list.d/google-chrome.list'  
  
RUN apt-get update && apt-get install -y \  
google-chrome-stable  
  
RUN mkdir -p /opt/firefox/56.0.1  
RUN curl -SL
https://ftp.mozilla.org/pub/firefox/releases/56.0.1/linux-x86_64/en-
US/firefox-56.0.1.tar.bz2 \  
| tar -xjC /opt/firefox/56.0.1  
  
COPY firefox.sh /usr/bin/firefox  
  
RUN chmod +x /usr/bin/firefox  
  
COPY google-chrome.sh /usr/bin/google-chrome  
  
RUN chmod +x /usr/bin/google-chrome  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
CMD ["/bin/bash"]  


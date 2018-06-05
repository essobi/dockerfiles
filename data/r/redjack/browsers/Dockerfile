FROM redjack/node  
MAINTAINER RedJack, LLC  
  
ENV PATH /usr/local/bin:$PATH  
  
# Install Xvfb, VNC, fonts, Firefox and Chrome  
RUN curl -f -s https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
x11vnc \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable \  
xvfb \  
firefox \  
google-chrome-stable \  
&& rm -rf /var/lib/apt/lists/*  
  
# Chrome remote debugger port  
EXPOSE 9222:9222  
# VNC  
EXPOSE 5900:5900  
# Selenium  
EXPOSE 4444:4444  
ENTRYPOINT ["/usr/bin/xvfb-run", "-e", "xvfberr.log", "-a"]  
CMD []  


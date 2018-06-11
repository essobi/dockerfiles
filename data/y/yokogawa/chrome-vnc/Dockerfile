FROM debian:sid  
  
RUN echo 'deb http://httpredir.debian.org/debian testing main' >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
ca-certificates \  
curl \  
gnupg \  
x11vnc \  
xvfb \  
supervisor \  
fonts-takao \  
fonts-symbola \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add
\- \  
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
google-chrome-stable \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV START_PAGE https://www.google.co.jp/  
COPY supervisord.conf /supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/supervisord.conf"]  


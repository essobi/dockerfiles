FROM debian:stretch  
  
MAINTAINER furiousgeorge <furiousgeorgecode@gmail.com>  
  
ENV LANG C.UTF-8  
ENV BUILD_LIST git gnupg2  
ENV INSTALL_LIST wget python3 curl  
ENV BROWSER_LIST google-chrome-beta  
  
RUN apt-get update \  
&& apt-get install -qy $INSTALL_LIST $BUILD_LIST \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google-chrome.list'  
  
RUN apt-get update \  
&& apt-get install -qy $BROWSER_LIST \  
&& git clone https://github.com/pirate/bookmark-archiver /app \  
&& apt-get purge -y $BUILD_LIST \  
&& apt-get autoremove --purge -y && apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /app  
  
ENTRYPOINT ["/app/archive.py"]  


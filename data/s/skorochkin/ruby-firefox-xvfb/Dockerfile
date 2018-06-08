FROM ruby:2  
# set env variables  
ENV DISPLAY=":99.0" \  
FF_VERSION="42.0"  
# install libs, xvfb and firefox  
RUN apt-get update && apt-get install -y zlib1g-dev xvfb libxcomposite1
libasound2 libdbus-glib-1-2 libgtk2.0-0  
RUN wget "https://download-
installer.cdn.mozilla.net/pub/firefox/releases/${FF_VERSION}/linux-x86_64/en-
US/firefox-${FF_VERSION}.tar.bz2" \  
-O /tmp/firefox.tar.bz2 && \  
tar xvf /tmp/firefox.tar.bz2 -C /opt && \  
ln -s /opt/firefox/firefox /usr/bin/firefox  
  
# install xvfb init script  
COPY xvfb-run /usr/local/bin/  
RUN chmod +x /usr/local/bin/xvfb-run  
  
# cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/usr/local/bin/xvfb-run"]  
CMD []  


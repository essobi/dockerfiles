FROM lynxtp/openjdk-jdk:8  
MAINTAINER "Tom Vaughan <tvaughan@lynxtp.com>"  
ENV PATH /opt/phantomjs/bin:$PATH  
  
RUN curl -sL -o /tmp/phantomjs.tar.xz http://build-dependencies.s3-website-us-
east-1.amazonaws.com/phantomjs-2.1.1-linux-x86_64.tar.xz \  
&& mkdir -p /opt/phantomjs \  
&& tar --strip-components=1 -C /opt/phantomjs -xf /tmp/phantomjs.tar.xz \  
&& rm -f /tmp/phantomjs.tar.xz  
  
RUN curl -sL -o /usr/local/bin/lein
https://raw.githubusercontent.com/technomancy/leiningen/2.6.1/bin/lein \  
&& chmod a+x /usr/local/bin/lein  
  
ENV LEIN_HOME /srv/lein  
ENV LEIN_ROOT 1  
ENV LEIN_REPL_HOST 0.0.0.0  
ENV LEIN_REPL_PORT 5309  
EXPOSE $LEIN_REPL_PORT  
  
CMD ["lein"]  


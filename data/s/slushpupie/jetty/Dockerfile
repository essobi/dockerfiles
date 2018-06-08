FROM openjdk:8-jre  
  
ENV JETTY_HOME /usr/local/jetty  
ENV PATH $JETTY_HOME/bin:$PATH  
RUN mkdir -p "$JETTY_HOME"  
WORKDIR $JETTY_HOME  
  
# see http://dev.eclipse.org/mhonarc/lists/jetty-users/msg05220.html  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \  
0x61c3351a438a3b7d  
  
ENV JETTY_MAJOR 7  
ENV JETTY_VERSION 7.6.21.v20160908  
ENV JETTY_TGZ_URL http://central.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/$JETTY_VERSION/jetty-distribution-$JETTY_VERSION.tar.gz  
  
RUN curl -SL "$JETTY_TGZ_URL" -o jetty.tar.gz \  
&& curl -SL "$JETTY_TGZ_URL.asc" -o jetty.tar.gz.asc \  
&& gpg --verify jetty.tar.gz.asc \  
&& tar -xvf jetty.tar.gz --strip-components=1 \  
&& sed -i '/jetty-logging/d' etc/jetty.conf \  
&& rm -fr javadoc \  
&& rm jetty.tar.gz*  
  
EXPOSE 8080  
CMD ["jetty.sh", "run"]  


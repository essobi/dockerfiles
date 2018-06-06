FROM jeanblanchard/busybox-java  
  
# Logstash version  
ENV VERSION 1.5.0  
ENV LOGSTASH_HOME /opt/logstash  
ENV GEM_PATH "$LOGSTASH_HOME/vendor/bundle/jruby/1.9"  
RUN opkg-install bash  
  
RUN curl
"http://download.elastic.co/logstash/logstash/logstash-$VERSION.tar.gz" \  
| gunzip -c - | tar -xf - -C /opt && \  
mv "/opt/logstash-$VERSION" "$LOGSTASH_HOME" && \  
mkdir "$LOGSTASH_HOME/conf.d" && \  
mkdir -p /usr/local/bin  
  
ENV PATH "$PATH:$LOGSTASH_HOME/vendor/jruby/bin"  
# Prerequisites for the logstash-webhdfs plugin  
RUN echo "gem \"webhdfs\"" >> "$LOGSTASH_HOME/Gemfile"  
RUN gem install -i "$GEM_PATH" webhdfs  
  
COPY conf.d/* "$LOGSTASH_HOME/conf.d/"  
COPY plugins/* "$GEM_PATH/gems/logstash-core-$VERSION-
java/lib/logstash/outputs/"  
COPY start.sh /usr/local/bin/  
  
VOLUME /docker  
  
ENTRYPOINT ["/usr/local/bin/start.sh"]  
  
CMD ["logstash"]  


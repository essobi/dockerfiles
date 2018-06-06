FROM logstash:latest  
  
CMD ["logstash", "-f", "/etc/logstash.conf"]  
  
ADD logstash.conf /etc/  
  
# Make logstash's local jruby available system-wide  
ENV PATH=/opt/logstash/vendor/jruby/bin:$PATH  
# Create a symlink so calling ruby will invoke jruby  
RUN ln -s /opt/logstash/vendor/jruby/bin/jruby
/opt/logstash/vendor/jruby/bin/ruby  
  
ENV INTERNODE_VERSION 1.1.0  
RUN gem install bundler internode:$INTERNODE_VERSION  


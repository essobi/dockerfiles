FROM alpine:3.5  
RUN apk add --update ruby ruby-json ca-certificates wget  
RUN gem install --no-rdoc --no-ri stomp  
  
RUN wget -q https://github.com/puppetlabs/marionette-
collective/archive/2.9.1.tar.gz \  
-O mcollective.tar.gz  
RUN tar xf mcollective.tar.gz  
RUN mv /marionette-collective-2.9.1 mcollective  
  
RUN mkdir -p /etc/mcollective  
RUN mkdir -p /usr/share/mcollective/plugins  
  
RUN cp /mcollective/etc/facts.yaml.dist /etc/mcollective/facts.yaml  
RUN cp /mcollective/etc/*.erb /etc/mcollective  
  
RUN cp /mcollective/etc/server.cfg.dist /etc/mcollective/server.cfg  
RUN cp /mcollective/etc/client.cfg.dist /etc/mcollective/client.cfg  
RUN sed -i 's/^libdir *= *.*$/libdir = \/usr\/lib\/ruby\/vendor_ruby/g'
/etc/mcollective/*.cfg  
  
RUN cp -r /mcollective/lib/* /usr/lib/ruby/vendor_ruby  
  
RUN cp /mcollective/bin/mcollectived /usr/sbin/  
RUN cp /mcollective/bin/mco /usr/bin/  
  
RUN rm mcollective.tar.gz  
RUN rm -rf mcollective  
RUN rm -rf var/cache/apk/*  
  
ENTRYPOINT ["mcollectived", "--no-daemonize"]  
  


FROM tomasbasham/node:6.11.0  
LABEL com.tomasbasham.maintainer "Tomas Basham <me@tomasbasham.co.uk>" \  
com.tomasbasham.version "2.13.2" \  
com.tomasbasham.description "Ember Command Line Interface"  
  
ENV VERSION 2.13.2  
ENV BOWER_VERSION 1.8.0  
ENV PHANTOM_VERSION 2.1.14  
# Install ember, bower and phantomjs  
RUN npm install -g \  
ember-cli@${VERSION} \  
bower@${BOWER_VERSION} \  
phantomjs-prebuilt@${PHANTOM_VERSION}  
  
ENTRYPOINT ["/usr/bin/ember"]  
CMD ["help"]  


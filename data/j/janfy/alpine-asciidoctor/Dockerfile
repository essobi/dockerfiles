FROM alpine:3.7  
  
ENV LIBRARY_PATH=/lib:/usr/lib  
RUN apk add --update --no-cache \  
gcc \  
g++ \  
make \  
ruby-dev \  
ruby \  
asciidoctor \  
python && \  
gem install --no-ri --no-rdoc asciidoctor-pdf --pre && \  
gem install --no-ri --no-rdoc coderay pygments.rb && \  
gem cleanup && \  
apk del \  
gcc \  
g++ \  
make \  
ruby-dev && \  
rm -rf /tmp/* /var/cache/apk/* ~/.cache/pip  
  
WORKDIR /documents  
VOLUME /documents  
  
CMD ["/bin/sh"]  


FROM alpine:3.4  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV ASCIIDOCTOR_VERSION "1.5.5"  
ENV ASCIIDOCTOR_PDF_VERSION "1.5.0.alpha.15"  
  
RUN apk add --update --no-cache \  
build-base \  
curl \  
gcc \  
g++ \  
libxslt-dev \  
libxml2-dev \  
make \  
openjdk8-jre \  
ruby-dev \  
ruby \  
ruby-json \  
ttf-dejavu \  
zip && \  
gem install --no-ri --no-rdoc nokogiri \  
\-- --use-system-libraries \  
\--with-xml2-config=/usr/bin/xml2-config \  
\--with-xslt-config=/usr/bin/xslt-config && \  
gem install --no-ri --no-rdoc asciidoctor --version $ASCIIDOCTOR_VERSION && \  
gem install --no-ri --no-rdoc asciidoctor-diagram && \  
gem install --no-ri --no-rdoc asciidoctor-pdf --version
$ASCIIDOCTOR_PDF_VERSION && \  
gem install --no-ri --no-rdoc asciidoctor-epub3 --pre && \  
gem install --no-ri --no-rdoc asciidoctor-confluence && \  
gem install --no-ri --no-rdoc coderay && \  
gem cleanup && \  
apk del build-base gcc g++ make ruby-dev && \  
rm -rf /tmp/* /var/cache/apk/*  
  
WORKDIR /documents  
VOLUME /documents  
  
CMD ["/bin/sh"]  


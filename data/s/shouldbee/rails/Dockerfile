FROM ruby:2.3.0-alpine  
  
ENV BUILD_PACKAGES="build-base" \  
DEV_PACKAGES="libxml2-dev libxslt-dev sqlite-dev postgresql-dev tzdata nodejs"
\  
GEMS="nokogiri sqlite3 debug_inspector binding_of_caller byebug pg puma" \  
RUBY_VERSION="2.3.0"  
# preinstall native extensions  
RUN set -x \  
&& apk --update --upgrade add $BUILD_PACKAGES $DEV_PACKAGES \  
&& gem install $GEMS \  
\-- --use-system-libraries \  
\--with-xml2-config=/usr/bin/xml2-config \  
\--with-xslt-config=/usr/bin/xslt-config \  
&& apk del $BUILD_PACKAGES \  
&& find / -type f -iname \\*.apk-new -delete \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /usr/local/bundle/cache/*.gem \  
&& rm -rf /usr/local/lib/ruby/gems/$RUBY_VERSION/cache/*.gem \  
&& rm -rf ~/.gem  
  
# support Japanese input in Rails Console  
ENV LANG C.UTF-8  
# rails default port  
EXPOSE 3000  
  
WORKDIR /app  


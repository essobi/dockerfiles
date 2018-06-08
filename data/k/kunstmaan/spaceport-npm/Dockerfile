FROM mkenney/npm:node-8-alpine  
  
COPY buildgulp /usr/local/bin/buildgulp  
COPY buildui /usr/local/bin/buildui  
COPY stack-fix.c /lib/stack-fix.c  
  
RUN apk update && apk upgrade && apk --update add \  
ruby ruby-irb ruby-rake ruby-io-console ruby-bigdecimal ruby-json ruby-dev
ruby-bundler \  
libstdc++ tzdata bash ca-certificates automake git alpine-sdk nasm autoconf
build-base \  
zlib zlib-dev libpng libpng-dev libwebp libwebp-dev libjpeg-turbo libjpeg-
turbo-dev \  
&& rm -rf /var/cache/apk/* \  
&& echo 'gem: --no-document' > /etc/gemrc  
  
RUN gem install bundler && chmod +x /usr/local/bin/buildgulp && chmod +x
/usr/local/bin/buildui  
RUN gcc -shared -fPIC /lib/stack-fix.c -o /lib/stack-fix.so  
  
ENV LD_PRELOAD /lib/stack-fix.so  
  
CMD ["tail -f /dev/null"]  


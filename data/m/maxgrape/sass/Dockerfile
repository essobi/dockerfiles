FROM alpine:3.6  
  
ENV SASS_VERSION 3.5.5  
  
RUN apk add --no-cache ruby \  
&& apk --no-cache --virtual .build-deps add curl \  
&& curl -fSL https://github.com/sass/sass/archive/$SASS_VERSION.tar.gz -o
sass.tar.gz \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f sass.tar.gz \  
&& rm sass.tar.gz \  
&& ln -s /usr/src/sass-$SASS_VERSION/bin/sass /usr/bin/sass \  
&& apk del .build-deps  
  
CMD sass -v  


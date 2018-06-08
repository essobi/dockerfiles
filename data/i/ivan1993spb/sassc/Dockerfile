FROM alpine:latest  
  
ARG SASSC_VERSION="3.5.0"  
ARG LIBSASS_VERSION="3.5.0"  
ENV SASS_LIBSASS_PATH /libsass-${LIBSASS_VERSION}  
  
RUN apk add --no-cache --virtual .fetch-deps curl build-base ca-certificates \  
&& curl -L https://github.com/sass/sassc/archive/${SASSC_VERSION}.tar.gz | tar
-xz \  
&& curl -L https://github.com/sass/libsass/archive/${LIBSASS_VERSION}.tar.gz |
tar -xz \  
&& echo $SASSC_VERSION > sassc-${SASSC_VERSION}/VERSION \  
&& echo $LIBSASS_VERSION > libsass-${LIBSASS_VERSION}/VERSION \  
&& make -C sassc-${SASSC_VERSION} -j4 \  
&& apk del .fetch-deps \  
&& apk add --no-cache libstdc++ \  
&& rm -fr /var/cache/apk/* \  
&& cp sassc-${SASSC_VERSION}/bin/sassc /sassc \  
&& rm -fr sassc-${SASSC_VERSION} libsass-${LIBSASS_VERSION}  
  
ENTRYPOINT ["/sassc"]  
  


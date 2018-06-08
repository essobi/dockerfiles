FROM alpine:3.7  
# FROM quadric/alpine:3.7  
LABEL net.quadric.vendor="Quadric ApS" maintainer="Ahmed Magdy
<ahmed.magdy@quadric.net>"  
  
ENV BUILD_DEPS="gettext" \  
RUNTIME_DEPS="libintl"  
RUN apk add --update $RUNTIME_DEPS && \  
apk add --virtual build_deps $BUILD_DEPS && \  
cp /usr/bin/envsubst /usr/local/bin/envsubst && \  
apk del build_deps  
  
# apk add --update build-base && \  
# apk add --no-cache bash && \  
COPY ./entrypoint.sh /usr/bin/entrypoint.sh  
  
ENTRYPOINT [ "entrypoint.sh" ]


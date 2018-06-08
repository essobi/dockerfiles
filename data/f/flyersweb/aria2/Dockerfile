FROM alpine:3.7  
MAINTAINER Flyers <contact@flyers-web.org>  
  
ENV ARIA2_VERSION=1.33.1  
RUN set -x \  
  
# Prepare system  
  
&& resolve() { echo $(apk search $1 | grep "^$1-$2" | sed -e "s/$1-//g") ; } \  
  
&& apk add -U \  
  
# Install packages  
  
&& RESOLVED_ARIA2_VERSION=$(resolve aria2 $ARIA2_VERSION) \  
  
&& apk add \  
aria2=${RESOLVED_ARIA2_VERSION:?"Impossible to find 'aria2' in version
'$ARIA2_VERSION'"} \  
ca-certificates \  
  
&& apk add \--update bash \  
  
# Clean  
  
&& rm -rf \  
/var/cache/apk/* \  
  
&& mkdir -p /data \  
&& mkdir -p /dataComplete  
  
COPY aria2.conf /etc/aria2/aria2.conf  
COPY oncomplete.sh /  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
EXPOSE 6800  
CMD [ "aria2" ]  


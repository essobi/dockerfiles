FROM alpine:3.3  
MAINTAINER Jonas Zhou <zjqzero@gmail.com>  
  
ENV \  
ARIA2_VERSION=1.19.3  
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
  
# Clean  
  
&& rm -rf \  
/var/cache/apk/*  
  
RUN touch /var/run/aria2.session  
  
ADD aria2.conf /etc/aria2.conf  
  
EXPOSE 6800  
ENTRYPOINT [ "/usr/bin/aria2c", "--conf-path=/etc/aria2.conf" ]


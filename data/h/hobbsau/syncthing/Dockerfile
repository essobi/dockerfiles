FROM alpine:edge  
MAINTAINER Adrian Hobbs <adrianhobbs@gmail.com>  
ENV PACKAGE="syncthing tzdata" \  
USER="syncthing" \  
UID="1000" \  
GROUP="syncthing" \  
GID="1000" \  
HOME="/var/lib/syncthing" \  
TZ="Australia/Sydney"  
# Install package using --no-cache to update index and remove unwanted files  
RUN apk add --no-cache $PACKAGE && \  
cp /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo "$TZ" > /etc/timezone && \  
deluser $USER && \  
addgroup -g $GID $GROUP && \  
adduser -D -H -h $HOME -s /sbin/nologin -G $GROUP -g ' ' -u $UID $USER  
  
USER $USER  
CMD ["/usr/bin/syncthing","-home=/var/lib/syncthing"]  
  


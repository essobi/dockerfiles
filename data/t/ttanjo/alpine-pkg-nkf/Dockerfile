FROM alpine:latest  
  
LABEL maintainer="Tomoya Tanjo <ttanjo@gmail.com>"  
  
ENV REPODEST /packages  
ENV LOGINUSER builder  
  
RUN apk add --no-cache alpine-sdk && \  
adduser -D $LOGINUSER && \  
addgroup $LOGINUSER abuild && \  
echo "$LOGINUSER ALL=(ALL) ALL" >> /etc/sudoers && \  
mkdir -p /var/cache/distfiles && \  
chgrp abuild /var/cache/distfiles && \  
chmod g+w /var/cache/distfiles  
  
USER $LOGINUSER  
WORKDIR /home/$LOGINUSER  
  
RUN mkdir nkf  
WORKDIR nkf  
COPY APKBUILD /home/$LOGINUSER/nkf  
  
COPY start.sh /  
ENTRYPOINT ["/start.sh"]  


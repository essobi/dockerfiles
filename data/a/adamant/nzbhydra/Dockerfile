FROM alpine:3.6  
MAINTAINER Adam Dodman <adam.dodman@gmx.com>  
  
ENV UID=907 UNAME=hydra GID=900 GNAME=media  
  
RUN addgroup -g $GID $GNAME \  
&& adduser -SH -u $UID -G $GNAME -s /usr/sbin/nologin $UNAME \  
&& apk add --no-cache git python \  
&& mkdir /hydra && git clone \--depth 1 https://github.com/theotherp/nzbhydra
/hydra \  
&& chown $UID:$GID -R /hydra \  
&& apk del --no-cache git  
  
USER $UNAME  
  
VOLUME ["/config"]  
EXPOSE 8081  
CMD [ "/usr/bin/python", "/hydra/nzbhydra.py", "--nobrowser", "--
config","/config/settings.cfg", "--database","/config/nzbhydra.db" ]  


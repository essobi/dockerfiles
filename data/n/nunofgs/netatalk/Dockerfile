FROM alpine:3.4  
ENV NETATALK_VERSION 3.1.8  
RUN apk add --no-cache acl-dev build-base cracklib-dev db-dev krb5-dev
libevent-dev tdb-dev \  
&& wget -O-
http://ufpr.dl.sourceforge.net/project/netatalk/netatalk/$NETATALK_VERSION/netatalk-$NETATALK_VERSION.tar.gz
| tar -zx \  
&& cd netatalk-$NETATALK_VERSION \  
&& ./configure --enable-debug --enable-krbV-uam --with-cracklib \  
&& make \  
&& make install \  
&& apk del build-base \  
&& cd .. \  
&& rm -rf netatalk-$NETATALK_VERSION  
  
COPY afpd.conf /etc/netatalk/afpd.conf  
  
VOLUME /data  
  
EXPOSE 548  
CMD ["netatalk", "-d", "-F", "/etc/netatalk/afpd.conf"]  


FROM alpine:3.3  
ENV UNISON_VERSION=2.48.3  
RUN apk add --update alpine-sdk inotify-tools-dev && \  
apk add ocaml --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \  
curl -O
http://www.seas.upenn.edu/~bcpierce/unison//download/releases/unison-$UNISON_VERSION/unison-$UNISON_VERSION.tar.gz
&& \  
tar xzf unison-$UNISON_VERSION.tar.gz && \  
cd unison-$UNISON_VERSION && \  
make GLIBC_SUPPORT_INOTIFY=true UISTYLE=text INSTALLDIR=/bin NATIVE=true
STATIC=true install && \  
apk del ocaml inotify-tools-dev alpine-sdk && \  
rm -rf /unison-$UNISON_VERSION.tar.gz /unison-$UNISON_VERSION /binunison*
/var/cache/apk/* && \  
mkdir /unison  
  
ADD run.sh /run.sh  
  
ENV UNISON_DIR=/unison  
EXPOSE 5000  
ENTRYPOINT ["/run.sh"]  
CMD ["unison", "-socket", "5000"]  


FROM pipill/armhf-alpine-glibc  
  
ENV RESILIO_VERSION=2.5.2  
ENV RESILIO_URL=https://download-cdn.resilio.com/${RESILIO_VERSION}/linux-
armhf/resilio-sync_armhf.tar.gz  
  
RUN [ "cross-build-start" ]  
  
RUN apk --no-cache --update add bash \  
&& apk --no-cache --update --virtual=.build-deps add curl \  
&& curl -C - -SL ${RESILIO_URL} -o /tmp/sync.tgz \  
&& tar xf /tmp/sync.tgz -C /usr/bin rslsync \  
&& apk del .build-deps  
  
RUN [ "cross-build-end" ]  
  
COPY sync.conf.default /etc/  
COPY run_sync /usr/bin/  
  
EXPOSE 8888  
EXPOSE 55555  
VOLUME /mnt/sync  
  
ENTRYPOINT ["run_sync"]  
CMD ["--config", "/mnt/sync/sync.conf"]  
  


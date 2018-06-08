FROM ubuntu:16.10  
RUN apt-get -qq update \  
&& apt-get -qq -y install --no-install-recommends curl ca-certificates nfs-
common \  
&& apt-get -qq autoremove -y \  
&& apt-get -qq clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# get dumb-init  
ENV DI_VERSION 1.2.0  
RUN cd /tmp && \  
curl -sL -o /bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DI_VERSION}/dumb-init_${DI_VERSION}_amd64 && \  
chmod +x /bin/dumb-init  
  
# get syncthing  
ENV SYNCTHING_VERSION 0.14.43  
WORKDIR /srv  
  
RUN curl -sS -L -o syncthing.tar.gz
https://github.com/syncthing/syncthing/releases/download/v$SYNCTHING_VERSION/syncthing-
linux-amd64-v$SYNCTHING_VERSION.tar.gz \  
&& tar -xzf syncthing.tar.gz \  
&& rm -f syncthing.tar.gz \  
&& mv syncthing-linux-amd64-v* syncthing \  
&& rm -rf syncthing/etc \  
&& rm -rf syncthing/*.pdf \  
&& mkdir -p /srv/config \  
&& mkdir -p /srv/data  
  
VOLUME ["/srv/data", "/srv/config"]  
  
ADD ./start.sh /start.sh  
RUN chmod 770 /start.sh  
  
ENTRYPOINT ["dumb-init", "--"]  
CMD ["/start.sh"]  
  
ARG VCS_REF  
ARG BUILD_DATE  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/oskapt/docker-syncthing"  


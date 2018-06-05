FROM konstruktoid/debian:wheezy  
  
ENV USER apt-cacher-ng  
  
LABEL \  
org.label-schema.name="AptCacherNG" \  
org.labelschema.url="https://www.unix-ag.uni-kl.de/~bloch/acng/" \  
org.labelschema.vcs-url="https://github.com/konstruktoid/AptCacherNG_Build"  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install apt-cacher-ng --no-install-recommends && \  
apt-get -y clean && \  
mkdir -p /var/log/apt-cacher-ng /var/cache/apt-cacher-ng && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
/usr/share/doc /usr/share/doc-base \  
/usr/share/man /usr/share/locale /usr/share/zoneinfo  
  
COPY ./acng.sh /acng.sh  
  
RUN \  
chmod 0700 /acng.sh && \  
chown -R $USER:$USER /acng.sh /var/cache/apt-cacher-ng /var/log/apt-cacher-ng  
  
VOLUME ["/var/cache/apt-cacher-ng"]  
EXPOSE 3124  
USER $USER  
ENTRYPOINT ["/acng.sh"]  
CMD ["VerboseLog=1","Debug=7","ForeGround=1","PassThroughPattern=.*"]  


FROM debian:jessie  
MAINTAINER Jonas Thiel <jonas@thiel.io>  
  
ENV TARTARUS_VERSION=0.9.8 \  
RELEASE_DATE=2016-09-28 \  
REQUIRED_PACKAGES="tar bzip2 gnupg curl ca-certificates perl-modules"  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q --no-install-
recommends \  
$REQUIRED_PACKAGES \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/cache/debconf/*-old
/usr/share/doc/* /usr/share/man/* \  
&& cp -r /usr/share/locale/en\@* /tmp/ && rm -rf /usr/share/locale/* && mv
/tmp/en\@* /usr/share/locale/  
  
RUN curl -O -L
https://github.com/wertarbyte/tartarus/archive/release/$TARTARUS_VERSION.tar.gz
\  
&& tar xzf $TARTARUS_VERSION.tar.gz \  
&& rm $TARTARUS_VERSION.tar.gz \  
&& cp -R tartarus-release-$TARTARUS_VERSION/bin/* /usr/local/sbin \  
&& cp -R tartarus-release-$TARTARUS_VERSION/lib/Tartarus /usr/share/perl5/ \  
&& rm -r tartarus-release-$TARTARUS_VERSION \  
&& mkdir -p /var/backups/conf /var/backups/in /var/backups/out
/var/backups/timestamps  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
COPY conf/* /var/backups/conf  
  
WORKDIR /var/backups  
  
VOLUME /var/backups/out /var/backups/timestamps  
  
CMD ["app:start"]  


FROM debian:stable-slim  
  
LABEL name="pkg-cacher" \  
version="1.1.1" \  
maintainer="Reto Gantenbein <reto.gantenbein@linuxmonk.ch>"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
bzip2 \  
libwww-curl-perl \  
libwww-perl \  
libdigest-sha-perl \  
libclass-accessor-perl \  
libdbi-perl \  
libdbd-sqlite3-perl \  
libxml-simple-perl \  
libxml-twig-perl \  
libio-compress-lzma-perl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN install -m 755 -d /etc/pkg-cacher \  
&& install -m 755 -d /usr/share/pkg-cacher/Repos \  
&& install -m 755 -d /var/cache/pkg-cacher \  
&& install -m 755 -d /var/log/pkg-cacher  
  
COPY pkg-cacher.conf /etc/pkg-cacher/  
  
COPY pkg-cacher \  
pkg-cacher.pl \  
pkg-cacher-cleanup.pl \  
pkg-cacher-fetch.pl \  
pkg-cacher-lib.pl \  
pkg-cacher-report.pl \  
pkg-cacher-request.pl \  
Repos.pm \  
index_files.regexp \  
static_files.regexp \  
/usr/share/pkg-cacher/  
  
COPY Repos/Debian.pm \  
Repos/Fedora.pm \  
/usr/share/pkg-cacher/Repos/  
  
RUN ln -sf /usr/share/pkg-cacher/pkg-cacher /usr/sbin/pkg-cacher  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/pkg-cacher/access.log \  
&& ln -sf /dev/stderr /var/log/pkg-cacher/error.log  
  
VOLUME /var/cache/pkg-cacher  
  
EXPOSE 8080  
  
CMD /usr/sbin/pkg-cacher user=$(id -un) group=$(id -gn) daemon_port=8080  


FROM debian:jessie  
MAINTAINER Merikz <merikz.code@gmail.com>  
  
ENV TZ Europe/Stockholm  
RUN set -x \  
&& echo $TZ > /etc/timezone \  
&& rm /etc/timezone \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
RUN set -x \  
&& echo "deb http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --force-yes deb-multimedia-keyring \  
&& apt-get clean  
  
# Need --force-yes because not all are signed even with above keyring (libfaac
etc)  
RUN set -x \  
&& DEBIAN_FRONTEND=noninteractive apt-get install \  
-y --force-yes --no-install-recommends \  
supervisor \  
perl5 \  
locales \  
faad \  
faac \  
flac \  
lame \  
sox \  
wavpack \  
curl \  
libio-socket-ssl-perl \  
&& apt-get clean  
  
RUN set -x \  
&& echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen \  
&& DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
# Fix UID for squeezeboxserver user to help with host volumes  
ARG LMS_UID  
RUN set -x \  
&& useradd \  
\--system \  
\--uid ${LMS_UID} \  
-M \  
-s /bin/false \  
-d /usr/share/squeezeboxserver \  
-G nogroup \  
-c "Logitech Media Server user" \  
squeezeboxserver  
  
ARG LMS_URL  
ARG LMS_VERSION  
RUN set -x \  
&& curl -o /tmp/lms.deb ${LMS_URL} \  
&& dpkg -i /tmp/lms.deb \  
&& rm /tmp/lms.deb \  
&& echo ${LMS_VERSION} > /lms_version.txt  
  
# Move config dir to allow editing convert.conf  
RUN set -x \  
&& mkdir -p /mnt/state/etc \  
&& mv /etc/squeezeboxserver /etc/squeezeboxserver.orig \  
&& cp -pr /etc/squeezeboxserver.orig/* /mnt/state/etc \  
&& ln -s /mnt/state/etc /etc/squeezeboxserver \  
&& chown -R squeezeboxserver.nogroup /mnt/state \  
\  
&& mkdir -p /var/log/supervisor  
  
COPY ./supervisord.conf /etc/  
COPY ./start-lms.sh /  
  
VOLUME ["/mnt/state","/mnt/music","/mnt/playlists"]  
EXPOSE 3483 3483/udp 9000 9090 9010  
CMD ["/start-lms.sh"]


FROM debian:stretch  
  
RUN export rsync_version=3.1.3 \  
&& export DEBIAN_FRONTEND=noninteractive \  
\  
&& apt-get -q -y update \  
&& apt-get -q -y install build-essential \  
wget \  
&& apt-get -q -y install libpopt0 \  
zlib1g \  
\  
&& apt-get -q -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
\  
&& wget https://www.samba.org/ftp/rsync/src/rsync-${rsync_version}.tar.gz \  
&& tar xvf rsync-${rsync_version}.tar.gz \  
&& rm rsync-${rsync_version}.tar.gz \  
&& cd rsync-${rsync_version} \  
\  
&& ./configure \--prefix=/ \  
&& make \  
&& make install \  
\  
&& cd \- \  
&& rm -rf rsync-${rsync_version} \  
\  
&& touch /etc/rsyncd.secrets \  
&& chmod 600 /etc/rsyncd.secrets \  
\  
&& echo "log file = /dev/stdout" > /etc/rsyncd.conf \  
&& echo "use chroot = yes" >> /etc/rsyncd.conf \  
&& echo "list = yes" >> /etc/rsyncd.conf \  
&& echo "strict modes = yes" >> /etc/rsyncd.conf \  
&& echo "secrets file = /etc/rsyncd.secrets" >> /etc/rsyncd.conf \  
&& echo "uid = nobody" >> /etc/rsyncd.conf \  
&& echo "gid = nogroup" >> /etc/rsyncd.conf \  
&& echo "transfer logging = no" >> /etc/rsyncd.conf \  
&& echo "timeout = 600" >> /etc/rsyncd.conf \  
&& echo "ignore errors = no" >> /etc/rsyncd.conf \  
&& echo "refuse options = checksum dry-run" >> /etc/rsyncd.conf \  
&& echo "dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz"
>> /etc/rsyncd.conf \  
&& echo "" >> /etc/rsyncd.conf  
  
VOLUME ["/shares"]  
  
EXPOSE 873  
  
COPY scripts /usr/local/bin/  
  
HEALTHCHECK CMD ["docker-healthcheck.sh"]  
ENTRYPOINT ["entrypoint.sh"]  
  
CMD [ "rsync", "--no-detach", "--daemon", "--config", "/etc/rsyncd.conf" ]  


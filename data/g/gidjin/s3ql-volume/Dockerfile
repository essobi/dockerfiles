FROM debian:stretch  
MAINTAINER John Gedeon <js1@gedeons.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends ntpdate \  
inotify-tools python-paramiko python-gobject-2 \  
python-boto duplicity s3ql fuse unison ruby && \  
gem install daemons faraday  
  
RUN apt-get clean &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup  
  
USER root  
ENV HOME=/root  
WORKDIR /root  
  
RUN mkdir -p /mnt/s3ql/data  
RUN mkdir -p /mnt/s3ql/cache  
RUN mkdir -p /volume  
RUN mkdir -p /root/.unison  
  
RUN mkdir /root/.s3ql && ln -s /mnt/s3ql/authinfo2 /root/.s3ql/authinfo2  
  
# add utilities  
COPY *.prf /root/.unison/  
COPY bin/* /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
  
VOLUME /mnt/s3ql  
  
ENTRYPOINT ["/usr/local/bin/mount.sh"]  
  
CMD ["echo", "mount.s3ql", "[options]",
"s3c://objects.dreamhost.com/bucket/path/"]  
  


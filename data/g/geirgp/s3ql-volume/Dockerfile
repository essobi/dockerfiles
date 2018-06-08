FROM debian:stretch  
MAINTAINER John Gedeon <js1@gedeons.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends \  
inotify-tools python-paramiko python-gobject-2 \  
python-boto duplicity s3ql ssh fuse curl build-essential ruby ocaml-native-
compilers exuberant-ctags && \  
gem install daemons faraday  
  
RUN curl -o unison.tar.gz -SL
http://www.seas.upenn.edu/~bcpierce/unison//download/releases/stable/unison-2.48.3.tar.gz
\  
&& tar -xzf unison.tar.gz -C / \  
&& rm unison.tar.gz \  
&& cd /unison-2.48.3 \  
&& HOME=/usr/local make UISTYLE=text NATIVE=true install \  
&& cd / \  
&& rm -rf /unison-2.48.3 \  
&& unison -version  
  
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
RUN mkdir -p /root/.unison /root/.ssh /var/run/sshd  
  
RUN mkdir /root/.s3ql && ln -s /mnt/s3ql/authinfo2 /root/.s3ql/authinfo2  
  
# add utilities  
COPY *.prf /root/.unison/  
COPY bin/* /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
COPY sshd_config /etc/ssh/sshd_config  
  
VOLUME /mnt/s3ql  
  
ENTRYPOINT ["/usr/local/bin/mount.sh"]  
  
CMD ["echo", "mount.s3ql", "[options]",
"s3c://objects.dreamhost.com/bucket/path/"]  
  


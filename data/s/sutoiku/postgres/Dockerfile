FROM debian:stretch-slim  
  
RUN bash -c 'mkdir -p /usr/share/man/man{1,2,3,4,5,6,7,8}' && \  
apt-get update && export DEBIAN_FRONTEND=noninteractive && \  
apt-get install -q -y --no-install-recommends locales && \  
mkdir -p /usr/share/locale/ && touch /usr/share/locale/locale.alias && \  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
&& export LANG=en_US.utf8 && \  
apt-get install -q -y --no-install-recommends postgresql-common && \  
sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf && \  
apt-get install -q -y --no-install-recommends postgresql postgresql-client &&
\  
mkdir /docker-entrypoint-initdb.d && \  
addgroup --gid 40561 stoic && useradd --gid 40561 --uid 40561 stoic && \  
rm -rf /usr/share/man /var/lib/apt/lists/*  
  
ENV LANG en_US.utf8  
  
ENV PGDATA /var/lib/postgresql/data  
#VOLUME /var/lib/postgresql/data  
COPY docker-entrypoint.sh /  
  
WORKDIR /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
#EXPOSE 5432  
CMD ["postgres"]  
USER stoic  


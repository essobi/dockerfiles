FROM golang:1.6.2  
MAINTAINER Andrei Tretyakov <andrei.tretyakov@gmail.com>  
  
ENV CONFD_VERSION 0.11.0  
RUN cd /usr/src \  
&& mkdir -p $GOPATH/src/github.com/kelseyhightower \  
&& curl -SLO
"https://github.com/kelseyhightower/confd/archive/v$CONFD_VERSION.tar.gz" \  
&& tar xvzf "v$CONFD_VERSION.tar.gz" -C
"$GOPATH/src/github.com/kelseyhightower" \  
&& rm -rf "/usr/src/v$CONFD_VERSION.tar.gz" \  
&& cd "$GOPATH/src/github.com/kelseyhightower/confd-$CONFD_VERSION" \  
&& go get github.com/constabulary/gb/... \  
&& ./build . \  
&& ./install \  
&& bash -c "mkdir -pv /etc/confd/{conf.d,templates}"  
  
ENV PGBOUNCER_VERSION 1.7.2  
RUN apt-get update \  
&& apt-get install -y automake libevent-dev libssl-dev libtool pkg-config
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /usr/src \  
&& curl -SLO
"https://pgbouncer.github.io/downloads/files/$PGBOUNCER_VERSION/pgbouncer-$PGBOUNCER_VERSION.tar.gz"
\  
&& tar xvzf "pgbouncer-$PGBOUNCER_VERSION.tar.gz" \  
&& rm -rf "/usr/src/pgbouncer-$PGBOUNCER_VERSION.tar.gz" \  
&& cd "pgbouncer-$PGBOUNCER_VERSION/" \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install \  
&& groupadd -r postgres && useradd -r -g postgres postgres \  
&& bash -c "mkdir -pv /etc/pgbouncer /var/{log,run}/pgbouncer" \  
&& bash -c "chown -R postgres:postgres /etc/pgbouncer
/var/{log,run}/pgbouncer"  
  
COPY entrypoint.sh /  
COPY conf.d/* /etc/confd/conf.d/  
COPY templates/* /etc/confd/templates/  
  
ENTRYPOINT ["/entrypoint.sh"]  


#FROM alpine:3.3  
FROM frolvlad/alpine-oraclejdk8  
  
  
# himpy von riemann brauch haskell  
# https://github.com/mitchty/alpine-ghc/blob/master/Dockerfile  
ENV PATH ${PATH}:/root/.cabal/bin  
COPY mitch.tishmack@gmail.com-55881c97.rsa.pub
/etc/apk/keys/mitch.tishmack@gmail.com-55881c97.rsa.pub  
WORKDIR /root  
RUN echo "https://s3-us-west-2.amazonaws.com/alpine-ghc/8.0" >>
/etc/apk/repositories && \  
apk add -U --no-cache --virtual .build-deps zlib-dev musl-dev gmp-dev net-
snmp-dev ghc cabal stack git openssh && \  
cabal update && \  
cabal sandbox init && \  
git clone https://github.com/pyr/himpy.git &&\  
cd himpy &&\  
cabal install && \  
apk del .build-deps && \  
rm -rf /var/cache/apk/*  
ADD himpy/himpy.conf /etc/himpy.conf  
  
# add riemann-dashboard (needs ruby)  
RUN apk add --no-cache curl wget bash ruby ruby-bundler ruby-rdoc ruby-irb  
RUN gem install riemann-dash  
RUN rm -rf /var/cache/apk/*  
RUN mkdir /etc/riemann  
ADD ./riemann-dash-config.rb /etc/riemann/riemann-dash-config.rb  
# riemann-dash", "/etc/riemann/riemann-dash-config.rb"  
# influxdb  
ENV INFLUXDB_VERSION=0.13.0  
RUN apk add --no-cache --virtual .build-deps wget gnupg tar ca-certificates &&
\  
update-ca-certificates && \  
gpg --keyserver hkp://ha.pool.sks-keyservers.net \  
\--recv-keys 05CE15085FC09D18E99EFB22684A14CF2582E0C5 && \  
wget -q
https://dl.influxdata.com/influxdb/releases/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz.asc
&& \  
wget -q
https://dl.influxdata.com/influxdb/releases/influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz
&& \  
gpg --batch --verify
influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz.asc
influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz && \  
mkdir -p /usr/src && \  
tar -C /usr/src -xzf influxdb-${INFLUXDB_VERSION}-static_linux_amd64.tar.gz &&
\  
rm -f /usr/src/influxdb-*/influxdb.conf && \  
chmod +x /usr/src/influxdb-*/* && \  
cp -a /usr/src/influxdb-*/* /usr/bin/ && \  
rm -rf *.tar.gz* /usr/src /root/.gnupg && \  
apk del .build-deps  
  
RUN mkdir -p /etc/influxdb /usr/share/collectd  
COPY types.db /usr/share/collectd/types.db  
  
# add influxsnmp  
ENV GOPATH /go  
ENV PATH /go/bin:$PATH  
RUN mkdir -p /go/src /go/bin && chmod -R 777 /go && \  
apk --update add bash go net-snmp-tools && \  
apk --update add --virtual build-dependencies bzr git mercurial subversion
openssh-client ca-certificates && \  
cd /go/src && go get github.com/paulstuart/influxsnmp && go install
github.com/paulstuart/influxsnmp && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/*  
ADD influxsnmp/influxsnmp.cfg /root/influxsnmp.cfg  
ADD influxsnmp/NYMNETWORKS-MIB.txt /root/.snmp/mibs/NYMNETWORKS-MIB.txt  
  
# riemann  
ENV RIEMANN_VERSION=0.2.11 \  
RIEMANN_PATH_CONF=/opt/riemann \  
RIEMANN_CONFIG=/opt/riemann/riemann.config  
  
RUN apk -U add bash  
ADD https://aphyr.com/riemann/riemann-$RIEMANN_VERSION.tar.bz2
/riemann.tar.bz2  
RUN chmod 777 /riemann.tar.bz2 && \  
mkdir -p /opt/riemann && \  
cd /opt/riemann/ && tar -xj -f /riemann.tar.bz2 && rm -f /riemann.tar.bz2  
  
# see https://asylum.madhouse-project.org/blog/2014/12/09/monitoring-setup/  
# riemann-extra needs lein  
ENV LEIN_ROOT=true  
# get curl and bash, which we'll use to build.  
RUN apk add --update curl bash && rm -rf /var/cache/apk/*  
# download and install Leiningen  
RUN curl
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
./lein  
RUN chmod a+x ./lein  
RUN mv ./lein /usr/bin/lein  
  
# add riemann-syntax-checker and riemann-extra  
RUN apk add -U --no-cache --virtual .build-deps git && \  
cd && \  
git clone https://github.com/samn/riemann-syntax-check.git && \  
cd riemann-syntax-check && \  
LEIN_ROOT=1 lein uberjar && \  
cd && \  
git clone https://github.com:/pyr/riemann-extra.git && \  
cd riemann-extra && \  
LEIN_ROOT=1 lein uberjar && \  
apk del .build-deps && \  
rm -rf /var/cache/apk/*  
  
  
ENV EXTRA_CLASSPATH=/root/riemann-extra/target/riemann-extra-0.2.4.jar  
  
# use runit instead of supervisord which needs python  
ADD start_runit /sbin/  
RUN mkdir /etc/container_environment &&\  
mkdir /etc/service &&\  
mkdir -p /etc/service/riemann-dashboard &&\  
mkdir -p /etc/service/confd/log &&\  
mkdir -p /etc/service/influxdb/log &&\  
mkdir -p /etc/service/riemann/log &&\  
mkdir -p /var/log/runit/confd &&\  
mkdir -p /var/log/runit/influxdb &&\  
mkdir -p /var/log/runit/riemann &&\  
chmod a+x /sbin/start_runit && mkdir /etc/runit_init.d && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk --update upgrade && apk add runit && rm -rf /var/cache/apk/*  
  
# adding confd  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.12.0-alpha3/confd-0.12.0-alpha3-linux-
amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
# adding confd-templates  
ADD confd /etc/confd  
  
# entrypoint.sh is used for confd  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
VOLUME /var/lib/influxdb  
  
## influxdb-ports for admin-server/webui/http-api/collectd  
## riemann-ports: 5555 - Riemann TCP and UDP - 5556 - Riemann WS  
## riemann-dashboard: 4567  
EXPOSE 8083 8086 25826/udp 5555 5555/udp 5556 4567  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/sbin/start_runit"]  


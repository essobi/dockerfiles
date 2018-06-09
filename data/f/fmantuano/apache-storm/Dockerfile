FROM phusion/baseimage  
  
MAINTAINER Fedele Mantuano "mantuano.fedele@gmail.com"  
# labels  
LABEL description="Apache Storm (all-in-one): zookeeper, nimbus, ui,
supervisor" \  
repository_url="https://github.com/fedelemantuano/apache-storm-dockerfile"  
  
# args that can change from command line  
ARG GPG_KEY=ACEFE18DD2322E1E84587A148DE03962E80B8FFD  
ARG DISTRO_NAME=apache-storm-1.1.1  
# environment variables  
ENV STORM_CONF_DIR=/conf \  
STORM_DATA_DIR=/data \  
STORM_LOG_DIR=/logs \  
PATH=$PATH:/$DISTRO_NAME/bin  
  
# make directories  
RUN set -ex; \  
mkdir -p "/etc/service/zookeeperd" "/etc/service/nimbus"
"/etc/service/supervisor" "/etc/service/ui"; \  
mkdir -p "$STORM_CONF_DIR" "$STORM_DATA_DIR" "$STORM_LOG_DIR"; \  
# install packages  
apt-get -yqq update; \  
apt-get -yqq upgrade -o Dpkg::Options::="--force-confold"; \  
apt-get -yqq --no-install-recommends install \  
curl \  
openjdk-8-jre \  
python \  
zookeeperd; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*; \  
# Download Apache Storm, verify its PGP signature, untar and clean up  
curl -So "$DISTRO_NAME.tar.gz"
"http://www.apache.org/dist/storm/$DISTRO_NAME/$DISTRO_NAME.tar.gz"; \  
curl -So "$DISTRO_NAME.tar.gz.asc"
"http://www.apache.org/dist/storm/$DISTRO_NAME/$DISTRO_NAME.tar.gz.asc"; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-key "$GPG_KEY" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$GPG_KEY" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$GPG_KEY"; \  
gpg --batch --verify "$DISTRO_NAME.tar.gz.asc" "$DISTRO_NAME.tar.gz"; \  
tar -xzf "$DISTRO_NAME.tar.gz"; \  
rm -rf "$GNUPGHOME" "$DISTRO_NAME.tar.gz" "$DISTRO_NAME.tar.gz.asc";  
  
WORKDIR $DISTRO_NAME  
  
# copy run scripts  
COPY run/zookeeperd.sh /etc/service/zookeeperd/run  
COPY run/nimbus.sh /etc/service/nimbus/run  
COPY run/supervisor.sh /etc/service/supervisor/run  
COPY run/ui.sh /etc/service/ui/run  
COPY run/logviewer.sh /etc/service/logviewer/run  
  
# copy configuration  
COPY zookeeper/zoo.cfg /etc/zookeeper/conf/zoo.cfg  
COPY storm/storm.yaml $STORM_CONF_DIR/storm.yaml  
  
RUN set -ex; \  
sed -i "s!storm.log.dir:.*!storm.log.dir: $STORM_LOG_DIR!g"
$STORM_CONF_DIR/storm.yaml; \  
sed -i "s!storm.local.dir:.*!storm.local.dir: $STORM_DATA_DIR!g"
$STORM_CONF_DIR/storm.yaml;  
  
# ports  
EXPOSE 8080 8000  
# volume  
VOLUME ["/logs"]  
  
# init for phusion/baseimage  
CMD ["/sbin/my_init"]  


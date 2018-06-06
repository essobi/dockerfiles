FROM mesoform/concierge-debian-base-image:devtest  
LABEL maintainer="dan <dan@mesoform.com>"  
LABEL description="Concierge maintained MySQL for Mesoform"  
LABEL com.mesoform.baseimage="False"  
LABEL com.joyent.autopilotpattern="True"  
LABEL com.mesoform.builddate="2017-09-07T18:32:51Z"  
LABEL com.mesoform.baseimage.ver="mesoform/concierge-debian-base-
image:devtest"  
LABEL com.docker.img.ver="mesoform/concierge-mysql:concierge-0.2.32"  
  
# set some build variables  
ARG APT_FLAGS_COMMON="-qq -y"  
ARG APT_FLAGS_PERSISTANT="${APT_FLAGS_COMMON} --no-install-recommends"  
ENV DNS_DOMAIN=mysql.dockerlx.oaas.mesoform.com  
  
# Adding Percona 5.6 Dockerfile used on autopilotpattern/mysql  
# (Percona Server is a fork of the MySQL relational database management system
created by Percona)  
# https://hub.docker.com/_/percona/  
#  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
# add gosu for easy step-down from root  
ENV GOSU_VERSION="1.7"  
ENV GOSU_REPO="https://github.com/tianon/gosu/releases/download"  
ENV GOSU_KEY="B42F6819007F00F88E364FD4036A9C25BF357DD4"  
RUN set -x \  
&& apt-get update && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu "${GOSU_REPO}/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc "${GOSU_REPO}/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys ${GOSU_KEY} \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
# install "pwgen" for randomizing passwords  
# install "apt-transport-https" for Percona's repo (switched to https-only)  
RUN apt-get update && apt-get ${APT_FLAGS_PERSISTANT} install \  
apt-transport-https ca-certificates \  
pwgen \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEYS="430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A
4D1BB29D63D98E422B2113B19334A25F8507EFA5"  
# pub 1024D/CD2EFD2A 2009-12-15  
# Key fingerprint = 430B DF5C 56E7 C94E 848E E60C 1C4C BDCD CD2E FD2A  
# uid Percona MySQL Development Team <mysql-dev@percona.com>  
# sub 2048g/2D607DAF 2009-12-15  
# pub 4096R/8507EFA5 2016-06-30  
# Key fingerprint = 4D1B B29D 63D9 8E42 2B21 13B1 9334 A25F 8507 EFA5  
# uid Percona MySQL Development Team (Packaging key) <mysql-dev@percona.com>  
# sub 4096R/4CAC6D72 2016-06-30  
RUN set -ex; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done; \  
gpg --export $GPG_KEYS > /etc/apt/trusted.gpg.d/percona.gpg; \  
rm -r "$GNUPGHOME"; \  
apt-key list  
  
RUN echo 'deb https://repo.percona.com/apt jessie main' >
/etc/apt/sources.list.d/percona.list  
  
ENV PERCONA_MAJOR="5.6"  
ENV PERCONA_VERSION="5.6.39-83.1-1.jessie"  
# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't
have an explicit way to disable the mysql_install_db codepath besides having a
database already "configured" (ie, stuff in /var/lib/mysql/mysql)  
# also, we set debconf keys to make APT a little quieter  
RUN { \  
for key in \  
percona-server-server/root_password \  
percona-server-server/root_password_again \  
"percona-server-server-$PERCONA_MAJOR/root-pass" \  
"percona-server-server-$PERCONA_MAJOR/re-root-pass" \  
; do \  
echo "percona-server-server-$PERCONA_MAJOR" "$key" password 'unused'; \  
done; \  
} | debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y \  
percona-server-server-$PERCONA_MAJOR=$PERCONA_VERSION \  
&& rm -rf /var/lib/apt/lists/* \  
# comment out any "user" entires in the MySQL config ("docker-entrypoint.sh"
or "--user" will handle user switching)  
&& sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf \  
# purge and re-create /var/lib/mysql with appropriate ownership  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld  
  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
RUN \  
find /etc/mysql/ -name '*.cnf' -print0 \  
| xargs -0 grep -lZE '^(bind-address|log)' \  
| xargs -0 sed -Ei 's/^(bind-address|log)/#&/' \  
&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' >
/etc/mysql/conf.d/docker.cnf  
  
# Adding autopilotpattern/mysql Dockerfile  
# By keeping a lot of discrete steps in a single RUN we can clean up after
ourselves in the same layer.  
# This is gross but it saves ~100MB in the image  
RUN set -ex \  
&& export buildDeps='python-dev gcc unzip' \  
&& export runDeps='python curl libffi-dev libssl-dev percona-xtrabackup ca-
certificates' \  
&& apt-get update \  
&& apt-get ${APT_FLAGS_PERSISTANT} install $buildDeps $runDeps \  
# \  
# get Python drivers MySQL, Consul, and Manta \  
# \  
&& curl -Lsfo /tmp/mysql-connector.deb
http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-
python_2.1.3-1debian8.2_all.deb \  
&& dpkg -i /tmp/mysql-connector.deb \  
&& curl -Lsfo /tmp/mysql-utils.deb
http://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-
utilities_1.5.6-1debian8_all.deb \  
&& dpkg -i /tmp/mysql-utils.deb \  
&& curl -Lsfo get-pip.py https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install \  
python-Consul==0.7.0 \  
manta==2.5.0 \  
mock==2.0.0 \  
json5==0.2.4 \  
# \  
# clean up to minimize image layer size \  
# \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm /tmp/mysql-connector.deb \  
&& rm /tmp/mysql-utils.deb \  
&& rm /get-pip.py  
  
# configure ContainerPilot and MySQL  
COPY etc/* /etc/  
COPY bin/manager /usr/local/bin/manager  
COPY bin/test.py /usr/local/bin/test.py  
COPY bin/manage.py /usr/local/bin/manage.py  
  
VOLUME ["/var/lib/mysql", "/var/log/mysql"]  
  
EXPOSE 3306  
# override the parent entrypoint  
ENTRYPOINT []  
CMD ["mysqld"]  
CMD ["/usr/local/bin/containerpilot"]


FROM centos:7.3.1611  
MAINTAINER Jordan Wesolowski <jrwesolo@gmail.com>  
  
# install gosu  
ENV GOSU_VERSION="1.10"  
RUN curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64"
\  
&& curl -o /usr/local/bin/gosu.asc -sSL
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-
amd64.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver pgp.mit.edu --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf "${GNUPGHOME}" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# createrepo used for repo generation  
# pv used for yumsync backup and restore  
RUN yum install -y epel-release \  
&& yum install -y createrepo pv \  
&& yum clean all  
  
# pip installation  
RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python  
  
ENV YUMSYNC_VERSION="1.3.0"  
RUN curl -sSL
"https://github.com/jrwesolo/yumsync/archive/v${YUMSYNC_VERSION}.tar.gz" | \  
tar -C /usr/local/src -xz \  
&& cd "/usr/local/src/yumsync-${YUMSYNC_VERSION}" \  
&& python setup.py bdist_wheel \  
&& pip install dist/yumsync-*.whl \  
&& rm -rf "/usr/local/src/yumsync-${YUMSYNC_VERSION}"  
  
ENV YUMSYNC_CONF=/etc/yumsync \  
YUMSYNC_DATA=/data \  
YUMSYNC_USER=yumsync YUMSYNC_UID=489 \  
YUMSYNC_GROUP=yumsync YUMSYNC_GID=489  
RUN groupadd -g "${YUMSYNC_GID}" "${YUMSYNC_GROUP}" \  
&& useradd -s /bin/bash -d "${YUMSYNC_CONF}" -M -N -u "${YUMSYNC_UID}" -g
"${YUMSYNC_GROUP}" \-- "${YUMSYNC_USER}" \  
&& mkdir -p "${YUMSYNC_DATA}" "${YUMSYNC_CONF}" \  
&& chown "${YUMSYNC_USER}":"${YUMSYNC_GROUP}" "${YUMSYNC_DATA}"
"${YUMSYNC_CONF}" \  
&& chmod 0755 "${YUMSYNC_DATA}" "${YUMSYNC_CONF}"  
  
COPY docker /docker  
  
VOLUME $YUMSYNC_DATA  
WORKDIR $YUMSYNC_DATA  
ENTRYPOINT ["/docker/run"]  
CMD []  


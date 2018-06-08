# "ported" by Adam Miller <maxamillion@fedoraproject.org> from  
# https://github.com/fedora-cloud/Fedora-Dockerfiles  
#  
# Originally written for Fedora-Dockerfiles by  
# scollier <scollier@redhat.com>  
FROM amazeeio/centos:7  
ENV COUCH_URL="https://www.apache.org/dist/couchdb/source/1.6.1/" \  
COUCH_CONFIG_DIR="/usr/local/etc/couchdb/" \  
COUCH_NAME="apache-couchdb-1.6.1" \  
COUCH_DEP="wget make autoconf autoconf-archive automake libtool perl-Test-
Harness erlang libicu-devel js-devel curl-devel gcc-c++" \  
CLEANUP_PKGS="wget make"  
ENV COUCH_TAR="${COUCH_NAME}.tar.gz" \  
COUCH_DIR="${COUCH_NAME}"  
ENV COUCH_ASC="${COUCH_TAR}.asc"  
# Install epel  
RUN yum -y install epel-release && \  
yum -y install $COUCH_DEP && yum clean all && \  
wget "${COUCH_URL}${COUCH_TAR}" && \  
wget "${COUCH_URL}${COUCH_ASC}" && \  
gpg --keyserver pgpkeys.mit.edu --recv-key 04F4EE9B && \  
gpg --verify ${COUCH_ASC} ${COUCH_TAR} && \  
tar -xzf ${COUCH_TAR} && \  
cd ${COUCH_DIR} && \  
/bin/sh ./configure --with-erlang=/usr/lib64/erlang/usr/include && \  
make && make install && \  
yum -y remove ${CLEANUP_PKGS} && yum clean all && \  
cd .. && \  
rm -rf ${COUCH_NAME}*  
  
# Configure couchdb to listen at 0.0.0.0  
RUN sed -e 's/^bind_address = .*$/bind_address = 0.0.0.0/' -i
"${COUCH_CONFIG_DIR}default.ini"  
  
RUN fix-permissions /lost+found && \  
fix-permissions /usr/local/etc/couchdb && \  
fix-permissions /usr/local/var/lib/couchdb && \  
fix-permissions /usr/local/var/log/couchdb && \  
fix-permissions /usr/local/var/run/couchdb  
  
EXPOSE 5984  
CMD ["/usr/local/bin/couchdb", "start"]  


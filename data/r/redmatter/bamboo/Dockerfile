FROM java:8  
  
MAINTAINER Dino.Korah@redmatter.com  
  
ARG RUN_USER=daemon  
ARG RUN_GROUP=daemon  
ARG RUN_USER_HOME_DIR=  
  
ENV TZ="Europe/London" \  
# unprivileged users used to run the app  
RUN_USER=${RUN_USER} \  
RUN_GROUP=${RUN_GROUP} \  
# bamboo variables  
BAMBOO_VERSION="5.15.3" \  
BAMBOO_HOME="/var/atlassian/application-data/bamboo" \  
BAMBOO_INSTALL_DIR="/opt/atlassian/bamboo"  
  
ADD https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz /tmp/files.tar.gz  
COPY https_proxy_server_xml.patch /tmp/  
COPY entrypoint.sh /entrypoint.sh  
  
RUN ( \  
export DEBIAN_FRONTEND=noninteractive; \  
export BUILD_DEPS="patch"; \  
export APP_DEPS="libtcnative-1"; \  
  
MYSQL_CONNECTOR_VERSION=5.1.41; \  
MYSQL_CONNECTOR_URL="https://cdn.mysql.com//Downloads/Connector-J/mysql-
connector-java-${MYSQL_CONNECTOR_VERSION}.tar.gz"; \  
  
set -e -u -x; \  
  
apt-get update; \  
apt-get -y upgrade; \  
apt-get install -y \--no-install-recommends ${APP_DEPS} ${BUILD_DEPS}; \  
  
mkdir -p ${BAMBOO_INSTALL_DIR}; \  
tar -C ${BAMBOO_INSTALL_DIR} --strip-components=1 -xzf /tmp/files.tar.gz; \  
echo "bamboo.home=${BAMBOO_HOME}" >> ${BAMBOO_INSTALL_DIR}/atlassian-
bamboo/WEB-INF/classes/bamboo-init.properties; \  
  
# setup reverse proxy settings  
# More details here https://confluence.atlassian.com/bamboo/integrating-
bamboo-with-apache-http-server-391087370.html  
patch -p1 -d ${BAMBOO_INSTALL_DIR} < /tmp/https_proxy_server_xml.patch; \  
rm /tmp/https_proxy_server_xml.patch; \  
  
mkdir ${BAMBOO_INSTALL_DIR}/lib/native; \  
ln --symbolic "/usr/lib/x86_64-linux-gnu/libtcnative-1.so"
"${BAMBOO_INSTALL_DIR}/lib/native/libtcnative-1.so"; \  
  
wget -qO- "${MYSQL_CONNECTOR_URL}" | \  
tar -xz -O mysql-connector-java-${MYSQL_CONNECTOR_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar \  
>"${BAMBOO_INSTALL_DIR}/lib/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar"; \  
  
mkdir -p "${BAMBOO_HOME}"; \  
  
# If RUN_USER's home directory is not specified as a build parameter, fall
back to BAMBOO_HOME  
[ -n "${RUN_USER_HOME_DIR}" ] || RUN_USER_HOME_DIR="$BAMBOO_HOME"; \  
  
# if the specified RUN_GROUP is not present add it  
getent group "${RUN_GROUP}" >/dev/null 2>&1 || groupadd "${RUN_GROUP}"; \  
  
# check if the specified RUN_USER is present  
if getent passwd "${RUN_USER}" >/dev/null 2>&1 ; then \  
# if present, check if RUN_USER's home directory is not writable  
current_home="$( getent passwd "${RUN_USER}" | cut -d: -f 6 )"; \  
su -c "[ -w \"$current_home\" ]" -s /bin/bash "${RUN_USER}" || \  
# if so, modify the user to set home directory to RUN_USER_HOME_DIR  
usermod -d "${RUN_USER_HOME_DIR}" "${RUN_USER}"; \  
else \  
useradd "${RUN_USER}" -g "${RUN_GROUP}" -d "${RUN_USER_HOME_DIR}"; \  
fi; \  
  
if [ ! -d "${RUN_USER_HOME_DIR}" ]; then \  
mkdir -p "${RUN_USER_HOME_DIR}"; \  
chown "${RUN_USER}:${RUN_GROUP}" "${RUN_USER_HOME_DIR}"; \  
chmod go-rwx "${RUN_USER_HOME_DIR}"; \  
fi; \  
  
mkdir -p "${RUN_USER_HOME_DIR}/.ssh"; \  
  
chown -R "${RUN_USER}:${RUN_GROUP}" "${BAMBOO_INSTALL_DIR}" "${BAMBOO_HOME}"
"${RUN_USER_HOME_DIR}/.ssh"; \  
chmod -R go-rwx "${BAMBOO_INSTALL_DIR}/logs" "${BAMBOO_INSTALL_DIR}/temp" \  
"${BAMBOO_INSTALL_DIR}/work" "${RUN_USER_HOME_DIR}/.ssh"; \  
  
apt-get remove -y $BUILD_DEPS; \  
apt-get clean autoclean; \  
apt-get autoremove --yes; \  
rm -rf /var/lib/{apt,dpkg,cache,log}/; \  
  
# fix issue #2 - replace dash with bash  
ln -sf bash /bin/sh; \  
)  
  
USER ${RUN_USER}:${RUN_GROUP}  
  
VOLUME ["${BAMBOO_HOME}"]  
  
# HTTP port  
EXPOSE 8085  
# Remote agent communication  
EXPOSE 54663  
  
WORKDIR ${BAMBOO_INSTALL_DIR}  
  
CMD ["/entrypoint.sh", "-fg"]  


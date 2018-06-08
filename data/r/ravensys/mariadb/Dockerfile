FROM centos:7  
#  
# MariaDB SQL database server Docker image  
#  
# Environment variables (container initialization):  
# * $MARIADB_ADMIN_PASSWORD password for the `root` admin account  
# * $MARIADB_DATABASE name of database to be created  
# * $MARIADB_PASSWORD password for the user account  
# * $MARIADB_USER name of user to be created  
#  
# Environment variables (mariadb configuration):  
# * $MARIADB_FT_MAX_WORD_LEN  
# * $MARIADB_FT_MIN_WORD_LEN  
# * $MARIADB_INNODB_BUFFER_POOL_SIZE  
# * $MARIADB_INNODB_LOG_BUFFER_SIZE  
# * $MARIADB_INNODB_LOG_FILE_SIZE  
# * $MARIADB_INNODB_USE_NATIVE_AIO  
# * $MARIADB_KEY_BUFFER_SIZE  
# * $MARIADB_LOWER_CASE_TABLE_NAMES  
# * $MARIADB_MAX_ALLOWED_PACKET  
# * $MARIADB_MAX_CONNECTIONS  
# * $MARIADB_READ_BUFFER_SIZE  
# * $MARIADB_SORT_BUFFER_SIZE  
# * $MARIADB_TABLE_OPEN_CACHE  
#  
# Exposed ports:  
# * 3306/tcp mariadb  
#  
# Secrets:  
# * mariadb/admin_password | $MARIADB_ADMIN_PASSWORD_SECRET password for the
`root` admin account  
# * mariadb/database | $MARIADB_DATABASE_SECRET name of database to be created  
# * mariadb/password | $MARIADB_PASSWORD_SECRET password for the user account  
# * mariadb/user | $MARIADB_USER_SECRET name of the user to be created  
#  
# Volumes:  
# * /var/lib/mysql/data mariadb data directory  
#  
ENV MARIADB_VERSION 5.5  
ENV MARIADB_PKGVERSION ${MARIADB_VERSION}.57  
LABEL name="ravensys/mariadb" \  
description="This container image provides a containerized packaging of the
MariaDB mysqld daemon and client \  
application. The mysqld server daemon accepts connections from clients and
provides access to content from MariaDB \  
databases on behalf of the clients. You can find more information on the
MariaDB project from the project Web site \  
(https://mariadb.org/)." \  
version="${MARIADB_VERSION}" \  
release="1" \  
summary="MariaDB SQL database server" \  
maintainer="Tomáš Havlas <tomashavlas@raven-systems.eu>" \  
vendor="Raven Systems"  
  
EXPOSE 3306  
RUN groupadd -g 27 -r mysql && useradd -c 'MariaDB Server' -d /var/lib/mysql
-g mysql -r -u 27 mysql \  
&& yum -y --setopt=tsflags=nodocs install gettext \  
&& { \  
echo '[mariadb]'; \  
echo 'name = MariaDB'; \  
echo 'baseurl = http://yum.mariadb.org/5.5/centos7-amd64'; \  
echo 'gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB'; \  
echo 'gpgcheck=1'; \  
} > /etc/yum.repos.d/mariadb-community.repo \  
&& yum -y --setopt=tsflags=nodocs install MariaDB-server-${MARIADB_PKGVERSION}
\  
&& yum clean all \  
&& localedef -f UTF-8 -i en_US en_US.UTF-8 \  
&& test "$(id mysql)" = "uid=27(mysql) gid=27(mysql) groups=27(mysql)"  
  
ENV CONTAINER_ENTRYPOINT_PATH /usr/share/container-entrypoint  
ENV CONTAINER_SECRETS_PATH /run/secrets  
COPY [ "common/root", "root", "${MARIADB_VERSION}/root", "/" ]  
RUN /usr/libexec/container-setup  
  
VOLUME [ "/var/lib/mysql/data" ]  
  
USER 27  
ENTRYPOINT [ "container-entrypoint" ]  
CMD [ "run-mysqld" ]  


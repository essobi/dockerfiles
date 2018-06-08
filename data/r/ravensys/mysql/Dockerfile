FROM centos:7  
  
#  
# MySQL SQL database server Docker image  
#  
# Environment variables (container initialization):  
# * $MYSQL_ADMIN_PASSWORD password for the `root` admin account  
# * $MYSQL_DATABASE name of database to be created  
# * $MYSQL_PASSWORD password for the user account  
# * $MYSQL_USER name of user to be created  
#  
# Environment variables (mysql configuration):  
# * $MYSQL_FT_MAX_WORD_LEN  
# * $MYSQL_FT_MIN_WORD_LEN  
# * $MYSQL_INNODB_BUFFER_POOL_SIZE  
# * $MYSQL_INNODB_LOG_BUFFER_SIZE  
# * $MYSQL_INNODB_LOG_FILE_SIZE  
# * $MYSQL_INNODB_USE_NATIVE_AIO  
# * $MYSQL_KEY_BUFFER_SIZE  
# * $MYSQL_LOWER_CASE_TABLE_NAMES  
# * $MYSQL_MAX_ALLOWED_PACKET  
# * $MYSQL_MAX_CONNECTIONS  
# * $MYSQL_READ_BUFFER_SIZE  
# * $MYSQL_SORT_BUFFER_SIZE  
# * $MYSQL_TABLE_OPEN_CACHE  
#  
# Exposed ports:  
# * 3306/tcp mysql  
#  
# Secrets:  
# * mysql/admin_password | $MYSQL_ADMIN_PASSWORD_SECRET password for the
`root` admin account  
# * mysql/database | $MYSQL_DATABASE_SECRET name of database to be created  
# * mysql/password | $MYSQL_PASSWORD_SECRET password for the user account  
# * mysql/user | $MYSQL_USER_SECRET name of the user to be created  
#  
# Volumes:  
# * /var/lib/mysql/data mysql data directory  
#  
  
ENV MYSQL_VERSION 5.7  
ENV MYSQL_PKGVERSION ${MYSQL_VERSION}.19  
  
LABEL name="ravensys/mysql" \  
description="This container image provides a containerized packaging of the
MySQL mysqld daemon and client \  
application. The mysqld server daemon accepts connections from clients and
provides access to content from MySQL \  
databases on behalf of the clients. You can find more information on the MySQL
project from the project Web site \  
(https://www.mysql.org/)." \  
version="${MYSQL_VERSION}" \  
release="1" \  
summary="MySQL SQL database server" \  
maintainer="Tomáš Havlas <tomashavlas@raven-systems.eu>" \  
vendor="Raven Systems"  
  
EXPOSE 3306  
  
RUN yum -y --setopt=tsflags=nodocs install gettext \  
&& yum -y --setopt=tsflags=nodocs install
https://repo.mysql.com/mysql57-community-release-el7.rpm \  
&& yum -y --setopt=tsflags=nodocs install mysql-community-
server-${MYSQL_PKGVERSION} \  
&& yum clean all \  
&& localedef -f UTF-8 -i en_US en_US.UTF-8 \  
&& test "$(id mysql)" = "uid=27(mysql) gid=27(mysql) groups=27(mysql)"  
  
ENV CONTAINER_ENTRYPOINT_PATH /usr/share/container-entrypoint  
ENV CONTAINER_SECRETS_PATH /run/secrets  
COPY [ "common/root", "root", "${MYSQL_VERSION}/root", "/" ]  
RUN /usr/libexec/container-setup  
  
VOLUME [ "/var/lib/mysql/data" ]  
  
USER 27  
  
ENTRYPOINT [ "container-entrypoint" ]  
CMD [ "run-mysqld" ]  


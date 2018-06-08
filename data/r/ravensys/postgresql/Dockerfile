FROM centos:7  
#  
# PostgreSQL SQL database server Docker image  
#  
# Environment variables (container initialization):  
# * $POSTGRESQL_ADMIN_PASSWORD password for the `postgres` admin account  
# * $POSTGRESQL_DATABASE name of database to be created  
# * $POSTGRESQL_PASSWORD password for the user account  
# * $POSTGRESQL_USER name of user to be created  
#  
# Environment variables (postgresql configuration):  
# * $POSTGRESQL_EFFECTIVE_CACHE_SIZE  
# * $POSTGRESQL_MAINTENANCE_WORK_MEM  
# * $POSTGRESQL_MAX_CONNECTIONS  
# * $POSTGRESQL_MAX_PREPARED_TRANSACTIONS  
# * $POSTGRESQL_SHARED_BUFFERS  
# * $POSTGRESQL_WORK_MEM  
#  
# Exposed ports:  
# * 5432/tcp postgres  
#  
# Secrets:  
# * postgresql/admin_password | $POSTGRESQL_ADMIN_PASSWORD_SECRET password for
the `postgres` admin account  
# * postgresql/database | $POSTGRESQL_DATABASE_SECRET name of database to be
created  
# * postgresql/password | $POSTGRESQL_PASSWORD_SECRET password for the user
account  
# * postgresql/user | $POSTGRESQL_USER_SECRET name of the user to be created  
#  
# Volumes:  
# * /var/lib/pgsql/data postgresql data directory  
#  
ENV POSTGRESQL_VERSION 9.6  
ENV POSTGRESQL_PKGVERSION ${POSTGRESQL_VERSION}.3  
LABEL name="ravensys/postgresql" \  
description="This container image provides a containerized packaging of the
PostgreSQL postgres daemon and \  
client application. The postgres server daemon accepts connections from
clients and provides access to content from \  
PostgreSQL databases on behalf of the clients. You can find more information
on the PostgreSQL project from the \  
project Web site (https://www.postgresql.org/)." \  
version="${POSTGRESQL_VERSION}" \  
release="1" \  
summary="PostgreSQL database server" \  
maintainer="Tomáš Havlas <tomashavlas@raven-systems.eu>" \  
vendor="Raven Systems"  
  
EXPOSE 5432  
RUN yum -y --setopt=tsflags=nodocs install gettext \  
&& yum -y --setopt=tsflags=nodocs install
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-
centos96-9.6-3.noarch.rpm \  
&& yum -y --setopt=tsflags=nodocs install
postgresql96-server-${POSTGRESQL_PKGVERSION}
postgresql96-contrib-${POSTGRESQL_PKGVERSION} \  
&& yum clean all \  
&& localedef -f UTF-8 -i en_US en_US.UTF-8 \  
&& test "$(id postgres)" = "uid=26(postgres) gid=26(postgres)
groups=26(postgres)"  
ENV PATH "${PATH}:/usr/pgsql-9.6/bin"  
ENV CONTAINER_ENTRYPOINT_PATH /usr/share/container-entrypoint  
ENV CONTAINER_SECRETS_PATH /run/secrets  
COPY [ "common/root", "root", "${POSTGRESQL_VERSION}/root", "/" ]  
RUN /usr/libexec/container-setup  
  
VOLUME [ "/var/lib/pgsql/data" ]  
  
USER 26  
ENTRYPOINT [ "container-entrypoint" ]  
CMD [ "run-postgresql" ]  


FROM ubuntu:12.04.5  
  
# define Docker image label information  
LABEL com.ciandt.vendor="CI&T Software SA" \  
com.ciandt.maintainers.1="Ivan Pinatti - @ivan_pinatti" \  
com.ciandt.maintainers.2="Thomas Bryan - @thobryan"  
  
# defines root user, to perform privileged operations  
USER root  
  
# enable apt mirrors (best performance due to use the closest repository)  
RUN readonly APT_SOURCES="/etc/apt/sources.list" \  
&& readonly UBUNTU_RELEASE_NAME="$(cat /etc/lsb-release | grep CODENAME | cut
-d '=' -f2)" \  
&& sed --in-place \  
\--regexp-extended \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-security main restricted universe multiverse\n\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-backports main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}"-updates main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/deb mirror:\/\/mirrors\\.ubuntu\\.com\/mirrors\\.txt
"${UBUNTU_RELEASE_NAME}" main restricted universe multiverse\n/" \  
\--expression \  
"1s/^/\\# Enable Ubuntu mirrors and multiverse\n/" \  
"${APT_SOURCES}"  
  
# upgrade Ubuntu packages, install security updates and required packages  
RUN readonly UBUNTU_PACKAGES=" \  
curl \  
ca-certificates \  
binutils \  
cpp \  
cpp-4.6 \  
gcc \  
gcc-4.6 \  
libaio1 \  
libc-dev-bin \  
libc6-dev \  
libdbi-perl \  
libgmp10 \  
libgomp1 \  
libmpc2 \  
libmpfr4 \  
libnet-daemon-perl \  
libplrpc-perl \  
libquadmath0 \  
linux-libc-dev \  
manpages \  
manpages-dev \  
psmisc \  
zlib1g-dev \  
pwgen \  
" \  
&& apt-get update \  
&& apt-get upgrade --assume-yes \  
&& apt-get install --no-install-recommends \  
\--assume-yes \  
${UBUNTU_PACKAGES} \  
# remove apt cache in order to improve Docker image size  
&& apt-get clean  
  
## Percona  
# environment variables  
ENV PERCONA_MAJOR_VERSION 5.5  
ENV PERCONA_MINOR_VERSION 24  
ENV PERCONA_RELEASE_VERSION 26.0  
ENV PERCONA_USER mysql  
ENV PERCONA_UID 3306  
ENV GOSU_VERSION 1.7  
  
# create group  
RUN groupadd \  
\--system \  
\--gid ${PERCONA_UID} \  
${PERCONA_USER} \  
# create user and add to group  
&& useradd \  
\--system \  
\--uid ${PERCONA_UID} \  
\--gid ${PERCONA_USER} \  
${PERCONA_USER}  
  
# add gosu for easy step-down from root  
RUN curl \  
\--silent \  
\--show-error \  
\--location \  
\--output \  
/usr/local/bin/gosu \  
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--output \  
/usr/local/bin/gosu.asc \  
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \  
\--keyserver \  
ha.pool.sks-keyservers.net \  
\--recv-keys \  
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm \--recursive "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# create temp folder  
RUN mkdir --parents /tmp/percona \  
&& cd /tmp/percona \  
# download Percona installation files  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/libmysqlclient-
dev_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/libmysqlclient18-dev_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/libmysqlclient18_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
client-${PERCONA_MAJOR_VERSION}_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
client_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
common-${PERCONA_MAJOR_VERSION}_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
server-${PERCONA_MAJOR_VERSION}_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
server_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
&& curl \  
\--silent \  
\--show-error \  
\--location \  
\--remote-name \  
https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
test-${PERCONA_MAJOR_VERSION}_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
\  
# configure package installation  
&& { \  
echo percona-server-server-$PERCONA_MAJOR percona-server-server/root_password
password 'unused'; \  
echo percona-server-server-$PERCONA_MAJOR percona-server-
server/root_password_again password 'unused'; \  
} | debconf-set-selections \  
# install Percona  
&& dpkg \  
\--install \  
*.deb \  
# clean up files  
&& cd / \  
&& rm \  
\--recursive \  
\--force \  
/tmp/percona  
  
# copy Percona configuration file  
COPY files/my.cnf /etc/mysql/my.cnf  
  
# Acquia specifics  
COPY files/repl.cnf /etc/mysql/conf.d/repl.cnf  
COPY files/mycustom.cnf /etc/mysql/conf.d/mycustom.cnf  
  
# purge and re-create /var/lib/mysql with appropriate ownership  
RUN rm \  
\--recursive \  
\--force \  
/var/lib/mysql \  
&& mkdir --parents \  
/var/lib/mysql \  
/var/run/mysqld \  
/mnt/tmp/mysql \  
&& chown \--recursive \  
${PERCONA_USER}:${PERCONA_USER} \  
/var/lib/mysql \  
/var/run/mysqld \  
/mnt/tmp/mysql \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld  
  
## Docker specifics  
# expose service port  
EXPOSE 3306  
  
# change workdir  
WORKDIR /  
  
# docker entrypoint/cmd configuration  
COPY files/docker-entrypoint.sh /usr/local/bin/  
RUN ln \  
\--symbolic \  
\--force \  
usr/local/bin/docker-entrypoint.sh \  
/ # backwards compatibity  
RUN mkdir --parents /docker-entrypoint-initdb.d  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["mysqld"]  
VOLUME ["/var/lib/mysql", "/var/log/mysql"]  


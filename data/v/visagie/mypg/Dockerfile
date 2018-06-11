FROM ubuntu:latest  
  
LABEL maintainer="Johann Visagie <johann@visagie.za.net>"  
  
RUN set -x \  
&& apt-get -y update \  
&& apt-get install -y --no-install-recommends ca-certificates \  
build-essential \  
bzip2 \  
curl libcurl4-openssl-dev \  
git \  
gosu \  
libldap-dev \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
locales \  
openssl \  
python3 \  
python3-dev \  
python3-pip \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
ENV LANG="en_US.utf8" \  
PG_MAJOR="10" \  
PG_VERSION="10.3" \  
PGHTTP_VERSION="1.2.2" \  
PGDATA="/data" \  
POSTGRES_USER="postgres" \  
POSTGRES_GROUP="postgres" \  
PYTHON="/usr/bin/python3"  
RUN mkdir /src \  
&& curl -s \  
https://ftp.postgresql.org/pub/source/v${PG_VERSION}/postgresql-${PG_VERSION}.tar.bz2
\  
| tar xvjC /src \  
&& cd /src/postgresql-${PG_VERSION} \  
&& ./configure \  
\--with-openssl \  
\--with-libxml \  
\--enable-thread-safety \  
\--with-python \  
\--with-ldap \  
\--prefix=/usr/local \  
&& make install \  
&& make install -C contrib/adminpack \  
&& make install -C contrib/pgcrypto  
  
RUN curl -sL \  
https://github.com/pramsey/pgsql-http/archive/v${PGHTTP_VERSION}.tar.gz \  
| tar xvzC /src \  
&& cd /src/pgsql-http-${PGHTTP_VERSION} \  
&& make install  
  
COPY requirements.txt entrypoint.sh /  
  
RUN pip3 install --upgrade --no-cache-dir pip setuptools wheel \  
&& pip3 install --no-cache-dir -r /requirements.txt  
  
RUN git clone https://github.com/wjv/Multicorn.git -b nocache /src/Multicorn \  
&& cd /src/Multicorn \  
&& make install  
  
RUN groupadd -r "${POSTGRES_GROUP}" \--gid=999 && useradd -r -g
"${POSTGRES_GROUP}" \--uid=999 "${POSTGRES_USER}"  
  
RUN sed -i -e '/^xterm/{' -e 'n; s/^/#/' -e '}' /root/.bashrc  
  
ARG MYPG_DEBUG  
  
RUN if [ -z "${MYPG_DEBUG}" ]; then \  
apt-get purge -y --auto-remove ca-certificates \  
build-essential \  
bzip2 \  
curl \  
git \  
&& rm -rf /src /requirements.txt; \  
fi  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["postgres"]  
  
EXPOSE 5432  
HEALTHCHECK \--interval=5m --timeout=5s --retries=3 \  
CMD gosu postgres pg_ctl -D /data status  


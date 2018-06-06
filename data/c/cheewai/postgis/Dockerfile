FROM postgres:10.1  
LABEL maintainer "Cheewai Lai <clai@csir.co.za>"  
# Subscribe to pgsql-pkg-debian@postgresql.org for release announcements  
# and watch https://github.com/docker-library/postgres Dockerfile  
ARG POSTGIS_MAJOR=2.4  
  
ENV LANG en_ZA.UTF-8  
ENV LANGUAGE en_ZA.UTF-8  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \  
postgis-$POSTGIS_MAJOR \  
locales \  
rsyslog \  
curl \  
pgbouncer \  
wget \  
&& echo "deb [arch=amd64] http://packages.2ndquadrant.com/pglogical/apt/
`lsb_release -cs`-2ndquadrant main" >/etc/apt/sources.list.d/2ndquadrant.list
\  
&& wget \--quiet -O -
http://packages.2ndquadrant.com/pglogical/apt/AA7A6805.asc | apt-key add \- \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends postgresql-$PG_MAJOR-pglogical
\  
&& sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \  
&& sed -i -e 's/# en_ZA.UTF-8 UTF-8/en_ZA.UTF-8 UTF-8/' /etc/locale.gen \  
&& echo 'LANG="en_ZA.UTF-8"'>/etc/default/locale \  
&& dpkg-reconfigure locales \  
&& update-locale LANG=en_ZA.UTF-8 \  
&& dpkg-reconfigure locales \  
&& rm -rf /var/lib/apt/lists/*  
  
# Entrypoint script sets UID/GID of postgres user  
ADD set-postgres-uid.sh /set-postgres-uid.sh  


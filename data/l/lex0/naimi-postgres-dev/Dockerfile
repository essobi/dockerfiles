FROM partlab/ubuntu  
  
MAINTAINER Amangeldy Kadyl <lex0.kz@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LANG ru_RU.UTF-8  
ENV PG_VERSION 9.5  
RUN set -x \  
&& locale-gen $LANG \  
&& locale-gen $LANG \  
&& update-locale LANG=$LANG  
  
RUN set -x \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' \  
| tee /etc/apt/sources.list.d/postgresql.list \  
&& apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
postgresql-$PG_VERSION postgresql-client-$PG_VERSION postgresql-
contrib-$PG_VERSION \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& update-rc.d -f postgresql disable  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY conf /etc/postgresql/$PG_VERSION/main  
  
RUN set -x \  
&& chown -R postgres:postgres /etc/postgresql \  
&& chmod +x /usr/local/bin/entrypoint.sh  
  
VOLUME ["/var/lib/postgresql"]  
  
EXPOSE 5432  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  


FROM postgres:9.6  
  
RUN echo "Asia/Yekaterinburg" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \  
&& echo 'LANG="en_US.UTF-8"' > /etc/default/locale \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG=en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq \  
&& apt-get install -yq --no-install-recommends \  
postgresql-plperl-9.6 \  
python-software-properties \  
software-properties-common \  
postgresql-9.6-pgq3 \  
skytools3 \  
skytools3-ticker \  
libpq-dev \  
postgresql-server-dev-9.6 \  
postgresql-common \  
wget \  
unzip \  
make \  
build-essential \  
libssl-dev \  
libkrb5-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& truncate -s 0 /var/log/*log  
  
RUN echo "plperl.on_init = 'use utf8; use re; package utf8; require
\"utf8_heavy.pl\";'" >> /usr/share/postgresql/postgresql.conf.sample  
  
RUN wget https://github.com/omniti-labs/pg_jobmon/archive/v1.3.3.zip \  
&& unzip v1.3.3.zip \  
&& make -C pg_jobmon-1.3.3 \  
&& make NO_BGW=1 install -C pg_jobmon-1.3.3 \  
&& rm v1.3.3.zip \  
&& rm -rf pg_jobmon-1.3.3  
  
RUN wget https://github.com/keithf4/pg_partman/archive/v3.1.0.zip \  
&& unzip v3.1.0.zip \  
&& make -C pg_partman-3.1.0 \  
&& make install -C pg_partman-3.1.0 \  
&& rm v3.1.0.zip \  
&& rm -rf pg_partman-3.1.0  
  
RUN wget https://github.com/postgrespro/pg_pathman/archive/1.4.5.zip \  
&& unzip 1.4.5.zip \  
&& make -C pg_pathman-1.4.5 install USE_PGXS=1 \  
&& rm 1.4.5.zip \  
&& rm -rf pg_pathman-1.4.5 \  
&& echo "shared_preload_libraries='pg_pathman'" >>
/usr/share/postgresql/postgresql.conf.sample  
  
ENV PATH /usr/bin:$PATH  
  
COPY initdb.sh /docker-entrypoint-initdb.d/  


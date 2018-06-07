FROM kippchicago/idea2-cron  
MAINTAINER Chris Haid <chaid@kippchicago.org>  
#install python3  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# runtime dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
libexpat1 \  
libffi6 \  
libgdbm3 \  
libreadline7 \  
libsqlite3-0 \  
libssl1.0.0 \  
netbase \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
ENV PYTHON_VERSION 3.6.5  
  
RUN set -ex \  
&& buildDeps=" \  
dpkg-dev \  
gcc \  
libbz2-dev \  
libc6-dev \  
libexpat1-dev \  
libffi-dev \  
libgdbm-dev \  
liblzma-dev \  
libncursesw5-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
make \  
tcl-dev \  
tk-dev \  
wget \  
xz-utils \  
zlib1g-dev \  
# as of Stretch, "gpg" is no longer included by default  
$(command -v gpg > /dev/null || echo 'gnupg dirmngr') \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
# && export GNUPGHOME="$(mktemp -d)" \  
# && for server in $(shuf -e pgp.mit.edu \  
# hkp://p80.pool.sks-keyservers.net:80 \  
# keyserver.ubuntu.com \  
# hkp://keyserver.ubuntu.com:80 \  
# ha.pool.sks-keyservers.net) ; do \  
# gpg --keyserver "$server" --recv-keys "$GPG_KEY" && break || : ; \  
# done \  
#&& gpg --batch --verify python.tar.xz.asc\  
# && rm -r "$GNUPGHOME" \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--with-system-expat \  
\--with-system-ffi \  
\--without-ensurepip \  
&& make -j "$(nproc)" \  
&& make install \  
&& ldconfig \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
\  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 10.0.1  
  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends wget; \  
rm -rf /var/lib/apt/lists/*; \  
\  
wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \  
\  
apt-get purge -y --auto-remove wget; \  
\  
python get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
"pip==$PYTHON_PIP_VERSION" \  
; \  
pip --version; \  
\  
find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' +; \  
rm -f get-pip.py  
  
  
  
  
  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
# Airflow  
ARG AIRFLOW_VERSION=1.9.0  
ARG AIRFLOW_HOME=/etc/airflow  
  
#Postgres  
ENV POSTGRES_HOST=postgres  
ENV POSTGRES_PORT=5432  
ENV POSTGRES_USER=airflow  
ENV POSTGRES_PASSWORD=airflow  
ENV POSTGRES_DB=airflow  
  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
  
RUN set -ex \  
&& buildDeps=' \  
python3-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
libblas-dev \  
liblapack-dev \  
libpq-dev \  
git \  
' \  
&& apt-get update -yqq \  
&& apt-get upgrade -yqq \  
&& apt-get install -yqq --no-install-recommends \  
$buildDeps \  
python3-pip \  
python3-requests \  
python3-setuptools \  
#mysql-client \  
#mysql-server \  
#libmysqlclient-dev \  
apt-utils \  
curl \  
rsync \  
netcat \  
locales \  
vim  
RUN sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
&& useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& pip install -U pip setuptools wheel\  
#&& pip install --upgrade setuptools \  
&& pip install Cython \  
&& pip install pytz \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install apache-
airflow[crypto,celery,postgres,hdfs,jdbc]==$AIRFLOW_VERSION \  
&& pip install 'sqlalchemy>=1.1.15, <1.2.0' \  
&& pip install oauth2client gcloud retrying python-dateutil ConfigParser \  
&& pip install celery[redis]==4.0.2  
RUN apt-get purge --auto-remove -yqq $buildDeps \  
&& apt-get autoremove -yqq --purge \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
COPY entrypoint.sh /entrypoint.sh  
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg  
  
# COPY supervisrd.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# add jobs  
COPY ./jobs /jobs  
  
# Need to copy datarobot helpers to site-packages  
#RUN mkdir /usr/local/lib/python3.6/site-packages  
RUN mv /jobs/silo/powerschool/datarobot_helpers /usr/local/lib/python3.6/site-
packages/datarobot_helpers  
  
RUN mkdir /var/log/airflow  
RUN mkdir /etc/airflow/dags  
  
# add dags  
COPY ./dags /etc/airflow/dags  
  
# This next line is necessary to get everything up and running nicely.  
# Dags need to be in the dag folder for the scheduler, db, and webserver to
paly nicely  
#RUN cp -rf /usr/local/lib/python2.7/dist-packages/airflow/example_dags/*
${AIRFLOW_HOME}/dags/  
RUN chown -R airflow: ${AIRFLOW_HOME}  
RUN chown -R airflow: /etc/supervisor/  
RUN chown -R airflow: /var/log/  
#RUN chown -R airflow: /jobs  
RUN chmod -R a+rw /jobs  
#add  
RUN echo 'airflow ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers  
  
EXPOSE 8080  
#ENV FERNET_KEY=kYaLE7G8dtKsVMfoIuXGl2kLvvDOzkEg0lI9ssKy7N4=  
  
USER airflow  
WORKDIR ${AIRFLOW_HOME}  
ENTRYPOINT ["/entrypoint.sh"]  
#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  


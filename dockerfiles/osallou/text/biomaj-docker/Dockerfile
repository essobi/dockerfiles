FROM debian:jessie

WORKDIR /root
ENV "BIOMAJ_CONFIG=/root/config.yml"
ENV "prometheus_multiproc_dir=/tmp/biomaj-prometheus-multiproc"
RUN rm -rf /tmp/biomaj-prometheus-multiproc
RUN mkdir -p /tmp/biomaj-prometheus-multiproc

RUN apt-get update
RUN apt-get install -y apt-transport-https curl libcurl4-openssl-dev python3-pycurl python3-pip git unzip bzip2 ca-certificates --no-install-recommends

# Install docker to allow docker execution from process-message
RUN buildDeps='gnupg2' \
    && set -x \
    && apt-get install -y $buildDeps --no-install-recommends \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && echo "deb https://apt.dockerproject.org/repo debian-jessie main" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y docker-engine \
    && apt-get purge -y --auto-remove $buildDeps

RUN git clone -b develop https://github.com/genouest/biomaj-core.git
RUN pip3 install setuptools --upgrade

RUN git clone https://github.com/genouest/biomaj-zipkin.git

RUN git clone https://github.com/genouest/biomaj-user.git

RUN git clone https://github.com/genouest/biomaj-cli.git

RUN git clone https://github.com/genouest/biomaj-process.git

RUN git clone https://github.com/genouest/biomaj-download.git

RUN git clone -b develop https://github.com/genouest/biomaj.git && echo "Install biomaj"

RUN git clone https://github.com/genouest/biomaj-daemon.git && echo "Install daemon"

RUN git clone -b develop https://github.com/genouest/biomaj-watcher.git && echo "Install biomaj-watcher"

RUN git clone https://github.com/genouest/biomaj-ftp.git

ENV "BIOMAJ_CONFIG=/etc/biomaj/config.yml"
RUN mkdir -p /var/log/biomaj

RUN buildDeps='gcc python3-dev protobuf-compiler' \
    && set -x \
    && apt-get install -y $buildDeps --no-install-recommends \
    && cd /root/biomaj-core && python3 setup.py install \
    && cd /root/biomaj-zipkin && python3 setup.py install \
    && cd /root/biomaj-user && python3 setup.py install \
    && cd /root/biomaj-cli && python3 setup.py install \
    && cd /root/biomaj-process/biomaj_process/message && protoc --python_out=. message.proto \
    && cd /root/biomaj-process && python3 setup.py install \
    && cd /root/biomaj-download/biomaj_download/message && protoc --python_out=. message.proto \
    && cd /root/biomaj-download && python3 setup.py install \
    && cd /root/biomaj && python3 setup.py install \
    && cd /root/biomaj-daemon && python3 setup.py install \
    && cd /root/biomaj-watcher && python3 setup.py develop \
    && cd /root/biomaj-ftp && python3 setup.py install \
    && pip3 install gunicorn \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove $buildDeps

RUN pip3 install graypy

RUN mkdir -p /var/lib/biomaj/data

COPY biomaj-config/config.yml /etc/biomaj/config.yml
COPY biomaj-config/global.properties /etc/biomaj/global.properties
COPY biomaj-config/production.ini /etc/biomaj/production.ini
COPY biomaj-config/gunicorn_conf.py /etc/biomaj/gunicorn_conf.py
COPY watcher.sh /root/watcher.sh

# Local test configuration
RUN mkdir -p /etc/biomaj/conf.d
RUN mkdir -p /var/log/biomaj
RUN mkdir -p /etc/biomaj/process.d
RUN mkdir -p /var/cache/biomaj
RUN mkdir -p /var/run/biomaj
COPY test-local/etc/biomaj/global_local.properties /etc/biomaj/global_local.properties
COPY test-local/etc/biomaj/conf.d/alu.properties /etc/biomaj/conf.d/alu.properties

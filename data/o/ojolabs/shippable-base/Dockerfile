FROM ubuntu:14.04.3  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
  
RUN locale-gen en_US en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
RUN apt-get update && \  
apt-get install -y \  
software-properties-common \  
build-essential \  
wget \  
git-core \  
ca-certificates \  
curl \  
python-pip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install virtualenv && \  
pip install awscli==1.7.20 && \  
pip install glob2==0.4.1 && \  
pip install pika==0.9.14  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# ==== RabbitMQ ====  
RUN apt-add-repository 'deb http://www.rabbitmq.com/debian/ testing main' && \  
wget --quiet -O - https://www.rabbitmq.com/rabbitmq-signing-key-public.asc |
apt-key add - && \  
apt-get update && \  
apt-get install --no-install-recommends -y rabbitmq-server && \  
rm -rf /var/lib/apt/lists/*  
RUN echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config  
# add a symlink to the .erlang.cookie in /root so we can "docker exec
rabbitmqctl ..." without gosu  
RUN ln -sf /var/lib/rabbitmq/.erlang.cookie /root/  
# ==== Java ====  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION=20140324  
  
RUN add-apt-repository -y ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk && \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure && \  
rm -rf /var/lib/apt/lists/*  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
# ==== PostgreSQL ====  
ENV PG_MAJOR 9.4  
ENV PG_VERSION 9.4.4-1.pgdg80+1  
ENV POSTGIS_VERSION 2.1  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r postgres && useradd -r -g postgres postgres  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
  
RUN apt-add-repository 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-
pgdg main' && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update && \  
apt-get install -y postgresql-common && \  
sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf && \  
apt-get install -y \  
postgresql-$PG_MAJOR \  
postgresql-contrib-$PG_MAJOR \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION \  
postgis && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
RUN mkdir -p /utils  
COPY /utils/* /utils/  
  
CMD ["/bin/bash"]


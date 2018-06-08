# VERSION 1.9.0-1  
# AUTHOR: Matthieu "Puckel_" Roisil  
# DESCRIPTION: Basic Airflow container  
# BUILD: docker build --rm -t puckel/docker-airflow .  
# SOURCE: https://github.com/puckel/docker-airflow  
  
FROM python:3.6-slim  
LABEL MAINTAINER=zhongjiajie955@hotmail.com  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
# Airflow  
ARG AIRFLOW_VERSION=1.9.0  
ARG AIRFLOW_HOME=/usr/local/airflow  
  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
# Oracle client base  
ENV ORACLE_INSTANTCLIENT_MAJOR 12.2  
ENV ORACLE_INSTANTCLIENT_VERSION 12.2.0.1.0  
ENV ORACLE /usr/lib/oracle  
ENV ORACLE_HOME $ORACLE/$ORACLE_INSTANTCLIENT_MAJOR/client64  
  
# Java  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# beeline  
ENV BEELINE_HOME /usr/local/beeline  
ENV HIVE_VERSION 1.2.0  
COPY beeline $BEELINE_HOME  
  
RUN set -ex \  
&& buildDeps=' \  
python3-dev \  
libkrb5-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
libblas-dev \  
liblapack-dev \  
libpq-dev \  
git \  
alien \  
gcc \  
' \  
# only need in dev env  
&& testDeps=' \  
iputils-ping \  
telnet \  
wget \  
vim \  
sudo \  
ssh \  
' \  
# add Oracle java ppa and key  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
\  
&& apt-get update -yqq \  
# install oracle java  
# https://stackoverflow.com/a/46815898/7152658  
# https://ubuntuforums.org/showthread.php?t=2374686&page=4  
&& mkdir -p /usr/share/man/man1/ \  
&& echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections \  
&& echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections \  
&& (apt-get install -yqq --no-install-recommends --force-yes oracle-
java8-installer oracle-java8-set-default || (true \  
&& cd /var/lib/dpkg/info \  
&& sed -i 's|JAVA_VERSION=8u151|JAVA_VERSION=8u162|' oracle-java8-installer.*
\  
&& sed -i 's|PARTNER_URL=http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/|PARTNER_URL=http://download.oracle.com/otn-
pub/java/jdk/8u162-b12/0da788060d494f5095bf8624735fa2f1/|' oracle-
java8-installer.* \  
&& sed -i
's|SHA256SUM_TGZ="c78200ce409367b296ec39be4427f020e2c585470c4eed01021feada576f027f"|SHA256SUM_TGZ="68ec82d47fd9c2b8eb84225b6db398a72008285fafc98631b1ff8d2229680257"|'
oracle-java8-installer.* \  
&& sed -i 's|J_DIR=jdk1.8.0_151|J_DIR=jdk1.8.0_162|' oracle-java8-installer.*
\  
&& apt-get install -yqq --no-install-recommends --force-yes oracle-
java8-installer oracle-java8-set-default)) \  
\  
&& apt-get install -yqq --no-install-recommends \  
$buildDeps \  
$testDeps \  
python3-pip \  
python3-requests \  
apt-utils \  
curl \  
rsync \  
netcat \  
locales \  
libsasl2-dev \  
# https://github.com/dropbox/PyHive/issues/161  
libsasl2-modules \  
libmysqlclient-dev \  
libaio1 \  
# install oracle db basic  
# todo last to change baidu yun pan  
&& curl -L https://github.com/sergeymakinen/docker-oracle-instant-
client/raw/assets/oracle-instantclient$ORACLE_INSTANTCLIENT_MAJOR-
basic-$ORACLE_INSTANTCLIENT_VERSION-1.x86_64.rpm -o /oracle-basic.rpm \  
&& curl -L https://github.com/sergeymakinen/docker-oracle-instant-
client/raw/assets/oracle-instantclient$ORACLE_INSTANTCLIENT_MAJOR-
devel-$ORACLE_INSTANTCLIENT_VERSION-1.x86_64.rpm -o /oracle-devel.rpm \  
&& alien -i /oracle*.rpm \  
&& echo "$ORACLE_HOME/lib/" > /etc/ld.so.conf.d/oracle.conf \  
&& ldconfig \  
\  
# pypi tsinghua  
# && mkdir -p ~/.config/pip \  
# && echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" >>
~/.config/pip/pip.conf \  
\  
# install beeline  
# https://github.com/sutoiku/docker-beeline  
&& mkdir -p $BEELINE_HOME/lib $BEELINE_HOME/conf \  
&& echo "$HIVE_VERSION" > $BEELINE_HOME/lib/hive.version \  
&& (curl -L https://s3.amazonaws.com/stoic-public/hive-
beeline-1.2.0-fetchSize.jar -o $BEELINE_HOME/lib/hive-
beeline-1.2.0-fetchSize.jar || curl -L
http://central.maven.org/maven2/org/apache/hive/hive-
beeline/$HIVE_VERSION/hive-beeline-$HIVE_VERSION.jar -o
$BEELINE_HOME/lib/hive-beeline-$HIVE_VERSION.jar) \  
&& curl -L http://central.maven.org/maven2/org/apache/hive/hive-
jdbc/$HIVE_VERSION/hive-jdbc-$HIVE_VERSION-standalone.jar -o
$BEELINE_HOME/lib/hive-jdbc-$HIVE_VERSION-standalone.jar \  
&& curl -L http://central.maven.org/maven2/commons-cli/commons-
cli/1.2/commons-cli-1.2.jar -o $BEELINE_HOME/lib/commons-cli-1.2.jar \  
&& curl -L http://central.maven.org/maven2/org/apache/hadoop/hadoop-
common/2.7.3/hadoop-common-2.7.3.jar -o $BEELINE_HOME/lib/hadoop-
common-2.7.3.jar \  
&& curl -L http://central.maven.org/maven2/jline/jline/2.12/jline-2.12.jar -o
$BEELINE_HOME/lib/jline-2.12.jar \  
&& curl -L http://central.maven.org/maven2/net/sf/supercsv/super-
csv/2.2.0/super-csv-2.2.0.jar -o $BEELINE_HOME/lib/super-csv-2.2.0.jar \  
&& ln -s $BEELINE_HOME/beeline /usr/bin/beeline \  
&& chmod +x /usr/bin/beeline \  
\  
&& sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
&& useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& echo "airflow:airflow" | chpasswd \  
&& adduser airflow sudo \  
&& python -m pip install -U pip setuptools wheel \  
&& pip install Cython \  
&& pip install pytz \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install apache-
airflow[crypto,celery,postgres,hive,jdbc]==$AIRFLOW_VERSION \  
&& pip install celery[redis]==4.0.2 \  
&& pip install mysqlclient cx_Oracle paramiko\  
# import thrift_sasl usually fail, impyla need specific versions libraries  
# thrift<=0.10.0 thrift_sasl<=0.2.1 sasl<=0.2.1 impyla<=0.14.0  
# https://github.com/cloudera/impyla/issues/268  
# https://stackoverflow.com/questions/46573180/impyla-0-14-0-error-tsocket-
object-has-no-attribute-isopen  
&& pip install thrift==0.9.3 thrift_sasl==0.2.1 \  
# && (pip uninstall -y thrift_sasl thrift sasl six && pip install
thrift_sasl==0.2.1 thrift==0.10.0) \  
# && apt-get purge --auto-remove -yqq $buildDeps \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base \  
/oracle*.rpm \  
/var/cache/oracle-jdk8-installer  
  
COPY script/entrypoint.sh /entrypoint.sh  
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg  
  
RUN chown -R airflow: ${AIRFLOW_HOME}  
  
EXPOSE 8080 5555 8793  
  
USER airflow  
WORKDIR ${AIRFLOW_HOME}  
  
# gen ssh-key  
# RUN mkdir -p $AIRFLOW_HOME/.ssh \  
# && ssh-keygen -f '$AIRFLOW_HOME/.ssh/id_rsa' -t rsa -N '' -C
"airflow@airflow.com"  
  
ENTRYPOINT ["/entrypoint.sh"]


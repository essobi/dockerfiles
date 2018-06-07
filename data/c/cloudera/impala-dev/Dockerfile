FROM ubuntu:14.04  
COPY container_root/bin/docker-boot /bin/  
COPY container_root/bin/docker-boot-daemon /bin/  
COPY container_root/bin/docker-ip /bin/  
COPY container_root/tmp /tmp/  
  
# Set bash as the default shell. Some impala scripts require bash and by
default  
# RUN uses /bis/sh which is dash.  
RUN unlink /bin/sh && ln -s /bin/bash /bin/sh  
  
ENV HOSTNAME localhost  
  
RUN apt-get update  
  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:git-core/ppa  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN add-apt-repository -y ppa:bitcoin/bitcoin  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | \  
debconf-set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | \  
debconf-set-selections  
RUN apt-get update  
  
RUN apt-get install -y \  
ant \  
apt-file \  
automake \  
bash-completion \  
bison \  
cmake \  
curl \  
distcc \  
emacs \  
flex \  
g++ \  
gdb \  
git \  
groff \  
inetutils-ping \  
ipython \  
libbz2-dev \  
libdb4.8-dev \  
libevent1-dev \  
libldap2-dev \  
liblzo2-dev \  
libsasl2-dev \  
libssl-dev \  
libtool \  
lsb-release \  
lsof \  
lzop \  
make \  
man \  
maven \  
net-tools \  
openssh-client \  
openssh-server \  
oracle-jdk7-installer \  
pkg-config \  
postgresql \  
postgresql-server-dev-9.3 \  
psmisc \  
pypy \  
python-dev \  
python-pip \  
python-setuptools \  
subversion \  
sudo \  
tmux \  
vim \  
wget \  
zlib1g-dev \  
zsh  
# Workaround https://github.com/docker/docker/issues/783  
RUN mkdir /etc/ssl/private-copy \  
&& mv /etc/ssl/private/* /etc/ssl/private-copy/ \  
&& rm -rf /etc/ssl/private \  
&& mv /etc/ssl/private-copy /etc/ssl/private \  
&& chmod -R 0700 /etc/ssl/private \  
&& chown -R postgres /etc/ssl/private  
  
RUN update-alternatives --set java /usr/lib/jvm/java-7-oracle/jre/bin/java  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
RUN easy_install -U setuptools  
RUN pip install git-review  
  
RUN locale-gen en_US en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
RUN echo 'America/Los_Angeles' > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
ENV SUDO_GROUP sudo  
  
RUN sed -i "s:#listen_addresses = 'localhost':listen_addresses = '*':g" \  
/etc/postgresql/*/main/postgresql.conf  
RUN sed -i s:peer:trust:g /etc/postgresql/*/main/pg_hba.conf  
RUN sed -i s:md5:trust:g /etc/postgresql/*/main/pg_hba.conf  
RUN sed -i s:127.0.0.1/32:0.0.0.0/0:g /etc/postgresql/*/main/pg_hba.conf  
RUN service postgresql start \  
&& sleep 5 \  
&& sudo -u postgres psql -c " \  
CREATE ROLE hiveuser LOGIN PASSWORD 'password'; \  
ALTER ROLE hiveuser WITH CREATEDB;"  
  
RUN echo root:cloudera | chpasswd  
  
ENV BASH_COMPLETION /etc/bash_completion  
  
CMD /bin/docker-boot-daemon  
  
RUN sed -i s:###JAVA_HOME###:$JAVA_HOME: /tmp/home/dev/.{bash,zsh}rc  
RUN sed -i s:###BASH_COMPLETION###:$BASH_COMPLETION: /tmp/home/dev/.bashrc  
RUN /tmp/setup-users setup_user dev  
  
RUN mkdir -p /var/lib/hadoop-hdfs  
RUN chown dev /var/lib/hadoop-hdfs  
  
ENV IMPALA_TOOLACHAIN /opt/Impala-Toolchain  
RUN mkdir -p $IMPALA_TOOLACHAIN  
RUN chmod 777 $IMPALA_TOOLACHAIN  
  
USER dev  
WORKDIR /home/dev  
RUN /tmp/git-clone-retry https://github.com/cloudera/Impala.git  
RUN /tmp/git-clone-retry https://github.com/cloudera/impala-lzo.git Impala-lzo  
RUN /tmp/git-clone-retry https://github.com/cloudera/hadoop-lzo.git  
RUN for DIR in Impala Impala-lzo; do \  
curl -o $DIR/.git/hooks/commit-msg \  
http://gerrit.cloudera.org:8080/tools/hooks/commit-msg \  
&& chmod +x $DIR/.git/hooks/commit-msg; \  
done  
ENV IMPALA_HOME /home/dev/Impala  
ENV USER dev  


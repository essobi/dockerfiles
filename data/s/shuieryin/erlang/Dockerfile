FROM centos:latest  
  
MAINTAINER Shuieryin <shuieryin@gmail.com>  
  
ENV container docker  
ENV OTP_VERSION=19.2 \  
EPEL_VERSION=7-8 \  
REDIS_VERSION=3.2.6 \  
ERLANG_SOLUTION_VERSION=1.0-1 \  
INSTALLATION_PATH=/root/installation \  
TOOLS_PATH=/root/tools  
  
LABEL "version"="${OTP_VERSION}" \  
"description"="This is a clean erlang otp image." \  
"author"="Shuieryin"  
  
#Install erlang and update yum  
WORKDIR ${INSTALLATION_PATH}  
RUN yum install -y man wget ;\  
wget http://packages.erlang-solutions.com/erlang-
solutions-${ERLANG_SOLUTION_VERSION}.noarch.rpm ;\  
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-${EPEL_VERSION}.noarch.rpm ;\  
rpm -Uvh erlang-solutions-${ERLANG_SOLUTION_VERSION}.noarch.rpm ;\  
rpm --import https://packages.erlang-solutions.com/rpm/erlang_solutions.asc ;\  
rpm -Uvh epel-release-${EPEL_VERSION}.noarch.rpm ;\  
yum update -y ;\  
yum install -y gcc \  
glibc-devel \  
make \  
autoconf \  
libGL \  
libGLU \  
unixODBC \  
wxGTK \  
wxGTK-gl \  
git \  
erlang  
  
WORKDIR ${TOOLS_PATH}  
  
#Install redis  
RUN cd ${TOOLS_PATH} ;\  
wget http://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz ;\  
tar xzf redis-${REDIS_VERSION}.tar.gz ;\  
cd redis-${REDIS_VERSION} ;\  
make ;\  
cd .. ;\  
rm redis-${REDIS_VERSION}.tar.gz ;\  
ln -s ${TOOLS_PATH}/redis-${REDIS_VERSION}/src/redis-server /usr/bin/redis-
server ;\  
ln -s ${TOOLS_PATH}/redis-${REDIS_VERSION}/src/redis-cli /usr/bin/redis-cli  
  
#Set volume for systemd  
VOLUME ["/sys/fs/cgroup"]  
  
#Fix LC_CTYPE  
RUN echo LC_CTYPE=\"en_US.UTF-8\" >> /etc/locale.conf  
  
#Install development tools  
#After sshd is installed, need to init root password in order to let ssh to
connect  
RUN yum install -y vim \  
net-tools \  
initscripts \  
passwd \  
openssh-server \  
openssh-clients  
  
#Remove installation files  
RUN rm -rf ${INSTALLATION_PATH}/* ;\  
yum clean all  
  
CMD ["/usr/sbin/init"]  
#Create container  
# docker run --privileged -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro
--name=erlang -p [port]:22 shuieryin/erlang  
#Change root password  
# docker exec -ti erlang passwd  


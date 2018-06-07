FROM centos:centos7  
  
RUN yum update -y  
  
RUN echo "===> Install the basics..." && \  
yum remove -y iputils && \  
yum update -y && \  
yum install -y \  
autoconf \  
bc \  
binutils-devel \  
bzip2 \  
curl-devel \  
expat-devel \  
elfutils-libelf-devel \  
fuse \  
fuse-devel \  
gettext \  
gcc \  
gcc-c++ \  
git \  
hmaccalc \  
libibverbs-utils \  
libibverbs-devel \  
libipathverbs \  
make \  
ncurses-devel \  
openssh-client \  
openssh-server \  
openssl-devel \  
perl-devel \  
readline-devel \  
sudo \  
tar \  
wget \  
zlib-devel && \  
yum groupinstall -y --setopt=group_package_types=optional "Infiniband Support"
"Development Tools" && \  
yum clean -y all || true  
  
RUN echo "===> Install samtools..." && \  
wget
https://github.com/samtools/samtools/releases/download/1.3/samtools-1.3.tar.bz2
&& \  
tar xjf samtools-1.3.tar.bz2 && \  
cd samtools-1.3 && \  
make && \  
make install  
  
RUN echo "===> Make users and add tty for sudo..." && \  
groupadd fuse && \  
usermod -a -G fuse root && \  
sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers  
  
RUN echo "Setup limits for infiniband" && \  
echo "* soft memlock unlimited" >> /etc/security/limits.conf && \  
echo "* hard memlock unlimited" >> /etc/security/limits.conf  
  
RUN echo "===> Install GassNET for infiniband..." && \  
cd /tmp && \  
curl -O https://gasnet.lbl.gov/GASNet-1.26.0.tar.gz && \  
tar xzvf GASNet-1.26.0.tar.gz && \  
cd GASNet-1.26.0 && \  
./configure \  
\--prefix=/usr \  
\--enable-udp \  
\--enable-ibv \  
\--disable-mpi \  
\--enable-par \  
\--enable-segment-fast \  
\--disable-aligned-segments \  
\--disable-pshm \  
\--with-segment-mmap-max=160GB && \  
make -j4 && \  
sudo make install  
  
# * modify sshd conf  
# * workaround for the way ubuntu deals with env for sudo  
# * create expected dirs/links  
RUN sed -i "s/UsePAM.*/UsePAM yes/" /etc/ssh/sshd_config && \  
sed -i "s/AcceptEnv LANG LC_*/#AcceptEnv LANG LC_*/" /etc/ssh/sshd_config && \  
echo "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:" >
/etc/environment && \  
echo "alias sudo='sudo env PATH=\$PATH'" >> /etc/environment && \  
sed -i "s/Defaults.*env_reset//" /etc/sudoers && \  
sed -i "s/Defaults.*secure_path.*//" /etc/sudoers  
  
ADD entrypoint.sh /  
ADD configure_ssh.sh /  
RUN chmod 755 /entrypoint.sh /configure_ssh.sh  
ENTRYPOINT ["/entrypoint.sh"]  


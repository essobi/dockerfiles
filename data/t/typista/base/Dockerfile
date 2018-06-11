#http://qiita.com/hnakamur/items/0b72590136cece29faee  
FROM centos:centos6  
ENTRYPOINT /etc/entrypoint.sh  
RUN rm /etc/localtime && \  
ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock && \  
echo 'UTF="false"' >> /etc/sysconfig/clock && \  
source /etc/sysconfig/clock && \  
touch /etc/bashrc && \  
echo 'alias vi="vim"' >> /etc/bashrc && \  
touch /etc/skel/.bash_profile && \  
echo '# .bash_profile' >> /etc/skel/.bash_profile && \  
echo '# Get the aliases and functions' >> /etc/skel/.bash_profile && \  
echo 'if [ -f ~/.bashrc ]; then' >> /etc/skel/.bash_profile && \  
echo '. ~/.bashrc' >> /etc/skel/.bash_profile && \  
echo 'fi' >> /etc/skel/.bash_profile && \  
echo '# User specific environment and startup programs' >>
/etc/skel/.bash_profile && \  
echo 'PATH=$PATH:$HOME/bin' >> /etc/skel/.bash_profile && \  
echo 'export PATH' >> /etc/skel/.bash_profile && \  
cp /etc/skel/.bash_profile /root/ && \  
touch /etc/skel/.bashrc && \  
echo 'alias vi="vim"' >> /etc/skel/.bashrc && \  
cp /etc/skel/.bashrc /root/ && \  
source /root/.bashrc && \  
echo 'umask 002' >> /etc/skel/.bashrc && \  
touch /etc/skel/.vimrc && \  
echo 'set encoding=utf-8' >> /etc/skel/.vimrc && \  
echo 'set fileencodings=utf-8,iso-2022-jp,sjis,euc-jp' >> /etc/skel/.vimrc &&
\  
echo 'set tabstop=4' >> /etc/skel/.vimrc && \  
echo 'set paste' >> /etc/skel/.vimrc && \  
cp /etc/skel/.vimrc /root/ && \  
yum update -y && \  
yum install -y vim wget which git curl tar zip unzip bzip2 make zlib-devel
crontabs && \  
yum install -y wget openssl openssl-devel language-pack-ja gcc && \  
wget https://raw.githubusercontent.com/typista/docker-
base/master/files/entrypoint.sh -O /etc/entrypoint.sh && \  
chmod +x /etc/entrypoint.sh && \  
wget http://ftp.gnu.org/gnu/glibc/glibc-2.14.1.tar.gz -O
/root/glibc-2.14.1.tar.gz && \  
cd /root && \  
tar zvxf glibc-2.14.1.tar.gz && \  
mkdir -p /usr/glibc/etc/ && \  
touch /usr/glibc/etc/ld.so.conf && \  
cd glibc-2.14.1 && \  
mkdir build && cd $_ && \  
../configure --prefix=/usr/glibc && \  
make && \  
make install && \  
cd /usr/glibc/lib/ && \  
cp libc-2.14.1.so /lib64/ && \  
ln -nfs libc-2.14.1.so libc.so.6 && \  
ldconfig && \  
wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O
/etc/yum.repos.d/devtools-2.repo && \  
yum update -y && \  
yum install -y devtoolset-2-gcc devtoolset-2-binutils && \  
yum install -y devtoolset-2-gcc-c++ devtoolset-2-gcc-gfortran && \  
ln -s /opt/rh/devtoolset-2/root/usr/bin/* /usr/local/bin/ && \  
hash -r && \  
export LC_ALL=C && \  
echo 'LANG=C' > /etc/sysconfig/i18n  
  


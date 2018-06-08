FROM ghifari160/apache:16.04  
  
MAINTAINER Ghifari160 <ghifari160@ghifari160.com>  
  
# Disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt update && \  
# Install git  
apt install -y git git-man less libbsd0 libedit2 \  
liberror-perl libpopt0 libx11-6 libx11-data libxau6 libxcb1 \  
libxdmcp6 libxext6 libxmuu1 openssh-client patch rsync xauth make && \  
# Install build prerequisite  
apt install -y autoconf automake autotools-dev binutils \  
build-essential bzip2 cpp cpp-5 dpkg-dev fakeroot g++ g++-5 gcc \  
gcc-5 libalgorithm-diff-perl libalgorithm-diff-xs-perl \  
libalgorithm-merge-perl libasan2 libatomic1 libc-dev-bin \  
libc6-dev libcc1-0 libcilkrts5 libdpkg-perl libfakeroot \  
libfile-fcntllock-perl libgcc-5-dev libgomp1 libisl15 libitm1 liblsan0 \  
libltdl-dev libltdl7 libmpc3 libmpfr4 libmpx0 libquadmath0 libsigsegv2 \  
libstdc++-5-dev libtool libtsan0 libubsan0 linux-libc-dev m4 manpages \  
manpages-dev re2c icu-devtools libicu-dev libxml2-dev apache2-dev && \  
# Build and install Bison v2.7  
wget http://ftp.gnu.org/pub/gnu/bison/bison-2.7.tar.gz -O bison-2.7.tar.gz &&
\  
tar -xvzf bison-2.7.tar.gz && cd /bison-2.7 && ./configure \  
\--prefix=/usr/local/bison \  
\--with-libiconv-prefix=/usr/local/libiconv && \  
make && make install && export PATH=$PATH:/usr/local/bison/bin && \  
  
# Download PHP v5.5.38 source code  
cd / && \  
git clone -b PHP-5.5.38 --single-branch https://github.com/php/php-src.git &&
\  
# Build and install PHP v5.5.38  
cd /php-src && ./buildconf --force && \  
./configure --with-apxs2=/usr/bin/apxs2 --enable-maintainer-zts && \  
make && make install && \  
# Clean up build environment  
rm -rf /php-src/* /bison-2.7/* /bison-2.7.tar.gz && \  
# Uninstall build prerequisites  
apt remove --autoremove -y autoconf automake autotools-dev binutils \  
build-essential bzip2 cpp cpp-5 dpkg-dev fakeroot g++ g++-5 gcc gcc-5 m4 \  
manpages manpages-dev re2c icu-devtools libicu-dev libxml2-dev apache2-dev &&
\  
# Uninstall git  
apt remove --autoremove -y git less patch && \  
# Clean up APT  
apt clean && rm -rf /var/lib/apt/lists/* && \  
# Configure PHP  
wget
https://gist.githubusercontent.com/Ghifari160/bc9a6b56a12706bfeb1292380347cc51/raw/php.ini
-O /usr/local/lib/php.ini && \  
  
# Configure Apache2  
wget
https://gist.githubusercontent.com/Ghifari160/a5c8778c192c34363178a9dc065029f3/raw/php.conf
-O /etc/apache2/conf-available/php.conf && \  
a2enconf php  
  
# Add the custom default page  
RUN rm /var/www/html/index.html  
ADD index.php /var/www/html/index.php  


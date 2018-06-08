# memcached  
  
FROM takaomag/base:2018.03.07.00.25  
  
ENV \  
X_DOCKER_REPO_NAME=memcached \  
X_MEMCACHED_VERSION=1.5.6  
  
RUN \  
echo "2016-03-08-0" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
: && \  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
: && \  
# echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}"
&& \  
# pacman-key --refresh-keys && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
#: && \  
REQUIRED_PACKAGES=("memcached") && \  
: && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
: && \  
# REQUIRED_PACKAGES=("libevent") && \  
# echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
# sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_SUCCESS}" && \  
# echo -e "${FONT_INFO}[INFO] Install
memcached-${X_MEMCACHED_VERSION}${FONT_DEFAULT}" && \  
# cd /var/tmp && \  
# mkdir -p /var/tmp/memcached-${X_MEMCACHED_VERSION} && \  
# curl --silent --location --fail
"http://memcached.org/files/memcached-${X_MEMCACHED_VERSION}.tar.gz" | tar xz
-C memcached-${X_MEMCACHED_VERSION} \--strip-components=1 && \  
# cd memcached-${X_MEMCACHED_VERSION} && \  
# ./configure --prefix=/opt/local/memcached-${X_MEMCACHED_VERSION}
\--enable-64bit && \  
# make && \  
# porg -lD make install && \  
# cd ../ && \  
# rm -rf memcached-${X_MEMCACHED_VERSION} && \  
# cd /opt/local && \  
# ln -s memcached-${X_MEMCACHED_VERSION} memcached && \  
# getent group memcached >/dev/null || groupadd --system memcached && \  
# getent passwd memcached >/dev/null || useradd --system -c 'memcached' -g
memcached -d / -s /bin/bash memcached && \  
#: && \  
mkdir -p /run/memcached && \  
chown -R memcached:memcached /run/memcached && \  
chmod 755 /run/memcached && \  
# echo -e "${FONT_SUCCESS}[SUCCESS] Install
memcached-${X_MEMCACHED_VERSION}${FONT_SUCCESS}" && \  
: && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
EXPOSE \  
11211 \  
11211/udp  
  
VOLUME ["/run/memcached"]  
  
# ENTRYPOINT ["/opt/local/memcached/bin/memcached"]  
ENTRYPOINT ["/usr/bin/memcached"]  
  
# CMD ["-u", "memcached", "-l", "127.0.0.1", "-o",
"slab_reassign,slab_automove,lru_crawler,lru_maintainer,maxconns_fast,hash_algorithm=murmur3",
"-v"]  
CMD ["-u", "memcached", "-l", "127.0.0.1", "-o", "modern", "-v"]  


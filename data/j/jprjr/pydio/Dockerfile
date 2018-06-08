FROM jprjr/php-fpm  
  
MAINTAINER John Regan <john@jrjrtech.com>  
  
RUN pacman -Syy --noconfirm --quiet > /dev/null  
  
RUN pacman -S --noconfirm --quiet --needed rsync \  
git imagemagick ghostscript >/dev/null 2>/dev/null  
  
# install packer and build+install cool stuff  
RUN pacman -S --noconfirm --quiet --needed --asdeps base-devel jshon \  
expac cmake libgit2 >/dev/null 2>/dev/null  
  
RUN mkdir /tmp/packer && \  
cd /tmp/packer && \  
curl -R -L -O https://aur.archlinux.org/packages/pa/packer/PKGBUILD && \  
makepkg --asroot -i --noconfirm && \  
cd / && rm -rf /tmp/packer  
  
RUN packer -S --noconfirm --noedit \  
subversion pear-http-oauth \  
pear-mail-mimedecode pear-http-webdavclient \  
pecl-rsync  
  
RUN mkdir /tmp/php-libgit2-git && \  
cd /tmp/php-libgit2-git && \  
curl -R -L
https://gist.githubusercontent.com/jprjr/10287798/raw/fbee7bb2f7ebe70a4bfbd1d11c3729f1f4b73266/PKGBUILD+-+php-
libgit2-git > PKGBUILD && \  
makepkg --asroot -i --noconfirm && \  
cd / && rm -rf /tmp/php-libgit2-git  
  
RUN pear config-set preferred_state alpha && pear install VersionControl_Git
&& pear config-set preferred_state stable  
  
RUN pacman -Ru --noconfirm packer base-devel  
RUN pacman -R --noconfirm $(pacman -Qdtq)  
RUN paccache -rk0 && pacman -Scc --noconfirm  
RUN rm -rf /tmp/packer*  
RUN rm -rf /tmp/pear*  
  
RUN sed -i '/^file_uploads/c \  
file_uploads = On' /etc/php/php.ini  
  
RUN sed -i '/^post_max_size/c \  
post_max_size = 2G' /etc/php/php.ini  
  
RUN sed -i '/^upload_max_filesize/c \  
upload_max_filesize = 2G' /etc/php/php.ini  
  
RUN sed -i '/^max_file_uploads/c \  
max_file_uploads = 20000' /etc/php/php.ini  
  
RUN sed -i '/^output_buffering/c \  
output_buffering = Off' /etc/php/php.ini  
  
RUN sed -i '/^open_basedir/c \  
open_basedir =
/usr/share/webapps/pydio/:/tmp/:/usr/share/pear/:/var/lib/pydio/'
/etc/php/php.ini  
  
RUN echo "extension=rsync.so" >> /etc/php/php.ini  
RUN echo "extension=git2.so" >> /etc/php/php.ini  
  
RUN mkdir -p /usr/share/webapps && \  
mkdir -p /var/lib/pydio && \  
cd /usr/share/webapps && \  
curl -R -L \  
"http://downloads.sourceforge.net/project/ajaxplorer/pydio/stable-
channel/5.2.3/pydio-core-5.2.3.tar.gz" \  
| tar xz && \  
mv pydio-core-5.2.3/data /usr/share/webapps/pydio-data-5.2.3 && \  
ln -s /usr/share/webapps/pydio-core-5.2.3 /usr/share/webapps/pydio && \  
ln -s /var/lib/pydio/data /usr/share/webapps/pydio/data && \  
chown -R http:http /var/lib/pydio && \  
chown -R http:http /usr/share/webapps  
  
ADD init_data_folder.sh /opt/init_data_folder.sh  
RUN /opt/init_data_folder.sh  
  
# Volumes to export  
VOLUME /usr/share/webapps/pydio  
VOLUME /var/lib/pydio/data  
  
# Port 9000 (fastcgi) is implied by parent  
# WebSockets port  
EXPOSE 8090  


FROM jprjr/php-fpm  
  
USER root  
RUN pacman --sync --refresh --sysupgrade --ignore filesystem --noconfirm
--noprogressbar --quiet && pacman --sync --noconfirm --noprogressbar --quiet
fakeroot git go btrfs-progs bridge-utils  
RUN pacman --sync --noconfirm --noprogressbar --quiet base-devel  
  
# Build package from PKGBUILD  
RUN mkdir /http && chown http:http /http  
WORKDIR /http  
USER http  
RUN curl -sS https://aur.archlinux.org/packages/do/docker-git/docker-
git.tar.gz | tar -xz  
RUN sed '/patch/d' -i docker-git/PKGBUILD  
RUN cd docker-git && makepkg --clean --noconfirm --noprogressbar
--skipchecksums  
  
# Install package  
USER root  
RUN pacman --upgrade --noconfirm --noprogressbar docker-git/docker-
git*.pkg.tar.xz  
  
RUN curl -L https://github.com/docker/fig/releases/download/1.0.0/fig-`uname
-s`-`uname -m` > /usr/local/bin/fig  
RUN chmod +x /usr/local/bin/fig  
  
RUN groupadd --gid 999 dockergroup || exit 0  
RUN gpasswd -a http $(cat /etc/group|grep 999|awk -F: '{print $1}')  
  
VOLUME /fig  
RUN sed -i 's#open_basedir = .*#\0:/fig#' /etc/php/php.ini  
  
ADD index.php /srv/http/index.php  
  
ENV DOCKER_HOST unix://tmp/docker.sock  
  
USER http  


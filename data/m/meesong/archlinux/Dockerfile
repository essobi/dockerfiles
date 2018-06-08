# meesong/archlinux  
FROM meesong/arch-base:latest  
  
MAINTAINER MeeSong <meesong@outlook.com>  
  
ENV LANG=C.UTF-8  
# Pacman config  
COPY pacman.conf /etc/pacman.conf  
COPY mirrorlist /etc/pacman.d/mirrorlist  
RUN chmod 644 /etc/pacman.conf /etc/pacman.d/mirrorlist  
  
# Time zone  
ENV TZ=Asia\/Shanghai  
RUN set -x \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone  
  
# Packages  
RUN set -x \  
&& pacman -Syu \  
&& pacman -S --noconfirm yaourt archlinuxcn-keyring \  
&& pacman -S --noconfirm vim wget curl git openssh zsh \  
&& sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)" \  
&& pacman -Scc --noconfirm  
  
# gosu  
ENV GOSU_VERSION=1.10  
ENV ARCHITECTURE=amd64  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$ARCHITECTURE"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$ARCHITECTURE.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
WORKDIR /root  
ENTRYPOINT ["/bin/zsh"]  


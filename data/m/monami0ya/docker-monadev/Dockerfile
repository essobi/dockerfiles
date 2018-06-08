FROM monami0ya/docker-baseimage:monadev-16.04  
MAINTAINER Masaki Muranaka "https://github.com/monaka"  
RUN echo dummy-1  
  
RUN add-apt-repository -y ppa:openjdk-r/ppa  
RUN add-apt-repository ppa:jonathonf/vim  
RUN apt-get update  
  
RUN apt-get install -y openssh-server eclipse xvfb wget \  
xbase-clients python-psutil libpango1.0-0 libxss1 \  
zip unzip eclipse maven git tmux vim  
RUN apt-get install -y openjdk-8-jdk openjfx  
RUN apt-get install -y dnsutils  
RUN apt-get install -y libssl-dev \  
libmcrypt-dev libreadline-dev libxslt1-dev libxml2-dev libbz2-dev
libcurl4-openssl-dev \  
libpng-dev libjpeg-dev libmcrypt-dev libsqlite-dev libtidy-dev libltdl-dev \  
make autoconf automake re2c lemon \  
bash-completion \  
gawk libsqlite3-dev sqlite3 libgmp-dev libgdbm-dev libncurses5-dev bison
libffi-dev \  
libzmq3-dev \  
jq  
  
RUN apt-get install -y policykit-1 libgtk-3-0  
RUN wget https://dl.google.com/linux/direct/chrome-remote-
desktop_current_amd64.deb  
RUN dpkg -i chrome-remote-desktop_current_amd64.deb && rm chrome-remote-
desktop_current_amd64.deb  
  
RUN echo 'root:root' |chpasswd  
  
RUN addgroup --gid 1000 monaka  
RUN adduser --uid 1000 --gid 1000 --shell /bin/bash monaka  
RUN apt-get install -y sudo  
RUN echo 'monaka ALL=NOPASSWD: ALL' > /etc/sudoers.d/monaka  
RUN addgroup --gid 1001 cryptcoin-junkey  
RUN adduser --uid 1001 --gid 1001 --shell /bin/bash cryptcoin-junkey  
  
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin no/'
/etc/ssh/sshd_config  
RUN sed -ri 's/^#?PasswordAuthentication\s+.*/PasswordAuthentication no/'
/etc/ssh/sshd_config  
#RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
EXPOSE 22  
RUN mkdir /etc/service/x11vnc  
ADD x11vnc.sh /etc/service/x11vnc/run  
  
RUN mkdir /etc/service/xvfb  
ADD xvfb.sh /etc/service/xvfb/run  
  
RUN apt-get install -y vim x11vnc xvfb awesome traceroute man \  
xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic sakura \  
xfonts-intl-japanese xfonts-intl-japanese-big \  
chromium-browser libyaml-dev build-essential zlib1g-dev language-pack-ja  
  
RUN ln -sf /var/host/media/removable/ /media/removable  
  


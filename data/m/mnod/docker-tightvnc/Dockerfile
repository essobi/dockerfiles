From debian:wheezy  
  
RUN sed -i -e 's/$/ contrib non-free/' /etc/apt/sources.list  
RUN apt-get update && apt-get install --no-install-recommends -y \  
dynamips \  
dynagen \  
telnet \  
tcpdump \  
screen \  
git \  
subversion \  
vim-tiny \  
openssh-server \  
pwgen \  
ca-certificates \  
locales \  
lxde \  
tightvncserver \  
xfonts-base \  
iceweasel \  
dbus-x11 ibus-anthy fonts-ipafont \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/run/sshd  
RUN sed -i -e '/PermitRootLogin/ s/yes/no/' /etc/ssh/sshd_config  
  
RUN sed -i -e 's/^# ja_JP.UTF-8/ja_JP.UTF-8/' /etc/locale.gen && \  
locale-gen && \  
update-locale LANG=ja_JP.UTF-8  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
RUN useradd -s /bin/bash -m docker  
  
EXPOSE 22  
CMD ["/run.sh"]  


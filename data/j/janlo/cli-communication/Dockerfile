FROM debian:stretch  
  
MAINTAINER Jan Losinski <losinski@wh2.tu-dresden.de>  
  
ENV USER jan  
  
RUN DEBIAN_FRONTEND=noninteractive DEBIAN_NONINTERACTIVE_SEEN=true apt-get
update && \  
apt-get -y install \  
tmux \  
irssi \  
irssi-plugin-xmpp \  
mutt-patched \  
gnupg2 \  
gnupg \  
zsh \  
vim-nox \  
vim-addon-manager \  
vim-scripts \  
ncurses-term \  
w3m \  
wget \  
curl \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN groupadd ${USER} && \  
useradd --uid 1000 --create-home --home-dir /home/${USER} -s /bin/zsh -g
${USER} ${USER}  
  
ADD run /usr/bin/start-tmux  
ADD attach /usr/bin/attach-tmux  
  
WORKDIR /home/${USER}  
  
VOLUME /home/${USER}  
  
USER ${USER}  
  
ENTRYPOINT ["/usr/bin/start-tmux"]  


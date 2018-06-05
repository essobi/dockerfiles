FROM l3iggs/archlinux-aur  
MAINTAINER l3iggs <l3iggs@live.com>  
  
# add rack config file  
ADD config.ru /home/docker/config.ru  
  
# install better webserver  
RUN yaourt -S --noconfirm --needed ruby-thin  
  
# install ssl forcer  
RUN yaourt -S --noconfirm --needed ruby-rack-ssl  
  
# Install gollum  
RUN yaourt -S --noconfirm --needed gollum  
  
# for working in the image  
RUN sudo pacman --noconfirm --needed -S vim  
  
# generate self-signed ssl cert  
WORKDIR /root  
ENV SUBJECT /C=US/ST=CA/L=CITY/O=ORGANIZATION/OU=UNIT/CN=localhost  
RUN sudo openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out
server.key  
RUN sudo chmod 600 server.key  
RUN sudo openssl req -new -key server.key -out server.csr -subj $SUBJECT  
RUN sudo openssl x509 -req -days 3650 -in server.csr -signkey server.key -out
server.crt  
RUN sudo mkdir /https  
RUN sudo ln -s /root/server.crt /https/server.crt  
RUN sudo ln -s /root/server.key /https/server.key  
  
# switch to root  
USER 0  
# make wiki dir  
RUN mkdir /wiki  
  
# set wiki repo directory variable  
ENV WIKI_REPO /wiki  
  
# set default login  
ENV WIKI_USER gollum  
ENV WIKI_PASS gollum  
  
# start gollum twice  
# once for https and once for http  
CMD thin start --ssl --ssl-key-file /https/server.key --ssl-cert-file
/https/server.crt -p 443 -R /home/docker/config.ru& thin start -p 80 -R
/home/docker/config.ru  


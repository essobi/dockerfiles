# https://docs.docker.com/engine/reference/builder/  
FROM opensuse/tumbleweed  
MAINTAINER Jimmy Berry <jimmy@boombatower.com>  
  
RUN zypper -n ref && zypper -n dup && zypper -n in aws-cli make wget rsync  
  
# Since addative file system pointless to remove source and make. Not ideal,
but  
# short of file system rebase being built-in this is only way to use Makefile.  
COPY . /srv/source  
RUN cd /srv/source && make install  
  
WORKDIR /srv  
ENTRYPOINT ["tumbleweed-snapshot"]  


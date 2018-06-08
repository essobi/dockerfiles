FROM debian  
#  
MAINTAINER João Antonio Ferreira "joao.parana@gmail.com"  
  
RUN apt-get update && apt-get install -y \  
aufs-tools \  
automake \  
btrfs-tools \  
build-essential \  
curl \  
dpkg-sig \  
git \  
iptables \  
libapparmor-dev \  
libcap-dev \  
libsqlite3-dev \  
lxc \  
ssh-client \  
libc++-dev \  
libarchive-tar-perl  
  
# Tip: To run eval.sh as entrypoint you have to put  
# the shebang in eval.sh script and run "chmod a+rx eval.sh" command  
COPY ./eval.sh /  
RUN chmod a+rx /eval.sh  
# setting the image’s main command, allowing that image to be run as though it
was that command  
ENTRYPOINT ["/eval.sh"]  
  
# use help as the default flag for eval bash command  
CMD ["help"]  


# Use this very basic openSUSE JeOS image -- till I can get my own image to
build with KIWI  
FROM hachque/opensuse:latest  
  
# HEY, This is me!  
MAINTAINER Drew Adams <druonysus@opensuse.org>  
  
# lets do all our work from the context of the /root directory  
WORKDIR /root  
  
# add some nice stuff to /etc/vimrc  
ADD fs/etc/vimrc /etc/vimrc  
  
# set skel the way I like it.  
ADD fs/etc/skel /etc/skel  
  
# load up /root with my skel stuff  
ADD fs/etc/skel /root  
  
# we will need a copy of the .repo file to inport  
ADD fs/root/13.1-2014-06-17.repo /root/sources.repo  
  
# remove any existing repos ; inport the repos with zypper; get the gpg keys
for the repos ; remove source repos file  
RUN ( zypper rr {1..100} && zypper ar -f /root/sources.repo && zypper -n
--gpg-auto-import-keys ref ) \  
&& rm -f /root/sources.repo  
  
# install Salt Minion along with some of my favorite packages and patterns.  
RUN zypper -n in -t pattern base devel_basis devel_C_C++ console \  
&& zypper -n in zsh ksh tmux tcpdump tree mlocate command-not-found sudo salt-
minion salt  
  
# Salt uses these ports, so lets expose these  
EXPOSE 4505 4506  


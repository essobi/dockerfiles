# See https://github.com/phusion/baseimage-docker  
FROM phusion/baseimage:0.9.22  
MAINTAINER Doug Goldstein <cardoe@cardoe.com>  
  
# No Debian that's a bad Debian! We don't have an interactive prompt don't
fail  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use baseimage-docker's init  
# https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-
problem/  
ENTRYPOINT ["/sbin/my_init", "--"]  
  
# Where we build  
RUN mkdir -p /var/build  
WORKDIR /var/build  
# workaround HOME ignore. see https://github.com/phusion/baseimage-
docker/issues/119  
RUN echo /var/build > /etc/container_environment/HOME  
  
# utilize my_init from the baseimage to create the user for us  
# the reason this is dynamic is so that the caller of the container  
# gets the UID:GID they need/want made for them  
RUN mkdir -p /etc/my_init.d  
ADD create-user.sh /etc/my_init.d/create-user.sh  
  
# bitbake wrapper to drop root perms  
ADD bitbake.sh /usr/local/bin/bitbake  
ADD bitbake.sh /usr/local/bin/bitbake-diffsigs  
ADD bitbake.sh /usr/local/bin/bitbake-dumpsig  
ADD bitbake.sh /usr/local/bin/bitbake-layers  
ADD bitbake.sh /usr/local/bin/bitbake-prserv  
ADD bitbake.sh /usr/local/bin/bitbake-selftest  
ADD bitbake.sh /usr/local/bin/bitbake-worker  
ADD bitbake.sh /usr/local/bin/bitdoc  
ADD bitbake.sh /usr/local/bin/image-writer  
ADD bitbake.sh /usr/local/bin/toaster  
ADD bitbake.sh /usr/local/bin/toaster-eventreplay  
  
# ensure our rebuilds remain stable  
ENV APT_GET_UPDATE 2017-09-11  
# Yocto's depends  
# plus some debugging utils  
RUN apt-get --quiet --yes update && \  
apt-get --quiet --yes install gawk wget git-core diffstat unzip \  
texinfo gcc-multilib build-essential chrpath socat cpio python \  
python3-pip python3-pexpect xz-utils debianutils iputils-ping \  
libsdl1.2-dev xterm sudo curl libssl-dev tmux strace ltrace && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set the default shell to bash instead of dash  
RUN echo "dash dash/sh boolean false" | debconf-set-selections && dpkg-
reconfigure dash  
  
# If you need to add more packages, just do additional RUN commands here  
# this is so that layers above to not have to be regenerated.  


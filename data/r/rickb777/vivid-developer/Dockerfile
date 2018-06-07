FROM rickb777/vivid-base  
  
LABEL description="\  
Creates an Ubuntu instance that includes basic OS and developer cmd-line
tools. \  
By setting entrypoint to /sbin/init, it will start up Ubuntu as a headless \  
desktop for the user 'steve'."  
  
# A stevedore is an archaic term for a dock worker.  
MAINTAINER Rick Beton <rickb777@bitbucker.org>  
  
RUN export DEBIAN_FRONTEND=noninteractive; \  
apt-get update -q -q && \  
apt-get -y install --no-install-recommends \  
git mercurial \  
autoconf autoconf-doc build-essential sysv-rc-conf \  
libc6-dev libssl-dev libexpat1-dev \  
bison gawk gcc golang libc6-dev make gdbserver  
  
# Other candidate tools include:  
# ansible supervisor  
# save a bit of space in the Docker image by deleting apt sources  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY installers /home/steve/installers  
  
# To start the Docker image so that it behaves just like an Ubuntu server, use  
# --entrypoint /sbin/init  
# and put "splash" as the command-option.  


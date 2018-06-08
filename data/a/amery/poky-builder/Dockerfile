FROM ubuntu:16.04  
# UK mirror  
RUN sed -i 's|http://archive.ubuntu.com|http://gb.archive.ubuntu.com|'
/etc/apt/sources.list  
  
# reduce apt-get install warnings  
ENV TERM xterm  
  
# Platform requirements  
#  
# debconf: delaying package configuration, since apt-utils is not installed  
#  
RUN apt-get update && apt-get install --no-install-recommends -y \  
apt-utils \  
build-essential \  
ca-certificates \  
language-pack-en \  
&& apt-get clean  
  
# bitbake: Please use a locale setting which supports utf-8.  
ENV LANG=en_GB.UTF-8  
RUN update-locale LANG=$LANG LC_MESSAGES=POSIX  
  
# required by OE's sanity check  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
chrpath \  
cpio \  
cvs \  
diffstat \  
gawk \  
git \  
iputils-ping \  
python \  
python3 \  
subversion \  
texinfo \  
texi2html \  
wget \  
&& apt-get clean  
  
# minimal interactivity  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
tmux \  
vim \  
&& apt-get clean  
  
# and remove things that confuse the entrypoint script  
RUN apt-get remove --purge -y \  
rsync \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
COPY tmux.conf /etc/tmux.conf  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  


FROM ubuntu:16.04  
LABEL maintainer="Ian Martin <ian@imartin.net>" license="MIT"
description="Combined Blu-Ray and DVD ripping program"  
  
ENV DISPLAY=":0" LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive  
  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ xenial universe \  
deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates universe \  
deb http://us.archive.ubuntu.com/ubuntu/ xenial multiverse \  
deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates multiverse" >>
/etc/apt/sources.list && \  
echo 'deb http://ppa.launchpad.net/heyarje/makemkv-beta/ubuntu xenial main' >
/etc/apt/sources.list.d/makemkv.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8540356019f7e55b && \  
apt-get update && \  
apt-get install -yq makemkv-oss makemkv-bin curl libbluray-bin lsdvd dvdbackup
libdvd-pkg && \  
dpkg-reconfigure libdvd-pkg && \  
# addgroup -u 10298 media && \  
# useradd --no-create-home --uid 10298 --gid media media && \  
# passwd -l media && \  
mkdir -p /rips  
# chown -R 10298:10298 /rips  
# it would be nice to run this container as non-root, but it needs access to
/dev/sr0, and it's  
# nearly impossible to get the media user added to right group to match the
hosts idea of the device's group  
# ownership. So... root it is for now.  
COPY entrypoint.sh /  
USER root  
VOLUME /rips  
  
ENTRYPOINT ["/entrypoint.sh"]  


FROM debian:latest  
MAINTAINER John Huang <little78926@gmail.com>  
  
ENV container docker  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list  
RUN echo "deb http://deb.debian.org/debian stretch-backports main contrib non-
free" >> /etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get install -y systemd sudo curl gnupg gnupg2 gnupg1  
  
RUN cd /tmp \  
&& curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& apt-get install -y nodejs  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN cd /lib/systemd/system/sysinit.target.wants/; ls | grep -v systemd-
tmpfiles-setup | xargs rm -f $1 \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*; \  
rm -f /lib/systemd/system/plymouth*; \  
rm -f /lib/systemd/system/systemd-update-utmp*;  
  
RUN systemctl set-default multi-user.target  
ENV init /lib/systemd/systemd  
VOLUME [ "/sys/fs/cgroup" ]  
  
# CMD ["/usr/sbin/init"]  
  
RUN mkdir -p /home  
WORKDIR /home  
  
ARG local="."  
  
RUN apt-get update -y  
RUN apt-get install -y --fix-missing automake autotools-dev fuse g++ git \  
libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config  
  
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git; \  
cd s3fs-fuse; \  
./autogen.sh; \  
./configure --prefix=/usr; \  
make; \  
make install;  
  
COPY $local/config/fuse.conf /etc/fuse.conf  
COPY $local/config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY $local/run.sh /home/run.sh  
RUN chmod +x /home/run.sh  
  
# ENTRYPOINT ["/home/run.sh"]  
# CMD ["/bin/bash"]  
ENTRYPOINT ["/lib/systemd/systemd"]


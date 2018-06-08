FROM debian:jessie  
  
MAINTAINER "Abejaruco" <garcia.luisfelipe@gmail.com>  
  
ENV container docker  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV init /lib/systemd/systemd  
  
RUN rm -f /lib/systemd/system/multi-user.target.wants/systemd-logind.service  
  
RUN apt-get upgrade --yes --force-yes  
RUN apt-get update  
RUN apt-get install apt-utils --yes  
RUN apt-get install dialog dbus sudo screen tmux python curl wget vim less
--yes  
  
RUN echo 'root:vagrant' | chpasswd  
RUN mkdir -p /home/vagrant  
RUN groupadd -r vagrant -g 1000 && \  
useradd -u 1000 -r -g vagrant -d /home/vagrant -s /bin/bash -c "Docker image
user" vagrant && \  
chown -R vagrant:vagrant /home/vagrant && \  
echo "vagrant:vagrant" | chpasswd && \  
adduser vagrant sudo && \  
echo "vagrant ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/vagrant  
  
RUN echo "alias ll='ls $LS_OPTIONS -l'" >> /etc/profile  
RUN echo "alias l='ls $LS_OPTIONS -lA'" >> /etc/profile  
RUN apt-get install openssh-server --yes  
  
CMD ["/lib/systemd/systemd", "--system"]  
#docker run -it -h systemd -e APPLICATION_ENV=development --cap-add SYS_ADMIN
--name=prueba -v /sys/fs/cgroup:/sys/fs/cgroup:ro prueba /lib/systemd/systemd
--system  
ONBUILD ADD . /opt/app  


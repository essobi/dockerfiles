#  
# Minimum Docker image to build Android AOSP  
#  
FROM shugaoye/docker-aosp:ubuntu16.04-JDK7  
  
MAINTAINER Roger Ye <shugaoye@yahoo.com>  
  
# install and configure SSH server  
RUN apt-get update  
RUN apt-get install -y openssh-server genisoimage net-tools gettext vim-common
vim-tiny python-pip  
RUN mkdir /var/run/sshd  
RUN export LC_ALL=C  
RUN sudo pip install Mako  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
# The persistent data will be in these two directories, everything else is  
# considered to be ephemeral  
VOLUME ["/tmp/ccache", "/home/aosp"]  
  
# Improve rebuild performance by enabling compiler cache  
ENV USE_CCACHE 1  
ENV CCACHE_DIR /tmp/ccache  
  
# Work in the build directory, repo is expected to be init'd here  
WORKDIR /home/aosp  
  
COPY utils/bash.bashrc /root/bash.bashrc  
RUN chmod 755 /root /root/bash.bashrc  
COPY utils/docker_entrypoint.sh /root/docker_entrypoint.sh  
ENTRYPOINT ["/root/docker_entrypoint.sh"]  


FROM centos:centos7  
MAINTAINER Amit Bakshi <ambakshi@gmail.com>  
  
RUN yum update -y && \  
yum groupinstall -y 'Development Tools' && \  
yum install -y libX11-devel freetype-devel zlib-devel libxcb-devel epel tar
bzip2 vim-enhanced git curl  
RUN curl -sSL http://prdownloads.sourceforge.net/wine/wine-1.9.0.tar.bz2 | tar
jxf - -C /usr/src  
WORKDIR /usr/src/wine-1.9.0  
RUN yum install -y libxml2-devel libxslt-devel libgnutls-devel libjpeg-devel
gnutls-devel libpng-devel openssh-server openssh xorg-x11-apps xauth  
RUN ./configure --enable-win64 --with-png  
RUN make -j4  
RUN make install  
RUN curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/v1.16.0.0/s6-overlay-amd64.tar.gz |
tar zxf - -C /  
RUN mkdir -m 0700 -p /root/.ssh  
ADD insecure.pub /root/.ssh/authorized_keys  
RUN chmod 0600 /root/.ssh/authorized_keys  
RUN /usr/bin/ssh-keygen -A  
RUN sed -i -e 's/^GSSAPIAuthentication.*$/GSSAPIAuthentication no/g'
/etc/ssh/sshd_config  
RUN sed -i -e 's/^#UseDNS.*$/UseDNS no/g' /etc/ssh/sshd_config  
RUN sed -i -e 's/^#X11UseLocalhost.*$/X11UseLocalhost no/g'
/etc/ssh/sshd_config  
RUN sed -i -e 's/^#AddressFamily.*$/AddressFamily inet/g' /etc/ssh/sshd_config  
EXPOSE 22  
ENTRYPOINT ["/init"]  
CMD ["/usr/sbin/sshd","-D"]  
  


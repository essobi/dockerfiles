# Development  
#  
# VERSION 0.2  
# Dockerfile  
FROM centos:latest  
  
MAINTAINER Kim Goh <gaojingan@gmail.com>  
LABEL Vendor="CentOS"  
LABEL License=GPLv2  
LABEL Version=0.2  
  
RUN yum -y update; yum -y clean all  
RUN yum -y --setopt=tsflags=nodocs install bash-completion curl wget w3m sudo
rsync vim git unzip gcc make automake zsh systemd-sysv \  
initscripts openssh-server openssh-clients net-tools environment-modules  
RUN yum -y clean all; yum -y erase vim-minimal  
  
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"  
  
RUN ssh-keygen -q -N "" -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -b 2048 -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
RUN /bin/echo 'root:gaoxing' |chpasswd  
  
RUN /bin/sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional
pam_loginuid.so/g' /etc/pam.d/sshd  
RUN /bin/echo -e "LANG=\"en_US.UTF-8\"" > /etc/default/local  
  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config; echo "UseDNS no" >>
/etc/ssh/sshd_config; echo "Port 22" >> /etc/ssh/sshd_config  
  
EXPOSE 22 80 443  
ENV container=docker  
  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
RUN systemctl enable sshd  
  
ENV GOLANG_VERSION 1.7  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
702ad90f705365227e902b42d91dd1a40e48ca7f67a2f4b2fd052aaa4295cd95  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
ADD golang /usr/share/Modules/modulefiles/golang  
  
VOLUME [ "/sys/fs/cgroup" ]  
CMD ["/usr/sbin/init"]  


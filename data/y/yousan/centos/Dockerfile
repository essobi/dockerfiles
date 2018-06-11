FROM centos:7  
  
ENV container docker  
LABEL maintainer="yousan@l2tp.org"  
  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
  
RUN yum update -y && \  
yum install -y emacs-nox zsh mlocate etckeeper git sudo  
  
RUN adduser yousan && usermod -aG root,adm,wheel yousan  
#USER yousan  
#RUN cd ~/ && mkdir git && cd git && git clone
https://github.com/yousan/dotfiles && cd dotfiles && \  
# pwd -P && yes | sh install_oh-my-zsh.sh ; sh ./init.sh  
# Change default shell to zsh. Only root allowed change shell without
password.  
#USER root  
#RUN chsh -s /bin/zsh yousan  
# USER yousan  
  
RUN sed -i -e 's/# %wheel\tALL=(ALL)\tNOPASSWD:
ALL/%wheel\tALL=(ALL)\tNOPASSWD: ALL/' /etc/sudoers  
RUN sed -i -e 's/%wheel\tALL=(ALL)\tALL/# %wheel\tALL=(ALL)\tALL/'
/etc/sudoers  
RUN visudo -c  
  
#RUN echo "[unit]\n name=unit repo\n
baseurl=http://nginx.org/packages/mainline/centos/7/$basearch/ \n gpgcheck=0
\n enabled=1' \n" > /etc/yum.repos.d/unit.repo  
# COPY unit.repo /etc/yum.repos.d/unit.repo  
# RUN yum install -y unit  
# VOLUME [ "/sys/fs/cgroup" ]  
# RUN systemctl  
# RUN systemctl enable unitd.service  
# RUN systemctl start unitd.service  
# USER yousan  
CMD ["/usr/sbin/init"]  


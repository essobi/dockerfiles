# Bitrix env Docker file  
# https://hub.docker.com/infoservice/bitrixenv7  
# https://github.com/infoservice/bitrixenv7  
  
FROM centos:7  
MAINTAINER "Infoservice" dev@infoservice.ru  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
  
#pre-setup  
RUN yum install wget mc nano initscripts ethtool bind-utils -y  
RUN echo "export LC_ALL=en_US.UTF-8" >> /etc/profile  
RUN export LC_ALL=en_US.UTF-8  
# Get Bitrix install script to /opt  
ADD http://repos.1c-bitrix.ru/yum/bitrix-env.sh /opt/  
RUN chmod +x /opt/bitrix-env.sh  
  
# Add scripts for auto-install bitrix-env at login with --login flag  
ADD https://bitbucket.org/Infoservice_web/bitrix-
env7-docker/raw/860c32bd68d94754a3eb4aa188ebad4d46ed45cf/bitrix_entrypoint.sh
/opt/bitrix_entrypoint.sh  
RUN chmod +x /opt/bitrix_entrypoint.sh  
  
RUN mv /root/.bash_profile /root/.bash_profile.disabled  
ADD https://bitbucket.org/Infoservice_web/bitrix-
env7-docker/raw/a42b433c2c52c310bff5682a1acbd677688b01c5/.bash_profile
/root/.bash_profile  
RUN chown -R root /root/.bash_profile  
  
# For run services  
CMD ["/usr/sbin/init"]


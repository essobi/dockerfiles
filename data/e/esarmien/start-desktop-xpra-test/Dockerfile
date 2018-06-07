FROM fedora:latest  
EXPOSE 8080  
RUN mkdir /var/run/dbus  
RUN mkdir -p /run/user/0/xpra/  
RUN yum -y update && \  
rpm --import https://winswitch.org/gpg.asc && \  
cd /etc/yum.repos.d/ && \  
yum install -y curl && \  
curl -O https://winswitch.org/beta/Fedora/winswitch-beta.repo && \  
yum -y update && \  
yum -y install xpra && \  
yum -y install python-dbus google-roboto-fonts libvpx libvpx-devel python-libs
python-websockify && \  
yum -y install @lxde-desktop  
COPY start-lxde.sh /usr/bin  
CMD ["bash", "/usr/bin/start-lxde.sh"]  


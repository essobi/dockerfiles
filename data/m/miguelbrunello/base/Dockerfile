# sshd  
#  
# VERSION 1.0  
# https://docs.docker.com/examples/running_ssh_service/  
  
FROM ubuntu:14.04  
MAINTAINER Miguel Brunello <miguel.brunello@unc.edu.ar>  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y \  
aptitude \  
mc \  
openssh-server  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#RUN mkdir -p /root/.ssh  
ADD root /root  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
#########################################################  
  
# Supervisor  
RUN apt-get update && apt-get -qy install \  
python-setuptools  
RUN easy_install supervisor  
ADD ./supervisor/supervisord.conf /etc/supervisord.conf  
ADD ./supervisor/supervisord.d /etc/supervisord.d  
ADD ./opt /opt  
  
#########################################################  
  
RUN locale-gen es_AR.UTF-8  
ENV LANG es_AR.UTF-8  
ENV LC_CTYPE es_AR.UTF-8  
  
RUN dpkg-divert --local --rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
RUN apt-get update && apt-get install -y \  
vim \  
software-properties-common \  
rsync \  
sshfs \  
cifs-utils  
  
#Instalación de gdrive:  
RUN add-apt-repository -y ppa:twodopeshaggy/drive && \  
apt-get update && apt-get install drive  
  
# Gluster Client  
RUN echo "" | add-apt-repository ppa:gluster/glusterfs-3.5  
RUN apt-get update && apt-get -qy install \  
glusterfs-client  
  
ADD gen-prot /root/tools/gluster/gen-prot  
ADD mount.gluster /sbin/mount.gluster  
ADD rc.local /etc/rc.local  
RUN chmod 755 /etc/rc.local  
ADD start.sh /start.sh  
  
  
  
# Final  
#WORKDIR /root/tools/gluster  
#RUN ./gen-prot devnull.psi.unc.edu.ar fernanda /mnt/varios-01  
#RUN ./gen-prot devnull.psi.unc.edu.ar varios-01 /mnt/varios-01  
#RUN ln -s /var/log/glusterfs/mnt-varios-01.log /root/tools/gluster/log  
  
  
  
  
  
  
  
  


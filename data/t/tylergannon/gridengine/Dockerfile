######################################################  
#  
# GridEngine Server  
# Tag: tylergannon/gridengine  
#  
# This container provides a standard pbs controller  
# and worker created on top of the agaveapi/centos-base  
# image. Nothing special here.  
#  
# Usage:  
# docker run -h docker.example.com -i -t \  
# -p 127.0.0.1:10022:22 \ # SSHD, SFTP \  
# -p 127.0.0.1:4443:443 \ # HTTPS  
# --rm tylergannon/gridengine  
#  
# tylergannon/gridengine  
#  
# Builds a Centos 6 machine with gridengine, and the necessary  
# components for pyenv and remote_sge  
#  
######################################################  
  
FROM agaveapi/gridengine  
  
MAINTAINER Tyler Gannon <tyler.gannon@interxinc.com>  
  
# Install GridEngine  
RUN yum -y install git nginx sqlite-devel readline-devel bzip2-devel \  
gcc gcc-c++ kernel-devel make zlib-devel openssl-devel sudo; \  
yum clean all  
RUN usermod -aG wheel testuser  
EXPOSE 443  
  
RUN yum -y install tar gzip sudo bzip2; yum clean all  
RUN echo "%wheel ALL=(ALL) ALL" >> /etc/sudoers  
RUN echo "export DOCKER=yes" >> /home/testuser/.bashrc  
RUN su -l testuser \  
-c "curl -L https://raw.githubusercontent.com/tylergannon/remote_sge/master/src/bin/install.sh | bash"  
  
RUN yum -y install vim; yum clean all  


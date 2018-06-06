FROM flyceek/centos7-android-build:gradle-4.4.1  
MAINTAINER flyceek <flyceek@gmail.com>  
  
RUN yum update -y \  
&& yum install -y passwd openssh openssh-clients openssh-server \  
&& yum clean all \  
&& rm -rf /etc/ssh/ssh_host_*_key /etc/ssh/ssh_host_*_key.pub \  
&& ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N '' \  
&& ssh-keygen -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N '' \  
&& ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' \  
&& ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N '' \  
&& sed -i 's/#RSAAuthentication yes/RSAAuthentication yes/'
/etc/ssh/sshd_config \  
&& sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/'
/etc/ssh/sshd_config \  
&& sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config \  
&& sed -i 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd","-D"]


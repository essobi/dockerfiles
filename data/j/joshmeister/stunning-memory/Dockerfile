FROM fedora:latest  
  
RUN yum -y install openssh-server docker && \  
yum install -y pwgen supervisor nano net-tools less wget findutils screen
bash-completion git nmap procps-ng && \  
curl https://raw.githubusercontent.com/rapid7/metasploit-
omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb >
msfinstall && \  
chmod 755 msfinstall && \  
./msfinstall && \  
yum clean all && \  
yum -y update && yum clean all && \  
rm -rf /var/cache/yum/* && \  
rm -rf /var/cache/dnf/* && \  
rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \  
sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/g"
/etc/ssh/sshd_config && \  
sed -i "s/#Port 22/Port 6667/g" /etc/ssh/sshd_config  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
COPY supervisord.conf /supervisord.conf  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 80 443 445 6667 24245  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
  
CMD ["/run.sh"]  


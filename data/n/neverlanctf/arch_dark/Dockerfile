FROM base/archlinux  
MAINTAINER Ian Laird <en0@mail.com>  
  
# Install sshd and configure it  
RUN \  
pacman-key --refresh-keys && \  
pacman --noconfirm -Syu openssh supervisor && \  
pacman-db-upgrade && \  
ssh-keygen -f /etc/ssh/ssh_host_rsa_key -t rsa -N '' && \  
ssh-keygen -f /etc/ssh/ssh_host_dsa_key -t dsa -N '' && \  
ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -t ecdsa -N '' && \  
ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -t ed25519 -N '' && \  
echo -e "Match Group sandbox" >> /etc/ssh/sshd_config && \  
echo -e "\tPasswordAuthentication yes" >> /etc/ssh/sshd_config && \  
echo -e "\tChrootDirectory /sandbox/" >> /etc/ssh/sshd_config && \  
echo -e "\tAllowTcpForwarding no" >> /etc/ssh/sshd_config && \  
sed -i s/^#PasswordAuthentication.*/PasswordAuthentication\ no/g
/etc/ssh/sshd_config  
# Create the hacker user (password hacker)  
RUN \  
ln /bin/bash /bin/rbash && \  
groupadd sandbox && \  
useradd -g sandbox -G users -m -s /bin/rbash hacker && \  
echo -e "hacker\nhacker" | passwd hacker  
  
# Create the chroot directory  
RUN \  
mkdir -p /sandbox/{bin,lib,lib64,usr/lib,usr/lib64,dev,home/hacker} && \  
mknod /sandbox/dev/null c 1 3 && \  
mknod /sandbox/dev/zero c 1 5 && \  
chmod 0666 /sandbox/dev/{zero,null} && \  
chown root:root /sandbox/home/hacker && \  
chmod 655 /sandbox/home/hacker  
  
ADD ./sshd_process.ini /etc/supervisor.d/  
  
# Install rbash in the chroot directory (This will probably break often.  
# If you find a way to handle the library versions and linking with what  
# bash expects, please please please let me know. i will buy you a beer.  
RUN \  
cp -p /bin/bash /sandbox/bin/rbash && \  
sed -i 0,/^$/s/^$/\\\/bin\\\/rbash/ /etc/shells && \  
cp -p /usr/lib/libreadline.so.6.3 /usr/lib/libncursesw.so.6.0
/usr/lib/libdl-2.23.so /usr/lib/libc-2.23.so /sandbox/lib/ && \  
cp -p /lib64/ld-2.23.so /sandbox/lib64/ && \  
ln /sandbox/lib/libreadline.so.6.3 /sandbox/usr/lib/libreadline.so.6 && \  
ln /sandbox/lib/libncursesw.so.6.0 /sandbox/usr/lib/libncursesw.so.6 && \  
ln /sandbox/lib/libdl-2.23.so /sandbox/usr/lib/libdl.so.2 && \  
ln /sandbox/lib/libc-2.23.so /sandbox/usr/lib/libc.so.6 && \  
ln /sandbox/lib64/ld-2.23.so /sandbox/lib64/ld-linux-x86-64.so.2  
  
ADD secret /sandbox/home/hacker/  
  
EXPOSE 22  
  
CMD supervisord -n  


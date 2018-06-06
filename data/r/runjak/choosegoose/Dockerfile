FROM alpine:latest  
  
MAINTAINER Jakob Runge <sicarius@g4t3.de>  
  
LABEL version="1.0.0" \  
source="https://github.com/runjak/docker-choosegoose"  
# Fetching necessary apk packages:  
RUN apk update \  
&& apk upgrade \  
&& apk add \  
git \  
openssh \  
zsh \  
&& rm /var/cache/apk/APKINDEX*tar.gz \  
# We need grml.conf for zsh:  
&& wget -O /etc/zsh/zshrc http://git.grml.org/f/grml-etc-core/etc/zsh/zshrc \  
# Disable password auth and root login:  
&& sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g'
/etc/ssh/sshd_config \  
&& sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/g'
/etc/ssh/sshd_config \  
# Generating ssh keypairs:  
&& ssh-keygen -C "root@chooseGoose-$(date -I)" -f /etc/ssh/ssh_host_rsa_key -N
'' -t rsa \  
&& ssh-keygen -C "root@chooseGoose-$(date -I)" -f /etc/ssh/ssh_host_dsa_key -N
'' -t dsa \  
&& ssh-keygen -C "root@chooseGoose-$(date -I)" -f /etc/ssh/ssh_host_ecdsa_key
-N '' -t ecdsa \  
&& ssh-keygen -C "root@chooseGoose-$(date -I)" -f
/etc/ssh/ssh_host_ed25519_key -N '' -t ed25519 \  
# User specific configuration:  
&& adduser -s /bin/zsh -D mushu \  
&& passwd -d mushu \  
&& mkdir /home/mushu/git /home/mushu/.ssh \  
&& echo "# Placeholder" > /home/mushu/.zshrc \  
&& sync \  
&& echo "ssh-ed25519
AAAAC3NzaC1lZDI1NTE5AAAAIG2yHFL0iDzu8/Xw41Iik8XkRFmBIoqMjQvFVz/338h4
mushu@stormo-2016-02-23" > /home/mushu/.ssh/authorized_keys \  
&& chown -R mushu.mushu /home/mushu \  
&& chmod 600 /home/mushu/.ssh/authorized_keys  
  
# motd from  
# http://www.chris.com/ascii/index.php?art=art%20and%20design/patterns  
COPY motd /etc/motd  
  
VOLUME ["/home/mushu/git","/etc/ssh"]  
  
EXPOSE 22  
  
ENTRYPOINT ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]  


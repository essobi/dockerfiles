FROM effarig/archlinux  
  
MAINTAINER docker@effarig.co.uk  
  
RUN pacman -Suy --noconfirm \  
&& pacman-db-upgrade \  
&& pacman -S --noconfirm openssh sudo  
  
ADD files/sudoers /etc/sudoers  
ADD files/sshd_config /etc/ssh/sshd_config  
  
RUN useradd -m -l -G wheel james -p "$(dd if=/dev/urandom bs=1 count=21
2>/dev/null | base64)" \  
&& chmod 440 /etc/sudoers \  
&& chmod 644 /etc/ssh/sshd_config \  
&& ssh-keygen -A  
  
ADD files/authorized_keys /home/james/.ssh/authorized_keys  
  
RUN cd /home/james \  
&& chown james:users -R .ssh \  
&& chmod 700 .ssh \  
&& chmod 644 .ssh/authorized_keys  
  
EXPOSE 22  
CMD ["/usr/bin/sshd", "-D", "-e"]  


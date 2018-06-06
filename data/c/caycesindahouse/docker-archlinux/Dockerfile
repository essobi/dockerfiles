FROM base/devel:latest  
LABEL maintainer "cayce@houseco.cc"  
  
RUN echo -e "\n[multilib]\nInclude =
/etc/pacman.d/mirrorlist\n\n[caycehouse]\nSigLevel = Never\nServer =
https://caycehouse.com/arch/repo/x86_64" >> /etc/pacman.conf \  
&& pacman -Syu --noconfirm sshpass sshfs aurutils repoctl \  
&& rm -f \  
/var/cache/pacman/pkg/* \  
/var/lib/pacman/sync/* \  
/etc/pacman.d/mirrorlist.pacnew \  
&& useradd -m -U build \  
&& echo "build ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/build  
  
USER build  
WORKDIR /home/build  
  
CMD ["/bin/bash"]


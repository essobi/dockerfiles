FROM debian:latest  
RUN apt-get update && apt-get upgrade -y && apt-get install -y openssh-server
vim zsh git tmux figlet && rm -rf /var/lib/apt/lists/*  
  
# config  
RUN rm /etc/ssh/*  
COPY sshd_config /etc/ssh/sshd_config  
COPY ssh_config /etc/ssh/ssh_config  
RUN ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key < /dev/null  
RUN ssh-keygen -t rsa -b 4096 -f /etc/ssh/ssh_host_rsa_key < /dev/null  
  
#RUN ssh-keygen -G "/moduli" -b 4096 && ssh-keygen -T /etc/ssh/moduli -f
"/moduli" && rm "/moduli"  
RUN mkdir /var/run/sshd  
  
# user setup  
RUN useradd -m -g users ssher  
RUN echo 'ssher:notgood' |chpasswd  
RUN chsh -s /bin/zsh ssher  
  
VOLUME /home/ssher  
EXPOSE 22  
CMD /usr/sbin/sshd -D  


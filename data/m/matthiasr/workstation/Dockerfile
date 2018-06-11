FROM ubuntu  
  
RUN apt-get update && apt-get install -y ssh zsh vim dnsutils curl build-
essential  
COPY sshd_config /etc/ssh/sshd_config  
RUN rm /etc/ssh/ssh_host_*  
COPY prepare.sh /etc/ssh/prepare.sh  
COPY sudoers /etc/sudoers.d/mr  
RUN adduser --home /home/mr --shell /bin/zsh --uid 1000 --disabled-password
--gecos "" mr  
  
VOLUME /etc/openssh/keys  
VOLUME /home/mr  
WORKDIR /home/mr  
EXPOSE 22  
ENTRYPOINT [ "/etc/ssh/prepare.sh" ]  
CMD [ "/usr/sbin/sshd", "-D", "-e" ]  


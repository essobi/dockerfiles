FROM debian:stretch  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install nano bash openssh-server ca-
certificates autossh && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -ri 's/^#PermitRootLogin\s+.*/PermitRootLogin no/'
/etc/ssh/sshd_config && \  
sed -ri 's/^#Port\s+.*/Port 12136/' /etc/ssh/sshd_config  
  
RUN mkdir -p /var/run/sshd  
  
EXPOSE 12136  
EXPOSE 26189  
ADD
https://github.com/CJBlake/docker_autossh_jackett/blob/master/portforward.sh
/portforward.sh  
  
RUN chmod 770 portforward.sh  
  
CMD ["/usr/sbin/sshd", "-D"]  


FROM ubuntu  
RUN apt-get update && apt-get install -y mutt openssh-server&& apt-get clean
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && mkdir /var/run/sshd &&
echo "root:mutt" | chpasswd  
COPY sshd_config /etc/ssh/sshd_config  
CMD /usr/sbin/sshd -d  


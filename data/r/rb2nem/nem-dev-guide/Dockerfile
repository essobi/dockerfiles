from rb2nem/nis  
  
RUN dnf install -y curl httpie jq net-tools nano less telnet tcpdump  
COPY ./container_files/supervisord.conf /etc/  
COPY ./container_files/start.sh /usr/local/bin/start.sh  
COPY ./container_files/bash_aliases /root/.bash_aliases  
  
# uncomment this to override nis version available in rb2nem/nis image  
#RUN rm -r /package && curl https://bob.nem.ninja/beta-testnet/nis-
ncc-0.6.92.tgz -o /nis.tgz &&\  
# tar xvf nis.tgz  
ENTRYPOINT ["/usr/local/bin/start.sh"]  


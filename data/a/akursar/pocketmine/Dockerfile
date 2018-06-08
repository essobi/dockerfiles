FROM phusion/baseimage:0.9.16  
  
ENV HOME /root  
  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init"]  
  
RUN mkdir /var/lib/pocketmine  
RUN cd /var/lib/pocketmine && curl -sL "http://get.pocketmine.net/" | bash -s
\- -r -v development  
  
RUN mkdir /etc/service/pocketmine  
ADD pocketmine.sh /etc/service/pocketmine/run  
  
EXPOSE 19132/tcp 19132/udp  
  
VOLUME ["/pocketmine"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  


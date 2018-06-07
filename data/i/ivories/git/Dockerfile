FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get install -y ssh  
RUN apt-get install -y git  
RUN mkdir /var/run/sshd  
RUN chmod 0755 /var/run/sshd  
RUN usermod -s /usr/bin/git-shell root  
RUN mkdir /root/.ssh  
RUN mkdir /git  
RUN ln -s /root/.ssh /ssh  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 22  
VOLUME ["/home/core/data/git"]  
  
CMD [ "/usr/sbin/sshd", "-D" ]  


#FROM ubuntu:14.04  
FROM ubuntu:latest  
  
ENV GITHUB https://github.com/ljh575/luxixi/raw/master  
  
RUN /bin/ln -sfT /bin/bash /bin/sh  
  
RUN apt-get update && apt-get install --no-install-recommends -y openssh-
server wget git  
RUN git config --global http.sslVerify false  
  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN wget --no-check-certificate $GITHUB/script/install.sh && sh install.sh  
RUN wget --no-check-certificate $GITHUB/script/runit.sh && chmod +x runit.sh  
  
EXPOSE 22  
EXPOSE 10575  
EXPOSE 10575/udp  
  
ENTRYPOINT ["/bin/sh", "runit.sh"]  
  
CMD ["/bin/cat", "runit.sh"]  


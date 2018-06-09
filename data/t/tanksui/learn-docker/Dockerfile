FROM ubuntu:latest  
MAINTAINER Tank Sui <suiwenfeng@live.cn>  
  
# install dependency  
RUN apt-get update && apt-get install -y openssh-server apache2 supervisor  
  
# create folder  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
  
# ready for sshd  
RUN echo 'root:......' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN echo 'KexAlgorithms diffie-hellman-group1-sha1,ecdh-sha2-nistp256,ecdh-
sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-
hellman-group14-sha1' >> /etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# copy supervisord conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 22 80  
CMD ["/usr/bin/supervisord"]


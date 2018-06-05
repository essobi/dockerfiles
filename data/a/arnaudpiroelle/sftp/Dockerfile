FROM arnaudpiroelle/base  
MAINTAINER Arnaud Piroelle "piroelle.arnaud@gmail.com"  
RUN apt-get update && apt-get install -y openssh-server  
  
COPY entrypoint.sh /opt/entrypoint.sh  
COPY asset/sshd_config /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN groupadd sftpusers  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
VOLUME /sftp  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D"]


# 0x13 Configuration management  
FROM holbertonschool/292  
ADD run.sh /tmp/run.sh  
RUN chmod u+x /tmp/run.sh  
  
# Install Vim and Emacs  
RUN apt-get install -y vim  
RUN apt-get install -y emacs  
  
RUN apt-get install -y openssh-server  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/^#PasswordAuthentication/PasswordAuthentication/'
/etc/ssh/sshd_config  
RUN sed -ri 's/^PasswordAuthentication no/PasswordAuthentication yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
# start run!  
CMD ["./tmp/run.sh"]  
  


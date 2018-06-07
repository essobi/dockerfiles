FROM ubuntu:16.04  
ENV PORT 22  
ENV FULL_IF_OLDER_THAN 10D  
ENV REMOVE_ALL_BUT_N_FULL 15  
ENV REMOVE_ALL_INC_OF_BUT_N_FULL 10  
RUN apt-get update  
RUN apt-get install -y duplicity par2 openssh-client python-paramiko python-
gobject-2 python-pexpect  
  
RUN mkdir ~/.ssh  
  
COPY entrypoint /entrypoint  
RUN chmod +x /entrypoint  
ENTRYPOINT ["/entrypoint"]  
  
COPY backup /usr/bin/backup  
RUN chmod +x /usr/bin/backup  
CMD ["/usr/bin/backup"]  
  
COPY list /usr/bin/list  
RUN chmod +x /usr/bin/list  
  
COPY restore /usr/bin/restore  
RUN chmod +x /usr/bin/restore  
  


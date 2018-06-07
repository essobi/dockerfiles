FROM ubuntu:xenial  
  
RUN touch /run.sh  
RUN chmod 755 /run.sh  
RUN echo "#!/bin/bash" >> /run.sh  
RUN echo "groupadd -g 30003 -f test" >> /run.sh  
RUN echo "useradd -d /home/test -m -g test -u \"\$1\" -s /bin/bash test" >>
/run.sh  
RUN echo "su -c \"id\" test" >> /run.sh  
#RUN echo 'rstudio:docker' | chpasswd  
ENTRYPOINT [ "/run.sh" ]  
  
# start as: docker run -it test $(id -u)  


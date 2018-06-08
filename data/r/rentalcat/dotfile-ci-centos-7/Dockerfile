FROM centos:7  
RUN yum install -y make curl git sudo which  
RUN sed -i -e 's/# %wheel\tALL=(ALL)\tNOPASSWD:
ALL/%wheel\tALL=(ALL)\tNOPASSWD: ALL/' /etc/sudoers  
RUN sed -i -e 's/%wheel\tALL=(ALL)\tALL/# %wheel\tALL=(ALL)\tALL/'
/etc/sudoers  
RUN visudo -c  
RUN useradd -m worker -g wheel  
  
WORKDIR /home/worker  
USER worker  


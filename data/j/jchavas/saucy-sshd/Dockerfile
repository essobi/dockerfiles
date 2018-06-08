FROM jchavas/saucy-base  
  
#######################################  
# initialization  
#######################################  
ENV DEBIAN_FRONTEND noninteractive  
  
#######################################  
# ssh server installs  
#######################################  
RUN apt-get install -y openssh-server  
  
EXPOSE 22  
  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN touch /root/.Xauthority  
RUN mkdir -p /root/.ssh  
RUN echo root | awk '{print $1; print $1}' | passwd  
  
#######################################  
# cleaning  
#######################################  
RUN unset DEBIAN_FRONTEND  
  


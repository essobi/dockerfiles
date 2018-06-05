FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y vim git bzip2 sudo  
  
# Create "dev" user with "dev" password and grant passwordless sudo permission  
ENV USERNAME dev  
RUN adduser --disabled-password --gecos '' $USERNAME && \  
echo dev:dev | chpasswd && \  
echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
sudo adduser dev sudo  
  
COPY home/ /home/$USERNAME  
RUN chown -R $USERNAME:$USERNAME /home/$USERNAME  
  
# Mark dev user home as data volume  
VOLUME /home/$USERNAME  
  
USER $USERNAME  
WORKDIR /source  
ENTRYPOINT ["bash"]  


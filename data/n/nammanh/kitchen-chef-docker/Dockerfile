FROM ruby:2.1  
RUN apt-get update  
RUN apt-get install -y sudo openssh-server curl lsb-release wget apt-
transport-https  
RUN apt-get upgrade -y  
  
RUN curl https://omnitruck.chef.io/install.sh | sudo bash -s -- -c current -P
chefdk  
RUN echo 'eval "$(chef shell-init bash)"' >> ~/.bash_profile  
RUN echo 'eval "$(chef shell-init bash)"' >> ~/.bashrc  


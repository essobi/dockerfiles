FROM ubuntu:14.04  
RUN apt-get -q update && \  
apt-get -y install build-essential vim-nox vim-doc git bash-completion
python3-pip && \  
pip3 install virtualenv && pip3 install virtualenvwrapper && \  
useradd dev --comment "Software development user." \--create-home --shell
/bin/bash && \  
mkdir /home/dev/.vim /home/dev/project -p && \  
echo ". /etc/bash_completion" >> /home/dev/.bashrc  
COPY vimrc /home/dev/.vimrc  
RUN chown -R dev:dev /home/dev/  
WORKDIR /home/dev/project  
CMD su dev  


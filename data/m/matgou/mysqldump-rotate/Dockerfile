from mariadb:latest  
  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install -y \  
less \  
man \  
ssh \  
python \  
jq \  
python-pip \  
python-virtualenv \  
vim  
  
RUN adduser --disabled-login --gecos '' aws  
WORKDIR /home/aws  
  
USER aws  
  
RUN \  
mkdir aws && \  
virtualenv aws/env && \  
./aws/env/bin/pip install awscli && \  
echo 'source $HOME/aws/env/bin/activate' >> .bashrc && \  
echo 'complete -C aws_completer aws' >> .bashrc  
  
ADD backup.sh /  
  
CMD /backup.sh  


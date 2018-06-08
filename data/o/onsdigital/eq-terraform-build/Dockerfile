FROM ubuntu:16.04  
  
RUN apt-get update -y && \  
apt-get install -y git curl unzip  
  
RUN git clone https://github.com/kamatama41/tfenv.git ~/.tfenv && \  
ln -s /root/.tfenv/bin/* /usr/local/bin  
  
RUN apt-get install -y software-properties-common && \  
apt-add-repository ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y ansible


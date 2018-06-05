FROM ubuntu:xenial  
  
RUN apt-get update && \  
apt-get install -y \  
software-properties-common \  
sudo \  
curl \  
wget \  
man-db \  
git-core \  
vim  
  
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb &&
\  
dpkg -i erlang-solutions_1.0_all.deb && \  
rm erlang-solutions_1.0_all.deb && \  
apt-get update && \  
apt-get install -y \  
esl-erlang \  
elixir  
  
RUN useradd -m -G sudo docker  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
USER docker  
  
CMD ["/bin/bash"]  


FROM ubuntu:16.04 as compile  
LABEL maintainer "Corey Ryan Hanson"  
  
#This line is where the required dependencies are downloaded.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
--no-install-recommends -y \  
git \  
ca-certificates \  
build-essential \  
libssl-dev \  
cmake \  
build-essential \  
ca-certificates \  
wget \  
openssl && \  
rm -rf /var/lib/apt/lists/*  
  
#Clones creepMiner and mdcct repositories. Edit out git checkout to try a
later version.  
RUN git clone https://github.com/Creepsky/creepMiner && cd creepMiner && git
checkout 4a2b842aea045a87466768d14c7e363d96e1387a  
RUN git clone https://github.com/Mirkic7/mdcct.git && cd mdcct && git checkout
d75dee6f543a2dd546abb02c7fb0a3fac44af3c9  
  
#Modifies and runs the script to install poco.  
RUN sed -i 's/sudo //g' /creepMiner/install-poco.sh && \  
cd /creepMiner && \  
sh ./install-poco.sh  
  
#Builds creepMiner.  
RUN cd creepMiner && \  
cmake CMakeLists.txt -DNO_GPU=ON && \  
make  
  
#Builds mdcct.  
RUN cd mdcct && \  
make  
  
#Begins stage 2 of image.  
FROM ubuntu:16.04  
#Downloads missing dependencies.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
--no-install-recommends -y \  
sudo \  
openssl && \  
rm -rf /var/lib/apt/lists/*  
  
#Creates unprivileged user.  
ARG docker_root_pass=edmund  
ARG docker_unprivileged_user=creepminer  
ARG docker_unprivileged_pass=booboo  
COPY /create-user.sh /  
RUN chmod +x create-user.sh  
RUN /create-user.sh && \  
rm /create-user.sh  
  
#Copies components.  
COPY \--from=compile /creepMiner/poco-1.7.8p3-all/lib/Linux/x86_64/*
/usr/local/lib/  
COPY \--from=compile /creepMiner/bin home/$docker_unprivileged_user/creepMiner  
COPY \--from=compile /mdcct /home/$docker_unprivileged_user/mdcct  
RUN chown -R $docker_unprivileged_user /home  
  
USER $docker_unprivileged_user  
WORKDIR /home/$docker_unprivileged_user  


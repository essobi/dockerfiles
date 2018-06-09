FROM kaixhin/torch:latest  
  
MAINTAINER Toshihiko Yanase <toshihiko.yanase@gmail.com>  
  
# install jdk8  
# This code is from https://github.com/smaliarov/docker-ubuntu-14.04-oracle-
jdk8  
RUN apt-get update \  
# install software-properties-common so that you have add-apt-repository  
&& apt-get install -y software-properties-common \  
# add repository for Oracle JDK  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
# auto accept oracle jdk license  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
# install Oracle JDK8  
&& apt-get install -y oracle-java8-installer  
  
# set PATH  
# This line is from Dockerfile of kaixhin/torch  
ENV PATH=/root/torch/install/bin:$PATH \  
LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH \  
DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH  
  
RUN luarocks install nngraph  
RUN cd /root && git clone https://github.com/stanfordnlp/treelstm.git  
WORKDIR /root/treelstm  


FROM ubuntu:trusty  
MAINTAINER dopin "dopinninja@gmail.com"  
RUN locale-gen en_US en_US.UTF-8  
  
RUN apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install \  
build-essential \  
curl \  
git-core \  
libcurl4-openssl-dev \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
zlib1g-dev \  
libffi-dev  
  
RUN useradd -d /home/wee -m -s /bin/bash -l wee  
USER wee  
WORKDIR /home/wee  
RUN git clone https://github.com/riywo/anyenv /home/wee/.anyenv  
RUN echo 'export HOME="/home/wee"' >> /home/wee/.bash_profile  
RUN echo 'export LANG="en_US.UTF-8"' >> /home/wee/.bash_profile  
RUN echo 'export LC_ALL="en_US.UTF-8"' >> /home/wee/.bash_profile  
RUN echo 'export PATH="/home/wee/.anyenv/bin:$PATH"' >>
/home/wee/.bash_profile  
RUN echo 'eval "$(anyenv init -)"' >> /home/wee/.bash_profile  
RUN export PATH="/home/wee/.anyenv/bin:$PATH"  
RUN eval "$(/.anyenv/bin/anyenv init -)"  
RUN /bin/bash -l -c 'mkdir -p $(anyenv root)/plugins'  
RUN /bin/bash -l -c 'git clone https://github.com/znz/anyenv-update.git
$(anyenv root)/plugins/anyenv-update'  
  
USER root  
RUN chown -R wee:wee /home/wee  


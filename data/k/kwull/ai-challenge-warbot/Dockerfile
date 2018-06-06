# DOCKER-VERSION 1.2.0  
# overwrite entry point  
# docker run --entrypoint="/bin/bash" -i -t -v /home/vagrant/aichallenge-
synced/Backend/AiDaemon/bots/user-0-bot:/code:rw kwull/ai-challenge-warbot -c
/bin/bash  
FROM ubuntu:14.04  
# Set the env variables to non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
ENV TERM linux  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
#add ppas and repositories  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono-xamarin.list  
  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN add-apt-repository -y ppa:brightbox/ruby-ng  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN add-apt-repository -y ppa:cwchien/gradle  
RUN apt-get update  
  
#install nodejs  
RUN apt-get install -y nodejs  
  
#install mono 3.10-xamarin  
RUN apt-get install -y mono-devel  
#RUN mozroots --import --sync --machine  
#install java  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo
debconf-set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-
set-selections  
RUN apt-get install -y oracle-java8-installer  
# install gradle for Java Runner  
RUN apt-get install -y gradle  
  
#install ruby  
RUN apt-get install -y ruby2.1 ruby2.1-dev  
  
ADD entrypoint.sh entrypoint.sh  
  
VOLUME ["/code"]  
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]  


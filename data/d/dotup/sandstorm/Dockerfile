FROM ubuntu  
MAINTAINER live@dotup.de  
EXPOSE 6080  
RUN apt-get update && apt-get -y install curl xz-utils gnupg wget  
  
#RUN groupadd -r sandstorm && useradd --no-log-init -r -g sandstorm sandstorm  
RUN adduser --disabled-password sandstorm  
  
RUN mkdir /sandstorm && chown sandstorm:sandstorm /sandstorm  
USER sandstorm  
ENV HOME /home/sandstorm  
ENV USER sandstorm  
  
WORKDIR /sandstorm  
  
#get the install script  
RUN wget https://raw.githubusercontent.com/sandstorm-
io/sandstorm/master/install.sh  
  
#add it to the current container  
#ADD ./install.sh /install.sh  
RUN bash install.sh -d -e -u  
RUN echo 'export PATH=$PATH:$HOME' >> $HOME/.bashrc  
  
CMD /home/sandstorm/sandstorm/sandstorm start && sleep infinity


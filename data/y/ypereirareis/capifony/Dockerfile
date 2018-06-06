FROM ruby:2.3.1  
RUN apt-get update && apt-get install -yy \  
rubygems \  
git \  
curl \  
libgcrypt11-dev \  
zlib1g-dev \  
ssh  
  
RUN gem install bundler  
  
ENV CAP_USER capifony  
ENV HOME /home/$CAP_USER  
ENV PROJECT_DIR $HOME/project  
ENV GEMS_RELATIVE_PATH .gems  
  
RUN useradd -ms /bin/bash $CAP_USER  
  
ADD ./start.sh $HOME/start.sh  
RUN chmod +x $HOME/start.sh  
RUN mkdir -p $PROJECT_DIR  
  
USER $CAP_USER  
WORKDIR $HOME  
  
ENTRYPOINT ["/home/capifony/start.sh"]  
CMD ["-h"]  
  


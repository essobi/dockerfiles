FROM httplab/ruby-dev:2.2  
RUN apt-get update -qq && apt-get install -y locales  
  
ENV LOCALE=en_US.UTF-8  
ENV LANGUAGE=$LOCALE  
ENV LANG=$LOCALE  
ENV LC_ALL=$LOCALE  
  
RUN dpkg-reconfigure -f noninteractive locales && \  
locale-gen $LOCALE && \  
/usr/sbin/update-locale LANG=$LOCALE  
  
RUN gem update --system $RUBYGEMS_VERSION  
RUN gem install bundler  
  
ENV USER apps  
ENV APP app  
  
ENV GEM_HOME /.gem  
ENV PATH $GEM_HOME/bin:$PATH  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev sudo
vim  
  
ENV HOME /home/$USER  
RUN adduser --disabled-password --gecos '' $USER  
RUN adduser $USER sudo  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
RUN mkdir -p $GEM_HOME && chown -R $USER $GEM_HOME  
  
RUN mkdir $HOME/$APP  
WORKDIR $HOME/$APP  
  
RUN chown $USER:$USER $HOME/$APP && \  
chown -R $USER:$USER /usr/local/lib/ruby/gems/$RUBY_MAJOR.0/doc  
  
RUN adduser $USER root  
  
ENV TZ=Europe/Moscow  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  


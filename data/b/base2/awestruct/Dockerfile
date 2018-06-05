FROM ruby:2.3.1  
# install the required dependencies to complile natice extensions  
# RUN dnf -y install gcc-c++ make ruby-devel libxml2-devel libxslt-devel
findutils git ruby  
RUN groupadd -r dev && useradd -g dev -u 1000 dev  
RUN mkdir -p /home/dev  
RUN chown dev:dev /home/dev  
  
# From here we run everything as dev user  
USER dev  
  
# Setup all the env variables needed for ruby  
ENV HOME /home/dev  
ENV GEM_HOME $HOME/.gems  
ENV GEM_PATH $HOME/.gems  
ENV PATH $PATH:$GEM_HOME/bin  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN mkdir $HOME/.gems  
ADD Gemfile /tmp/Gemfile  
RUN gem install -N rake bundler  
  
RUN cd /tmp && bundle config build.nokogiri --use-system-libraries && bundle
install  
  
EXPOSE 4242  
VOLUME $HOME/website  
WORKDIR $HOME/website  
  
ENTRYPOINT ["awestruct"]  
  
CMD ["--help"]  


FROM iconoeugen/fedora-dev:latest  
MAINTAINER info@vlad.eu  
  
# install things globally, for great justice  
ENV GEM_HOME $HOME/.gem  
ENV PATH $GEM_HOME/bin:$PATH  
  
# don't create ".bundle" in all our apps  
ENV BUNDLE_APP_CONFIG $GEM_HOME  
  
# skip installing gem documentation  
RUN echo 'install: --no-document\nupdate: --no-document' >> "$HOME/.gemrc"  
  
RUN dnf -y install ruby ruby-devel \  
&& dnf clean all  
  
RUN gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
CMD [ "irb" ]


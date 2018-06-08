FROM buildpack-deps:jessie  
  
RUN apt-get update && apt-get install -y rbenv ruby-build  
RUN mkdir /root/.rbenv  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
RUN echo 'eval "$(rbenv init -)"' >> "$HOME/.bashrc"  
  
CMD 'bash'  


FROM buildpack-deps:jessie  
  
RUN git clone https://github.com/sstephenson/ruby-build.git  
RUN cd ruby-build && ./install.sh  
RUN rm -rf /ruby-build  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
CMD 'bash'  


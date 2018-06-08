FROM sailor/ruby-build:latest  
  
RUN ruby-build 1.9.3-p551 /usr/local/ruby-1.9.3-p551  
ENV PATH /usr/local/ruby-1.9.3-p551/bin:$PATH  
RUN gem install bundler  
  
CMD 'irb'  


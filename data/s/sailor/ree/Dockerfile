FROM sailor/ruby-build:latest  
  
RUN CONFIGURE_OPTS=--no-tcmalloc ruby-build ree-1.8.7-2012.02
/usr/local/lib/ruby  
RUN ln -s /usr/local/lib/ruby/bin/* /usr/local/bin  
  
CMD 'irb'  


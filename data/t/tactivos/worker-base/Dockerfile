FROM ruby:2.3.1  
ENV TERM=xterm \  
LANG=C.UTF-8  
COPY ["install_phantomjs.sh", "/usr/src/"]  
  
WORKDIR /usr/src  
  
# Install PhantomJS for rasterising  
ENV PATH=/usr/vendor/phantomjs/bin:$PATH  
  
RUN ./install_phantomjs.sh /usr /tmp  


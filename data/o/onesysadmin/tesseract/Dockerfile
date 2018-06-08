FROM ubuntu:trusty  
  
RUN apt-get install -qq -y libpng12-0 libjpeg62 libjpeg8 libtiff5  
  
ADD vendor/build/usr-local.tar.gz /  
  
RUN ldconfig  


FROM ubuntu:14.04  
MAINTAINER Nathan Hopkins <natehop@gmail.com>  
  
ENV HOME /root  
ADD assets /opt/hopsoft/ruby-mri  
RUN /opt/hopsoft/ruby-mri/build  
ENV PATH /usr/local/ruby/bin:/usr/local/ruby/gems/bin:$PATH  


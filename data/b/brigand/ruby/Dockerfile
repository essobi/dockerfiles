FROM gliderlabs/alpine  
MAINTAINER Frankie Bagnardi <f.bagnardi@gmail.com>  
  
ADD config/gemrc /etc/gemrc  
  
RUN apk update && apk add ruby-bundler  
RUN echo "export PATH=$PATH:/usr/lib/ruby/gems/2.0.0/bin" >
/etc/profile.d/rubygems.sh  
  
CMD ["/bin/sh"]  


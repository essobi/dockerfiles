FROM ubuntu  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install python g++ make checkinstall git autoconf
libncurses5-dev openssl libxml2-utils xsltproc fop man lynx nginx  
RUN git clone https://github.com/erlang/otp.git  
RUN cd otp && git checkout OTP-17.0.2 && /otp/otp_build autoconf &&
./configure && make && make install-docs && make install  


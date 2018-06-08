FROM muli/ubuntu-dev  
  
RUN cd /opt && git clone https://github.com/mli/parameter_server.git  
RUN cd /opt/parameter_server && ln -s /usr/local third_party \  
&& make STATIC_THIRD_LIB=1 -j8 && ln -s /opt/parameter_server/build /build  


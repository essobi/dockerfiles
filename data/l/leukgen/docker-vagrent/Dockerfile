FROM ubuntu:16.04  
LABEL maintainers="Juan S. Medina <https://github.com/jsmedmar>"  
  
# install all dependencies in OPT  
ENV OPT /opt/bundle  
ENV PATH $OPT/bin:$PATH  
ENV PERL5LIB $OPT/lib/perl5:$PERL5LIB  
ENV VERSION v3.3.0  
# install dependencies  
COPY ./build/install_dependencies.sh /tmp  
RUN bash /tmp/install_dependencies.sh  
  
# set locale  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# create a /ifs volume for MSK users  
VOLUME /ifs  
VOLUME /data  
  
# set entry point  
ENTRYPOINT [ "AnnotateVcf.pl" ]  


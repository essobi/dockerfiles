FROM python:3.6.4-jessie  
  
LABEL maintainers="Juan S. Medina <https://github.com/jsmedmar>, Juan E.
Arango <https://github.com/juanesarango>"  
  
# install all dependencies in OPT  
ENV OPT /opt/bundle  
ENV PATH $OPT/bin:$PATH  
ENV PERL5LIB $OPT/lib/perl5:$PERL5LIB  
ENV VERSION 5.2.2  
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
ENTRYPOINT [ "cgpVaf.pl" ]  


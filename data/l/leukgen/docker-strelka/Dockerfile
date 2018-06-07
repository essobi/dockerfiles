FROM python:2.7-jessie  
  
LABEL maintainers="Joe Zhou <https://github.com/zhouyangyu>"  
  
# install all dependencies in OPT  
ENV MANTA /opt/manta  
ENV STRELKA /opt/strelka  
ENV PATH $MANTA/bin:$PATH  
ENV PATH $STRELKA/bin:$PATH  
  
# set locale  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Strelka specific env variables  
ENV CC /usr/bin/gcc-4.9  
ENV CXX /usr/bin/g++-4.9  
# install dependencies  
COPY ./build/install_dependencies.sh /tmp  
RUN bash /tmp/install_dependencies.sh  
  
# create a /ifs volume for MSK users  
VOLUME /ifs  
VOLUME /data  
  


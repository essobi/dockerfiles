######################################################  
# Base image with all of Grappa's dependencies  
######################################################  
FROM ubuntu  
MAINTAINER Grappa Team <grappa@cs.washington.edu>  
  
ADD install_dependencies.sh /install_dependencies.sh  
RUN bash /install_dependencies.sh && rm /install_dependencies.sh  
  
RUN git clone https://github.com/uwsampa/grappa.git /grappa  
WORKDIR /grappa  
  
RUN cd /grappa && \  
./configure --cc=$(which gcc) --gen=Ninja \  
\--third-party=/grappa-third-party && \  
cd build/Ninja+Release && \  
ninja  
  
ADD setup_environment.sh /setup_environment.sh  
RUN bash /setup_environment.sh && rm /setup_environment.sh  
  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib  
ENV CC /usr/bin/gcc  
ENV CXX /usr/bin/g++  
ENV GRAPPA_THIRD_PARTY /grappa-third-party  
ENV GRAPPA_ALLOW_RUN_AS_ROOT 1  
# expose the source code directory for mounting in other containers  
# (such as sharing with the host)  
VOLUME /grappa  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["--login"]  


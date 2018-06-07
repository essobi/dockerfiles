FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y cmake  
RUN apt-get install -y doxygen \  
flex \  
bison  
RUN apt-get install -y git  
RUN apt-get install -y g++  
RUN apt-get install -y python  
ENV DOXYGEN_PATH /opt/doxygen-latest  
RUN git clone https://github.com/doxygen/doxygen.git && cd doxygen && mkdir
build && cd build && cmake -DCMAKE_INSTALL_PREFIX=${DOXYGEN_PATH} .. && make
install && cd ../../ && rm -rf doxygen  
ENV PATH ${DOXYGEN_PATH}/bin:${PATH}  
RUN apt-get install -y texlive-latex-base  
RUN apt-get install -y ghostscript  
RUN apt-get install -y zsh  


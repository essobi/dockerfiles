FROM debian:jessie  
MAINTAINER Jon Malmaud (malmaud@gmail.com)  
WORKDIR /  
RUN apt-get update && apt-get install -y \  
clang-3.5 \  
gfortran \  
git \  
perl \  
m4 \  
wget \  
cmake \  
libssl-dev \  
python2.7 \  
libncurses5-dev \  
libedit-dev  
EXPOSE 8000  
VOLUME /data  
WORKDIR /usr/bin  
RUN rm -rf gcc g++  
RUN ln -s clang-3.5 gcc  
RUN ln -s clang-3.5 g++  
WORKDIR /  
RUN git clone https://github.com/JuliaLang/julia.git  
WORKDIR /julia  
RUN git checkout 930e6b55327c6caf60d0eae4d71ffdf43e55fbae  
ADD Make.user Make.user  
RUN make  
ENTRYPOINT ["/julia/julia"]  


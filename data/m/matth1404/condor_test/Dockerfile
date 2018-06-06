FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y cmake  
RUN apt-get install -y build-essential  
RUN apt-get install -y libboost-thread-dev  
RUN apt-get install -y libpcre++-dev  
RUN apt-get install -y libxml2-dev  
RUN apt-get install -y libcurl4-openssl-dev  
RUN apt-get install -y libpam0g-dev  
RUN apt-get install -y libc-ares-dev  
RUN apt-get install -y libldap2-dev  
RUN apt-get install -y uuid-dev  
RUN apt-get install -y libbison-dev  
RUN apt-get install -y flex  
RUN apt-get install -y libltdl3-dev  
RUN apt-get install -y libexpat1-dev  
RUN apt-get install -y expat  
RUN apt-get install -y autoconf  
RUN apt-get install -y gawk  
RUN apt-get install -y python-dev  
RUN apt-get install -y libxslt-dev  
RUN apt-get install -y libboost-python-dev  
RUN apt-get install -y libx11-dev  
RUN apt-get install -y curl  
  
RUN mkdir -p /usr/src/condor  
COPY . /usr/src/condor  
WORKDIR /usr/src/condor  
  
RUN cmake .  
RUN make  
RUN make install  
  
ENV PATH =
$PATH:/usr/src/condor/release_dir/bin/:/usr/src/condor/release_dir/sbin/  
RUN useradd condor  
RUN curl -sSL https://get.docker.com/ | sh  
RUN usermod -G docker condor  
  


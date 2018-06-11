FROM ubuntu:14.04  
RUN apt-get update -qq  
  
RUN apt-get install -qqy automake  
RUN apt-get install -qqy libcurl4-openssl-dev  
RUN apt-get install -qqy git  
RUN apt-get install -qqy make  
  
RUN git clone https://github.com/pooler/cpuminer  
  
RUN cd cpuminer && ./autogen.sh  
RUN cd cpuminer && ./configure CFLAGS="-O3"  
RUN cd cpuminer && make  
  
WORKDIR /cpuminer  
ENTRYPOINT ["./minerd"]  


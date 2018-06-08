FROM ubuntu:16.04  
MAINTAINER Keisuke Mutoh  
  
ENTRYPOINT ["/bin/bash"]  
WORKDIR /root  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y install build-essential  
RUN apt-get -y install git  
RUN apt-get -y install ruby-dev  
RUN apt-get -y install zlib1g-dev fontforge  
RUN git clone https://github.com/bramstein/sfnt2woff-zopfli.git sfnt2woff-
zopfli && cd sfnt2woff-zopfli && make && mv sfnt2woff-zopfli
/usr/local/bin/sfnt2woff  
RUN git clone \--recursive https://github.com/google/woff2.git && cd woff2 &&
make clean all && mv woff2_compress /usr/local/bin/ && mv woff2_decompress
/usr/local/bin/  
RUN gem install fontcustom  


FROM ubuntu:16.04  
MAINTAINER Jonathan Brooker <jonathan.brooker@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends wget rsync cmake binutils make
\  
pkg-config perl-modules libdigest-md5-file-perl xz-utils python \  
clang clang-tidy clang-format \  
&& apt-get -y autoremove \  
&& apt-get -y clean  
  
ENTRYPOINT [ "bash" ]  


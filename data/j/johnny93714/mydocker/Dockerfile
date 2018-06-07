FROM ubuntu:xenial  
MAINTAINER johnny93714 <johnny93714@gmail.com>  
  
RUN cd /bin \  
&& ln -sf bash sh  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
vim \  
subversion  
  
EXPOSE 80  
CMD ["/bin/bash"]  
  


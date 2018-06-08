# Version: 0.0.1  
FROM ubuntu:18.04  
MAINTAINER Mingshan Lin "yakel@126.com"  
# prepare for compiling environments  
RUN apt-get update \  
&& apt-get install -y gcc \  
gdb \  
make \  
git \  
&& apt-get clean \  
# download the source code for the overshadow project  
&& git clone https://github.com/yakelms/overshadow.git ~/overshadow \  
# build and test  
&& make test -C ~/overshadow \  
# build again  
&& make -C ~/overshadow \  
# install  
&& cp ~/overshadow/overshadow /usr/local/bin  
CMD ["/bin/bash"]  


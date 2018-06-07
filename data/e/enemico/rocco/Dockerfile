FROM centos:7  
RUN yum -y update  
  
RUN yum -y install zsh useradd epel-release yum-utils git cmake cmake3 make
gcc gcc-c++  
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm  
RUN yum -y update  
RUN yum -y install libuv-static libstdc++-static  
RUN yum -y install python36u  
RUN python3.6 -V  
RUN yum -y install python36u-pip  
RUN pip3.6 install virtualenv  
  
RUN rm -f /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Oslo /etc/localtime  
RUN useradd -ms /usr/bin/zsh rocco  
  
USER rocco  
WORKDIR /home/rocco  
  
RUN git clone https://github.com/xmrig/xmrig.git  
RUN mkdir /home/rocco/xmrig/build  
COPY ./service/donate.h /home/rocco/xmrig/src/  
USER root  
RUN cd /home/rocco/xmrig/build && cmake .. -DCMAKE_BUILD_TYPE=Release
-DUV_LIBRARY=/usr/lib64/libuv.a -DWITH_HTTPD=OFF  
RUN cd /home/rocco/xmrig/build && make  
RUN chmod o+x /home/rocco/xmrig/build/xmrig  
  
COPY ./service service  
USER rocco  
WORKDIR /home/rocco  
CMD ./service/rocco.py  


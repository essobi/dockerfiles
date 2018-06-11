FROM centos  
  
RUN yum update -y && yum install -y \  
tar \  
bzip2 \  
wget \  
cmake \  
make \  
gcc \  
gcc-c+\+ \  
&& cd ~ && wget
http://pkgs.fedoraproject.org/repo/pkgs/opencv/OpenCV-2.4.3.tar.bz2/c0a5af4ff9d0d540684c0bf00ef35dbe/OpenCV-2.4.3.tar.bz2
\  
&& tar jxvf OpenCV-2.4.3.tar.bz2 \  
&& cd OpenCV-2.4.3 && mkdir build \  
&& cd build && cmake -D CMAKE_BUILD_TYPE=RELEASE -D
CMAKE_INSTALL_PREFIX=/usr/local .. \  
&& make && make install \  
&& echo '/usr/local/lib' >> /etc/ld.so.conf.d/opencv.conf && ldconfig \  
&& rm -rf ~/OpenCV-2.4.3 ~/OpenCV-2.4.3.tar.bz2 \  
&& cd ~ && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \  
&& python get-pip.py && rm -f get-pip.py \  
&& yum install -y \  
zlib-devel \  
libjpeg-devel \  
python-devel  
  
WORKDIR /root/  
EXPOSE 80  
  
CMD /bin/bash


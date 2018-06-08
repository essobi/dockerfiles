FROM ubuntu  
MAINTAINER moremagic <itoumagic@gmail.com>  
  
RUN apt-get update && apt upgrade -y && apt-get install -y openssh-server
openssh-client  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# python2 + opencv install  
RUN apt-get install -y wget curl tar zip gcc make g++  
RUN apt-get install -y python2.7-dev python-numpy python-scipy python-opencv
libfreetype6-dev libxft-dev libopencv-dev  
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | /usr/bin/python2.7  
RUN python2 -m pip install ipykernel  
RUN python2 -m pip install pandas  
RUN python2 -m pip install matplotlib  
RUN python2 -m pip install networkx  
RUN python2 -m pip install pyyaml  
RUN python2 -m pip install xlsxwriter  
RUN python2 -m pip install tornado  
RUN python2 -m pip install pillow  
RUN python2 -m pip install opencv-python  
RUN python2 -m pip install scipy  
# http://qiita.com/youhei_nakagawa/items/1e40417fb94d4f8ffe62  
RUN ln /dev/null /dev/raw1394  
  
# python3 install  
RUN apt-get install -y python3-dev  
  
# jupyter install  
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python3  
RUN pip install jupyter ipython[notebook]  
RUN python3 -m pip install ipykernel  
RUN python3 -m pip install pandas  
RUN python3 -m pip install matplotlib  
RUN python3 -m pip install networkx  
RUN python3 -m pip install pyyaml  
RUN python3 -m pip install xlsxwriter  
RUN python3 -m pip install tornado  
RUN python3 -m pip install pillow  
RUN python3 -m pip install opencv-python  
RUN python3 -m pip install scipy  
# opencv3 install  
RUN apt-get install -y cmake libavcodec-dev libavformat-dev libswscale-dev
libv4l-dev libatlas-base-dev gfortran libgtk2.0-dev  
RUN wget https://github.com/Itseez/opencv/archive/3.4.0.zip && unzip 3.4.0.zip  
WORKDIR /opencv-3.4.0/build  
RUN cmake .. \  
-D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D BUILD_opencv_java=OFF \  
-D WITH_IPP=OFF \  
-D PYTHON_EXECUTABLE=/usr/bin/python3.4 .. \  
&& make -j4 \  
&& make install  
  
# kernel install  
RUN ipython2 kernel install --name python2  
RUN ipython3 kernel install --name python3  
  
RUN printf '#!/bin/bash \n\  
jupyter notebook --ip=0.0.0.0 --allow-root --notebook-dir=/root >
/var/log/notebook.log & \n\  
/usr/sbin/sshd -D \n\  
tail -f /var/null \n\  
' >> /etc/service.sh \  
&& chmod +x /etc/service.sh  
  
EXPOSE 22 8888  
CMD ["/etc/service.sh"]  


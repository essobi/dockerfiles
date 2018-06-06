FROM phusion/baseimage:0.9.19  
CMD ["/sbin/my_init"]  
  
RUN apt update && \  
apt install -y --force-yes build-essential cmake git libgtk2.0-dev libavcodec-
dev libavformat-dev libswscale-dev \  
libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev
libdc1394-22-dev \  
python3-dev python3-tk python3-numpy libtesseract-dev libleptonica-dev
libcurl4-openssl-dev liblog4cplus-dev wget && \  
apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir ~/opencv  
  
RUN cd ~/opencv && git clone https://github.com/Itseez/opencv.git && cd opencv
&& git checkout 3.0.0  
  
RUN cd ~/opencv/opencv && mkdir release && cd release && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python3 -c "import
sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..  
  
RUN cd ~/opencv/opencv/release && make && make install  
  
RUN mkdir ~/openalpr  
  
RUN cd ~/openalpr && git clone https://github.com/openalpr/openalpr.git  
  
RUN cd ~/openalpr/openalpr/src && mkdir build && cd build && cmake
-DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..  
  
RUN cd ~/openalpr/openalpr/src/build && make && make install  
  
RUN cp -R /usr/lib/python2.7/dist-packages/openalpr /usr/lib/python3.5/dist-
packages/  


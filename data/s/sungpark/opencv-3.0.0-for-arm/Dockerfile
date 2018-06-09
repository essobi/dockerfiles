FROM sungpark/opencv-3.0.0-src-for-arm  
  
RUN [ "cross-build-start" ]  
  
RUN cd /root/opencv/opencv-3.0.0 \  
&& mkdir release \  
&& cd release \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D
BUILD_PYTHON_SUPPORT=ON -D BUILD_NEW_PYTHON_SUPPORT=ON ..  
RUN cd /root/opencv/opencv-3.0.0/release && make && make install  
  
RUN [ "cross-build-end" ]  


FROM rudyryk/alpine-opencv:base-python3.6  
  
RUN mkdir /opt && cd /opt && \  
wget https://github.com/opencv/opencv/archive/3.2.0.zip && \  
unzip 3.2.0.zip && rm 3.2.0.zip && \  
wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip && \  
unzip 3.2.0.zip && rm 3.2.0.zip \  
&& \  
cd /opt/opencv-3.2.0 && mkdir build && cd build && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_C_COMPILER=/usr/bin/clang \  
-D CMAKE_CXX_COMPILER=/usr/bin/clang++ \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_PYTHON_EXAMPLES=OFF \  
-D INSTALL_C_EXAMPLES=OFF \  
-D WITH_FFMPEG=ON \  
-D BUILD_PERF_TESTS=OFF \  
-D BUILD_TESTS=OFF \  
-D OPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib-3.2.0/modules \  
-D PYTHON_EXECUTABLE=/usr/local/bin/python \  
.. && \  
make -j$(nproc) && make install && cd .. && rm -rf build && \  
cp -p $(find /usr/local/lib/python3.6/site-packages -name cv2.*.so) \  
/usr/local/lib/python3.6/site-packages/cv2.so  
  
CMD ["python", "-c", "'import cv2; print(\"Python: import cv2 - SUCCESS\")'"]  


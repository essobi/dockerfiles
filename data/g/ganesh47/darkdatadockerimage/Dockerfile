FROM debian  
ENV LANG C.UTF-8  
RUN apt-get -qq update  
RUN apt-get -qq -y install cmake python3 libpng12-dev libjpeg62-turbo-dev \  
libtiff5-dev automake checkinstall git build-essential \  
libtool libleptonica-dev tesseract-ocr-dev tesseract-ocr \  
libopencv-dev python3-pip python3-numpy \  
gfortran libopenblas-dev liblapack-dev python3-pil  
RUN cd ~  
RUN git clone https://github.com/opencv/opencv_contrib.git  
RUN mkdir ~/opencv  
RUN cd ~/opencv  
RUN git clone https://github.com/opencv/opencv.git  
WORKDIR opencv  
WORKDIR opencv  
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_C_EXAMPLES=OFF \  
-D INSTALL_PYTHON_EXAMPLES=OFF \  
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \  
-D BUILD_EXAMPLES=OFF .. \  
-D BUILD_TESTS=OFF .. \  
-D BUILD_PERF_TESTS=OFF ..  
RUN make -j4  
RUN make -j4 install  
RUN ln /dev/null /dev/raw1394  
RUN pip3 install -vU setuptools  
RUN pip3 install -vU jupyter  
RUN pip3 install -vU scipy  
RUN pip3 install -vU pytesseract  
RUN pip3 install -vU tesserpy


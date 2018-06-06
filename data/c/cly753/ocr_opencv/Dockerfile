# https://realpython.com/blog/python/setting-up-a-simple-ocr-server/  
# start with a base image  
FROM ubuntu:14.04  
# install dependencies  
RUN apt-get update && apt-get install -y autoconf automake libtool g++ git
cmake wget python python-pip python2.7-dev build-essential vim sed && apt-get
clean  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg62-dev && apt-get
clean  
RUN apt-get update && apt-get install -y libtiff4-dev && apt-get clean  
RUN apt-get update && apt-get install -y libopencv-dev libtesseract-dev
libleptonica-dev && apt-get clean  
RUN apt-get update && apt-get install -y liblog4cplus-dev && apt-get clean  
# RUN apt-get install -y libcurl3-dev && apt-get clean # installed by above
dependency  
RUN apt-get update && apt-get install -y tk8.5 tcl8.5 tk8.5-dev tcl8.5-dev &&
apt-get clean  
RUN apt-get update && apt-get build-dep -y python-imaging --fix-missing &&
apt-get clean  
RUN apt-get update && apt-get install -y imagemagick && apt-get clean  
  
# build leptonica  
RUN wget http://www.leptonica.org/source/leptonica-1.70.tar.gz \  
&& tar -zxvf leptonica-1.70.tar.gz \  
&& rm leptonica-1.70.tar.gz  
WORKDIR leptonica-1.70/  
RUN ./autobuild  
RUN ./configure  
RUN make \  
&& make install  
RUN ldconfig  
  
# build tesseract  
# and  
# download the relevant Tesseract English Language Packages  
WORKDIR /  
RUN wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.02.tar.gz \  
&& tar -zxvf tesseract-ocr-3.02.02.tar.gz \  
&& rm tesseract-ocr-3.02.02.tar.gz \  
&& wget https://tesseract-ocr.googlecode.com/files/tesseract-
ocr-3.02.eng.tar.gz \  
&& tar -xf tesseract-ocr-3.02.eng.tar.gz \  
&& rm tesseract-ocr-3.02.eng.tar.gz \  
&& cp -r tesseract-ocr/tessdata /usr/local/share/  
WORKDIR tesseract-ocr/  
RUN ./autogen.sh  
RUN ./configure  
RUN make \  
&& make install  
RUN ldconfig  
  
# python opencv start  
#
http://docs.opencv.org/3.0-beta/doc/tutorials/introduction/linux_install/linux_install.html  
# http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-
python-2-7-on-ubuntu/  
WORKDIR /  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-
dev \  
python-dev python-numpy \  
libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev
libdc1394-22-dev \  
&& apt-get clean  
# for docker hub continuous build  
RUN wget -O opencv-3.1.0.tar.gz
https://github.com/Itseez/opencv/archive/3.1.0.tar.gz \  
&& tar -zxvf opencv-3.1.0.tar.gz \  
&& rm opencv-3.1.0.tar.gz \  
&& wget -O opencv_contrib-3.1.0.tar.gz
https://github.com/Itseez/opencv_contrib/archive/3.1.0.tar.gz \  
&& tar -zxvf opencv_contrib-3.1.0.tar.gz \  
&& rm opencv_contrib-3.1.0.tar.gz  
# for local  
# be careful about the permission of the folder copied  
# COPY opencv-3.1.0 /opencv-3.1.0  
# COPY opencv_contrib-3.1.0 /opencv_contrib-3.1.0  
RUN mkdir /opencv-3.1.0/build  
WORKDIR /opencv-3.1.0/build  
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_C_EXAMPLES=OFF \  
-D INSTALL_PYTHON_EXAMPLES=OFF \  
-D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib-3.1.0/modules \  
-D BUILD_EXAMPLES=OFF ..  
RUN make -j4 \  
&& make install  
RUN ldconfig  
# in place (-i) remove -lippicv flag for linking opencv as it is out-dated  
RUN sed -i 's/ -lippicv / /g' /usr/local/lib/pkgconfig/opencv.pc  
# python opencv end  
# tesseract continue  
# delay to here because COPY will invalidate cache  
WORKDIR /  
COPY requirements.txt /  
RUN pip install -r requirements.txt  
  
CMD ["python", "-c", "import cv2; print('cv2.__version__ = ' +
str(cv2.__version__))"]  


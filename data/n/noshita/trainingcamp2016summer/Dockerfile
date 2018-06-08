From ubuntu:xenial  
MAINTAINER Koji Noshita <noshita@morphometrics.jp>  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y --force-yes build-essential cmake git libgtk2.0-dev pkg-
config libavcodec-dev libavformat-dev libswscale-dev \  
libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev
libdc1394-22-dev python-pip\  
python3-dev python3-tk python3-numpy && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# Use `pip` to make sure latest versions. RUN pip install pyzmq  
RUN pip install numpy  
RUN pip install matplotlib  
RUN pip install pandas  
RUN pip install scipy  
RUN pip install scikit-learn  
RUN pip install networkx  
RUN pip install bokeh  
RUN pip install XlsxWriter  
RUN pip install Sphinx  
RUN pip install ipython  
RUN pip install jupyter  
  
RUN mkdir ~/opencv  
  
RUN cd ~/opencv && git clone https://github.com/Itseez/opencv_contrib.git  
RUN cd ~/opencv && git clone https://github.com/Itseez/opencv.git  
  
RUN cd ~/opencv/opencv && mkdir release && cd release && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \  
-D INSTALL_C_EXAMPLES=ON \  
-D INSTALL_PYTHON_EXAMPLES=ON \  
-D BUILD_EXAMPLES=ON \  
-D WITH_OPENGL=ON \  
-D WITH_V4L=ON \  
-D WITH_XINE=ON \  
-D WITH_TBB=ON ..  
  
RUN cd ~/opencv/opencv/release && make -j $(nproc) && make install  
  
# Add a notebook profile.  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
ENTRYPOINT ["tini", "--"]  
CMD ["jupyter", "notebook", "--no-browser", "--allow-root"]


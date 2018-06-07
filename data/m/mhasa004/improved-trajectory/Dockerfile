FROM ubuntu:12.04  
MAINTAINER Mahmudul Hasan <mhasa004@ucr.edu>  
  
RUN apt-get update  
RUN apt-get remove -y ffmpeg x264 libx264-dev  
  
# update the system so that it can apt-get from the multiverse repository i.e.
libfaac-dev  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise multiverse" >>
/etc/apt/sources.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ precise multiverse" >>
/etc/apt/sources.list  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise-updates multiverse"
>> /etc/apt/sources.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ precise-updates
multiverse" >> /etc/apt/sources.list  
  
RUN apt-get update  
  
# get all the dependencies for x264  
RUN apt-get install -y -q build-essential wget checkinstall git cmake libfaac-
dev \  
libjack-jackd2-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev
\  
libsdl1.2-dev libtheora-dev libva-dev libvdpau-dev libvorbis-dev libx11-dev \  
libxfixes-dev libxvidcore-dev texi2html yasm zlib1g-dev vim locate unzip  
  
# install gstreamer and its dependencies  
RUN apt-get install -y libgstreamer0.10-0 libgstreamer0.10-dev \  
gstreamer0.10-tools gstreamer0.10-plugins-base libgstreamer-plugins-
base0.10-dev \  
gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly gstreamer0.10-plugins-
bad gstreamer0.10-ffmpeg  
  
# download and install vlc  
RUN apt-get install -y vlc vlc-dbg vlc-data libvlccore5 libvlc5 libvlccore-dev
\  
libvlc-dev tbb-examples libtbb-doc libtbb2 libtbb-dev libxine1-bin
libxine1-ffmpeg libxine-dev  
  
# install mysqlc++ client  
RUN apt-get install -y libmysqlcppconn-dev  
  
# download and install x264  
RUN cd /opt && wget
ftp://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-20121004-2245-stable.tar.bz2
\  
&& tar xjvf x264-snapshot-20121004-2245-stable.tar.bz2  
RUN cd /opt/x264-snapshot-20121004-2245-stable \  
&& ./configure --enable-static --enable-pic --enable-shared \  
&& make \  
&& make install  
  
# download ffmepg  
RUN cd /opt && wget
http://lear.inrialpes.fr/people/wang/download/ffmpeg-0.11.1.tar.bz2 \  
&& tar xjvf ffmpeg-0.11.1.tar.bz2  
  
# install ffmpeg  
RUN cd /opt/ffmpeg-0.11.1 \  
&& ./configure --enable-gpl --enable-libfaac --enable-libmp3lame \  
\--enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libtheora \  
\--enable-libvorbis --enable-libx264 --enable-libxvid --enable-nonfree \  
\--enable-postproc --enable-version3 --enable-x11grab --enable-pic \  
\--enable-shared \  
&& make && make install  
  
# install gtk  
RUN apt-get install -y libgtk2.0-0 libgtk2.0-dev libjpeg62 libjpeg62-dev  
  
# download and install v4l  
RUN cd /opt && wget
http://www.linuxtv.org/downloads/v4l-utils/v4l-utils-0.9.1.tar.bz2 \  
&& tar xjvf v4l-utils-0.9.1.tar.bz2 && cd v4l-utils-0.9.1 \  
&& ./configure \  
&& make && make install  
  
# download opencv2.4.2  
RUN cd /opt && wget
http://lear.inrialpes.fr/people/wang/download/OpenCV-2.4.2.tar.bz2 \  
&& tar xjvf OpenCV-2.4.2.tar.bz2  
  
# install opencv2.4.2  
RUN mkdir /opt/OpenCV-2.4.2/build  
RUN cd /opt/OpenCV-2.4.2/build && cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D WITH_TBB=ON -D WITH_XINE=ON -D BUILD_NEW_PYTHON_SUPPORT=ON \  
-D BUILD_EXAMPLES=ON \  
-D INSTALL_PYTHON_EXAMPLES=ON .. \  
&& make && make install  
  
# ldconfig the library path  
RUN echo "/usr/local/lib/" >> /etc/ld.so.conf  
RUN ldconfig  
  
# download improved trajectory  
RUN cd /opt && wget
http://lear.inrialpes.fr/people/wang/download/improved_trajectory_release.tar.gz
\  
&& tar xzvf improved_trajectory_release.tar.gz  
  
# install improved trajectory  
RUN cd /opt/improved_trajectory_release && make \  
&& cp ./release/DenseTrackStab /usr/local/bin  
  
# download stip-2.0  
RUN cd /opt && wget http://www.di.ens.fr/~laptev/download/stip-2.0-linux.zip \  
&& unzip stip-2.0-linux.zip  
RUN cd /opt/stip-2.0-linux/bin && chmod +x stipdet && chmod +x stipshow \  
&& cp stipdet /usr/local/bin && cp stipshow /usr/local/bin  
  
RUN cd /usr/local/lib \  
&& ln -s libopencv_core.so libcxcore.so.2 \  
&& ln -s libopencv_imgproc.so libcv.so.2 \  
&& ln -s libopencv_highgui.so libhighgui.so.2 \  
&& ln -s libopencv_ml.so libml.so.2 \  
&& ln -s libopencv_video.so libcvaux.so.2  
RUN ldconfig  


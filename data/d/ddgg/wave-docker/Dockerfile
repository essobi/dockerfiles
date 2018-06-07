FROM ubuntu:16.04  
RUN mkdir workspace  
WORKDIR workspace  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev
libavformat-dev libswscale-dev  
RUN apt-get install -y python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev
libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev  
  
RUN git clone \--depth=1 https://github.com/Itseez/opencv.git  
RUN rm -rf opencv/.git  
RUN mkdir opencv_build  
WORKDIR opencv_build  
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local
../opencv  
RUN make -j $(($(nproc) + 1))  
RUN make install  
WORKDIR ../  
RUN rm -rf opencv opencv_build  
  
RUN apt-get install -y wget  
RUN wget http://www.fftw.org/fftw-3.3.5.tar.gz  
RUN tar xzf fftw-3.3.5.tar.gz  
WORKDIR fftw-3.3.5/  
RUN ./configure --enable-shared --prefix /usr/local  
RUN make -j $(($(nproc) + 1))  
RUN make install  
WORKDIR ../  
RUN rm -rf fftw-3.3.5*  
  
RUN apt-get install -y libopenmpi-dev  
  
RUN wget
https://sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.tar.gz/download  
RUN mv download boost_1_59_0.tar.gz  
RUN tar xzf boost_1_59_0.tar.gz  
WORKDIR boost_1_59_0  
RUN apt-get install -y libbz2-dev  
RUN ./bootstrap.sh --prefix=/usr/local  
RUN echo "\nusing mpi ;" >> project-config.jam  
RUN ./b2 install -j $(($(nproc) + 1))  
WORKDIR ../  
RUN rm -rf boost*  
  
RUN git clone \--depth=1 https://github.com/boost-experimental/di.git  
RUN rm -rf di/.git  
RUN mv di/include/boost/* /usr/local/include/boost/  
RUN rm -rf di  
  
RUN git clone \--depth=1 https://github.com/google/googletest.git  
RUN rm -rf googletest/.git  
WORKDIR googletest  
RUN mkdir build  
WORKDIR build  
RUN cmake ..  
RUN make -j $(($(nproc) + 1))  
RUN make install  
WORKDIR ../  
WORKDIR ../  
RUN rm -rf googletest  
  
RUN git clone \--depth=1 https://github.com/google/benchmark.git  
WORKDIR benchmark  
RUN mkdir build  
WORKDIR build/  
RUN cmake -DCMAKE_BUILD_TYPE=Release -DBENCHMARK_ENABLE_LTO=true ../  
RUN make -j $(($(nproc) + 1))  
RUN make install  
WORKDIR ../  
WORKDIR ../  
RUN rm -rf benchmark  
  
RUN wget
https://sourceforge.net/projects/tclap/files/tclap-1.2.1.tar.gz/download  
RUN mv download tclap-1.2.1.tar.gz  
RUN tar xzf tclap-1.2.1.tar.gz  
WORKDIR tclap-1.2.1  
RUN ./configure  
RUN make -j $(($(nproc) + 1))  
RUN make install  
WORKDIR ..  
RUN rm -rf tclap-1.2.1*  
  
RUN ldconfig  


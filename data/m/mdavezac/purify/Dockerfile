FROM ipython/scipystack  
  
VOLUME /build  
WORKDIR /build  
  
# install casacore  
RUN apt-get install -y \  
bison libbison-dev wcslib-tools wcslib-dev \  
flex libncurses5-dev libreadline-dev \  
libfftw3-3 libfftw3-dev \  
libcfitsio3-dev libhdf5-dev \  
libgomp1 \  
cmake wget  
  
RUN wget ftp://ftp.atnf.csiro.au/pub/software/casacore/casacore-1.7.0.tar.bz2;
\  
tar -xvf casacore-1.7.0.tar.bz2; \  
mkdir casacore-1.7.0/build && cd casacore-1.7.0/build; \  
cmake -DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=/usr \  
-DCMAKE_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/ \  
-DFFTW3_INCLUDE_DIR=/usr/include \  
-DFFTW3F_LIBRARY=/usr/lib/x86_64-linux-gnu/libfftw3f.so \  
-DFFTW3_LIBRARY=/usr/lib/x86_64-linux-gnu/libfftw3.so \  
-DFFTW3L_LIBRARY=/usr/lib/x86_64-linux-gnu/libfftw3l.so \  
-DFFTW3F_THREAD_LIBRARY=/usr/lib/x86_64-linux-gnu/libfftw3f_omp.so \  
-DFFTW3_THREAD_LIBRARY=/usr/lib/x86_64-linux-gnu/libfftw3_omp.so \  
-DFFTW3L_THREAD_LIBRARY=/usr/lib/x86_64-linux-gnu/libfftw3l_omp.so \  
-DFFTW3_LIBRARIES=/usr/lib/x86_64-linux-gnu/libfftw3.so ..; \  
make -j 2 install;  
  
# install pyrap wrappers  
RUN apt-get install -y subversion libboost-python-dev scons  
RUN svn co http://pyrap.googlecode.com/svn/tags/pyrap-1.1.0; \  
cd pyrap-1.1.0; \  
./batchbuild.py --casacore-root=/usr --prefix=/usr  
  
# install purify  
RUN apt-get install -y libtiff5-dev  
RUN pip2.7 install git+https://github.com/UCL/purify.git@docker  
  
# add an ipython user  
RUN adduser ipython  
# add notebook directory in root  
RUN mkdir /notebooks && chown ipython /notebooks  
  
# add notebook script  
RUN echo "ipython notebook --ip=0.0.0.0 --port=8888 --no-browser" >
/usr/bin/notebook.sh; \  
chmod a+rx /usr/bin/notebook.sh  
  
# Now switch to ipython user  
USER ipython  
  
WORKDIR /notebooks  
RUN git clone https://github.com/UCL/purify.git -b docker; \  
cp purify/scripts/*.ipynb /notebooks; \  
mkdir data; \  
cp -r purify/data/images purify/data/expected data;  
  
CMD /usr/bin/notebook.sh  


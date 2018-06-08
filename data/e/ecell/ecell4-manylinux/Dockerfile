FROM quay.io/pypa/manylinux1_x86_64  
  
#RUN cd; yum update -y; git clone -b 'v4.0.2' --single-branch
git://github.com/ecell/ecell4  
RUN cd; yum update -y; git clone git://github.com/ecell/ecell4  
# Cython  
RUN /opt/python/cp27-cp27mu/bin/python -m pip install cython  
RUN /opt/python/cp35-cp35m/bin/python -m pip install cython  
RUN /opt/python/cp34-cp34m/bin/python -m pip install cython  
  
# config.h and BesselTables  
RUN cd; yum install cmake gsl-devel -y; wget
http://downloads.sourceforge.net/project/boost/boost/1.59.0/boost_1_59_0.tar.gz
https://www.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8.14/bin/linux-
centos5-x86_64-gcc482/hdf5-1.8.14-linux-centos5-x86_64-gcc482-shared.tar.gz;
tar xf hdf5-1.8.14-linux-centos5-x86_64-gcc482-shared.tar.gz; tar xf
boost_1_59_0.tar.gz  
RUN cd /root/ecell4; BOOST_INCLUDEDIR=/root/boost_1_59_0 cmake . #;
CPATH=/root/boost_1_59_0 make BesselTables  
  
# E-Cell4 wheels  
RUN cd /root/ecell4/python; LIBRARY_PATH=/root/hdf5-1.8.14-linux-
centos5-x86_64-gcc482-shared/lib
CPATH=/root/boost_1_59_0:/root/hdf5-1.8.14-linux-
centos5-x86_64-gcc482-shared/include /opt/python/cp27-cp27mu/bin/python
setup.py bdist_wheel  
RUN cd /root/ecell4/python; LIBRARY_PATH=/root/hdf5-1.8.14-linux-
centos5-x86_64-gcc482-shared/lib
CPATH=/root/boost_1_59_0:/root/hdf5-1.8.14-linux-
centos5-x86_64-gcc482-shared/include /opt/python/cp35-cp35m/bin/python
setup.py bdist_wheel  
RUN cd /root/ecell4/python; LIBRARY_PATH=/root/hdf5-1.8.14-linux-
centos5-x86_64-gcc482-shared/lib
CPATH=/root/boost_1_59_0:/root/hdf5-1.8.14-linux-
centos5-x86_64-gcc482-shared/include /opt/python/cp34-cp34m/bin/python
setup.py bdist_wheel  
  
# https://github.com/pypa/auditwheel/pull/31/files  
#RUN sed -ie 's/libname/soname/g'
/opt/_internal/cpython-3.5.1/lib/python3.5/site-packages/auditwheel/repair.py  
RUN cp /root/hdf5-1.8.14-linux-centos5-x86_64-gcc482-shared/lib/libhdf5.so.9
/lib64/; cp /root/hdf5-1.8.14-linux-
centos5-x86_64-gcc482-shared/lib/libhdf5_cpp.so.9 /lib64/; cp
/root/hdf5-1.8.14-linux-centos5-x86_64-gcc482-shared/lib/libsz.so.2 /lib64/  
RUN auditwheel repair
/root/ecell4/python/dist/ecell-4.0.2-cp35-cp35m-linux_x86_64.whl; auditwheel
repair /root/ecell4/python/dist/ecell-4.0.2-cp34-cp34m-linux_x86_64.whl;
auditwheel repair /root/ecell4/python/dist/ecell-4.0.2-cp27-cp27mu-
linux_x86_64.whl  


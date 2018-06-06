# Pull base image.  
FROM pyreefmodel/pyreef-dependencies-docker  
  
MAINTAINER Tristan Salles  
  
WORKDIR /build  
RUN pip install -e git+https://github.com/hplgit/odespy.git#egg=odespy  
WORKDIR /build/src/odespy  
RUN python setup.py install  
  
WORKDIR /build  
RUN pip install -U statsmodels  
  
# cd wavesed; f2py --f90exec=mpif90 -I. -c -m ocean ocean.f90  
WORKDIR /build  
RUN git clone https://github.com/pyReef-model/pyReefCore.git  
RUN pip install -e /build/pyReefCore  
  
RUN mkdir /usr/local/COVE  
RUN ls -la /usr/local/  
  
COPY COVE/ /usr/local/COVE/  
  
RUN ls -la /usr/local/  
  
RUN ls -la /usr/local/COVE  
  
RUN cd /usr/local/COVE/driver_files && \  
make -f spiral_bay_make.make && \  
mv spiral_bay.out cove && \  
mv cove /usr/local/bin  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
automake \  
autoconf \  
libtool \  
shtool \  
autogen \  
wget  
  
RUN pip install mako  
  
RUN cd /usr/local && \  
wget http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-4.1.3.tar.gz && \  
tar -xf netcdf-4.1.3.tar.gz && \  
cd netcdf-4.1.3 && \  
CPPFLAGS=-I/usr/local/include LDFLAGS=-L/usr/local/lib ./configure --enable-
separate-fortran --enable-netcdf-4 --enable-shared --enable-dap
--prefix=/usr/local && \  
make && \  
make install  
  
RUN ls -la /usr/local/include  
  
RUN mkdir /usr/local/xbeach  
  
COPY xbeach/ /usr/local/xbeach/  
  
RUN cd /usr/local/xbeach && \  
sh autogen.sh && \  
./configure --with-netcdf && \  
make && \  
sudo make install && \  
ldconfig  
  
ENV TINI_VERSION v0.8.4  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
RUN chmod +x /usr/local/bin/tini  
  
# Copy cluster configuration  
#RUN mkdir /root/.ipython  
#COPY profile_mpi /root/.ipython/profile_mpi  
RUN mkdir /usr/local/class  
COPY class/ /usr/local/class/  
  
RUN mkdir /usr/local/pracs  
COPY practicals/ /usr/local/pracs/  
  
RUN mkdir /workspace && \  
mkdir /workspace/volume  
  
RUN mv /usr/local/class /workspace  
RUN mv /usr/local/pracs /workspace  
  
RUN mv /workspace/class /workspace/classroom  
  
RUN cd /workspace/classroom/wavesed && \  
f2py --f90exec=mpif90 -I. -c -m ocean ocean.f90  
  
COPY run.sh /build  
RUN chmod +x /build/run.sh  
  
# setup space for working in  
VOLUME /workspace/volume  
  
RUN pip install git+https://github.com/jakevdp/JSAnimation.git  
  
# launch notebook  
WORKDIR /workspace  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
ENV
LD_LIBRARY_PATH=/workspace/volume/pyReefCore/pyReefCore/libUtils:/build/pyReefCore/pyReefCore/libUtils  
CMD /build/run.sh  


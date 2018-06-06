FROM ipython/scipystack  
MAINTAINER Petr Simecek <petrs@jax.org>  
  
# Install wget  
RUN apt-get update \  
&& apt-get install -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py  
  
# HDF5 installation  
RUN wget http://www.hdfgroup.org/ftp/HDF5/current/bin/linux-
centos6-x86_64-gcc447/hdf5-1.8.16-linux-centos6-x86_64-gcc447-shared.tar.gz  
RUN tar xvfz hdf5-1.8.16-linux-centos6-x86_64-gcc447-shared.tar.gz && \  
cp -R hdf5-1.8.16-linux-centos6-x86_64-gcc447-shared/* /usr/ && \  
rm -Rf hdf*  
  
# Install addition Python packages  
RUN pip install h5py  
RUN pip install flask  
RUN pip install flask-compress  
RUN pip install flask-cors  
  
# Clone the app from Github  
RUN git clone http://github.com/churchill-lab/qtl-viewer.git /root/app  
  
# The app starts when the container starts  
CMD ["python", "/root/app/run.py", "/data/settings.cfg"]  
  


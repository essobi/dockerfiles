# Install pieces of Matt's eQTL and pQTL viewers  
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
centos6-x86_64/hdf5-1.8.15-patch1-linux-centos6-x86_64-shared.tar.gz  
RUN tar xvfz hdf5-1.8.15-patch1-linux-centos6-x86_64-shared.tar.gz && \  
cp -R hdf5-1.8.15-patch1-linux-centos6-x86_64-shared/* /usr/ && \  
rm -Rf hdf*  
  
# Install addition Python packages  
RUN pip install h5py  
RUN pip install flask  
RUN pip install flask-compress  
RUN pip install flask-cors  
  
EXPOSE 8888  
EXPOSE 8889  
# copy the script to start eQTL/pQTL viewers  
RUN wget --directory-prefix=/usr/bin
https://raw.githubusercontent.com/churchill-
lab/sysgen2015/master/docker/webapp/start-app.sh \  
&& chmod 775 /usr/bin/start-app.sh  
  
# run the start script  
CMD ['/usr/bin/start-app.sh']  
  


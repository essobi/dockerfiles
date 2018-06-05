FROM debian:8.5  
MAINTAINER HDF-EOS Tools and Information Center <eoshelp@hdfgroup.org>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
RUN apt-get install -y curl grep sed dpkg emacs-nox vim-nox && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
ENV MPLBACKEND=agg  
# RUN conda install -y pyqt=4.11  
RUN conda install -y netcdf4  
RUN conda install -y hdf4  
RUN conda install -y basemap  
RUN apt-get install -y gcc python-dev python-numpy libhdf4-dev  
RUN pip install python-hdf4  
# RUN conda install -y -c conda-forge pyhdf  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]  


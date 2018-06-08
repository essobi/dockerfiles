# Installs Miniconda and uses the conda installer to add a bunch of additional  
# packages. Uses pip to install whatever remains.  
FROM magsol/lj-base  
MAINTAINER Shannon Quinn "magsol@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# A few prerequisites.  
RUN apt-get -y update && apt-get -y install libblas-dev liblapack-dev  
  
# Install Anaconda.  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > conda.sh && mv conda.sh
/etc/profile.d/  
RUN wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh  
RUN chmod +x Miniconda-latest-Linux-x86_64.sh && \  
/bin/bash Miniconda-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda-latest-Linux-x86_64.sh  
ENV PATH /opt/conda/bin:$PATH  
RUN conda update -y --all  
  
# Install some extra Python libraries.  
RUN /opt/conda/bin/conda install --yes astropy beautiful-soup blaze-core \  
bokeh bottleneck cython dask decorator freetype future gensim h5py hdf5 \  
ipython joblib libpng libsodium libtiff libxml2 llvmlite matplotlib nltk \  
numba numpy opencv pandas pep8 pillow pip protobuf pyamg scikit-image \  
scikit-learn scipy seaborn shapely sqlalchemy sqlite starcluster toolz \  
tornado twisted xray  
ADD requirements.txt /tmp/requirements.txt  
RUN /opt/conda/bin/pip install -r /tmp/requirements.txt && rm
/tmp/requirements.txt  


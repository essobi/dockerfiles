# Start with full anaconda (Python 3) distribution  
FROM continuumio/anaconda3:4.4.0  
MAINTAINER Michael van Vliet <m.s.vanvliet@lacdr.leidenuniv.nl>  
  
# make sure the font-manager is present  
RUN apt-get update --fix-missing && apt-get install -y --force-yes \  
libzmq3-dev python-setuptools python-dev build-essential \  
libcurl4-gnutls-dev libxml2-dev libssl-dev apt-utils gdebi-core psmisc \  
libapparmor1 libssh2-1 libssh2-1-dev curl nano libpng-dev  
  
# install conda packages  
RUN /opt/conda/bin/conda install jupyter lxml blaze numba h5py docopt
r-essentials -y --quiet  
  
COPY requirements.txt requirements.txt  
RUN /opt/conda/bin/pip install -r requirements.txt  
  
# add bash kernel to jupyter  
RUN python -m bash_kernel.install  
  
EXPOSE 8888:8888  
# prepare  
COPY jupyter.sh /usr/local/bin/jupyter.sh  
RUN chmod +x /usr/local/bin/jupyter.sh  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]


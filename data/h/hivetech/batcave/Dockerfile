# hivetech/pyscience  
# An ubuntu 12.04 LTS box with most common python packages for science
installed  
# VERSION 0.0.3  
# Administration  
FROM hivetech/batcave:base  
MAINTAINER Xavier Bruhiere, xavier.bruhiere@gmail.com  
  
# Requirements  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget r-base g++ make
libfreetype6-dev \  
libpng-dev libopenblas-dev liblapack-dev gfortran ipython  
RUN pip install --upgrade pep8 nose cython patsy  
  
RUN pip install -e git+https://github.com/numpy/numpy.git@master#egg=numpy  
RUN pip install -e git+https://github.com/pydata/pandas.git@master#egg=pandas  
RUN pip install -e git+https://github.com/scipy/scipy.git@master#egg=scipy  
RUN pip install -e git+https://github.com/scikit-learn/scikit-
learn.git@master#egg=sklearn  
  
# Cleaning  
RUN apt-get clean && rm -rf /tmp/* /var/tmp/*  
  
CMD ["ipython"]  
# ipython notebook port  
EXPOSE 8888  


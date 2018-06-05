FROM centos:7  
  
MAINTAINER Panagiotis Korfiatis <korfiatisp@gmail.com>  
  
#################################################################################################################  
# This builds a compute environment for developing medical image analysis
applications #  
#################################################################################################################  
  
  
#################################################################################################################  
# basic development tools #  
#################################################################################################################  
RUN yum -y install git python-devel  
RUN yum -y install python-setuptools  
RUN yum -y install gcc-gfortran libmpc-devel  
RUN yum -y install wget  
RUN yum -y install gcc  
RUN yum -y install gcc-c++  
RUN yum -y install Cython  
RUN yum -y install epel-release  
RUN yum -y install cmake  
RUN yum -y install make  
# RUN yum install -y zlib-dev openssl-devel sqlite-devel  
# RUN yum install -y glibmm24-devel gtkmm24-devel gsl-devel  
# nifticlib dependencies  
RUN yum install -y csh  
# python dependencies for https, bzip2  
RUN yum install -y bzip2-devel  
# MITK dependencies  
RUN yum install -y libtiff-devel tcp_wrappers-devel  
RUN yum install -y telnet  
RUN yum -y install python-pip  
RUN pip install --upgrade pip  
RUN pip install mako  
RUN yum -y install epel-release  
RUN yum -y install nodejs  
RUN yum -y install npm  
  
#RUN npm install -g codebox  
#EXPOSE 8000  
  
RUN mkdir ~/src && cd ~/src && \  
git clone https://github.com/xianyi/OpenBLAS && \  
cd ~/src/OpenBLAS && \  
make FC=gfortran && \  
make PREFIX=/opt/OpenBLAS install  
# now update the library system:  
RUN echo /opt/OpenBLAS/lib > /etc/ld.so.conf.d/openblas.conf  
RUN ldconfig  
ENV LD_LIBRARY_PATH=/opt/OpenBLAS/lib:$LD_LIBRARY_PATH  
RUN yum -y install freetype freetype-devel libpng-devel  
RUN pip install pandas  
RUN pip install matplotlib  
# now install numpy source  
RUN pwd  
RUN ls  
RUN cd ~/src && \  
git clone -b maintenance/1.9.x https://github.com/numpy/numpy && \  
cd numpy && \  
touch site.cfg  
RUN echo [default] > ~/src/numpy/site.cfg && \  
echo include_dirs = /opt/OpenBLAS/include >> ~/src/numpy/site.cfg && \  
echo library_dirs = /opt/OpenBLAS/lib >> ~/src/numpy/site.cfg && \  
echo [openblas] >> ~/src/numpy/site.cfg && \  
echo openblas_libs = openblas >> ~/src/numpy/site.cfg && \  
echo library_dirs = /opt/OpenBLAS/lib >> ~/src/numpy/site.cfg && \  
echo [lapack] >> ~/src/numpy/site.cfg && \  
echo lapack_libs = openblas >> ~/src/numpy/site.cfg && \  
echo library_dirs = /opt/OpenBLAS/lib >> ~/src/numpy/site.cfg  
RUN cd ~/src/numpy && \  
python setup.py config && \  
python setup.py build --fcompiler=gnu95 && \  
python setup.py install  
RUN pip install ipython  
RUN pip install cython --upgrade  
RUN pip install scipy  
# RUN cd ~/src && \  
# git clone https://github.com/scipy/scipy.git  
# RUN cd ~/src/scipy && \  
# python setup.py config && \  
# python setup.py build --fcompiler=gnu95 && \  
# python setup.py install  
RUN pip install scikit-learn  
RUN pip install scikit-image  
RUN pip install --trusted-host www.simpleitk.org -f
http://www.simpleitk.org/SimpleITK/resources/software.html SimpleITK  
RUN pip install argparse  
RUN pip install pydicom  
RUN pip install networkx  
RUN pip install tornado  
RUN pip install nibabel  
# RUN pip install nipype  
RUN pip install wget  
RUN pip install Flask  
RUN pip install Flask-Admin  
RUN pip install Flask-Assets  
RUN pip install markdown  
RUN pip install Flask-Login  
RUN pip install Flask-WTF  
ENV OPENBLAS_NUM_THREADS=4  
RUN pip install chainer  
RUN pip install theano  
RUN pip install keras  
RUN pip install jupyterlab  
RUN jupyter serverextension enable --py jupyterlab  
#####################  
############################################################################################  
#RUN cd ~/src && \  
#git clone https://github.com/stnava/ANTs.git  
#RUN cd ~/src && mkdir antsbin  
#RUN cd ~/src/antsbin && \  
#cmake ../ANTs -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=OFF
-DBUILD_TESTING=OFF && \  
# make -j4  
#ENV PATH=~/src/antsbin/bin  
# ENTRYPOINT ["jupyter"]  
RUN cd ~/src  
EXPOSE 8888  
# CMD ["jupyter", "lab"]  
RUN mkdir workdirectory  
ADD notebook.sh /  
  
CMD ["/notebook.sh"]


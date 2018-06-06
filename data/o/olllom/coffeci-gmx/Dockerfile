FROM ubuntu:16.04  
#RUN sudo apt-get install -y libssl-dev openssl bzip2  
RUN apt-get update  
RUN apt-get install -y cmake build-essential wget python3 python-dev
python3-pip python-pip  
RUN apt-get install -y openbabel pymol  
  
RUN wget ftp://ftp.gromacs.org/pub/gromacs/gromacs-2016.5.tar.gz  
RUN tar xfz gromacs-2016.5.tar.gz  
WORKDIR $HOME/gromacs-2016.5  
RUN mkdir build  
WORKDIR $HOME/gromacs-2016.5/build  
RUN cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON
-DGMX_USE_RDTSCP=OFF  
RUN make  
RUN make check  
RUN make install  
RUN echo "source /usr/local/gromacs/bin/GMXRC" > $HOME/.bashrc  
  
RUN sed -i "s,python2.7,/usr/bin/python2.7,g" /usr/bin/pymol


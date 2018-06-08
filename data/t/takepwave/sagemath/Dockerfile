# Sage Installation from Ubuntu PPA  
#  
# VERSION 0.2  
FROM takepwave/primesage:latest  
MAINTAINER Hiroshi TAKEMOTO <take.pwave@gmail.com>  
USER root  
  
RUN apt-get update  
RUN apt-get install -y libmagickwand-dev  
RUN apt-get install -y jags  
RUN apt-get install -y gdal-bin  
  
# for nloptr_1.0.4.tar.gz error  
RUN apt-get install -y libnlopt-dev  
  
COPY installRpackages.R /opt/installRpackages.R  
  
RUN apt-get install -y wget  
RUN wget
https://cran.r-project.org/src/contrib/Archive/rjags/rjags_3-15.tar.gz  
RUN sage -R --save </opt/installRpackages.R  
  
RUN sage -pip install pandas  
RUN sage -pip install ggplot  
RUN sage -pip install Wand  
RUN sage -pip install seaborn  
RUN sage -pip install pyjags  
RUN sage -pip install sklearn  
RUN sage -pip install xlsxWriter xlrd xlwt  
RUN sage -pip install python-nvd3  
  
RUN apt-get install -y mecab libmecab-dev mecab-ipadic-utf8  
RUN sage -pip install mecab-python  
  
RUN apt-get install -y build-essential cmake unzip  
RUN apt-get install -y libopenblas-dev liblapack-dev  
RUN apt-get install -y libhdf5-serial-dev  
RUN apt-get install -y graphviz  
RUN sage -pip install pydot-ng  
RUN sage -pip install tensorflow  
RUN sage -pip install keras  
RUN sage -pip install h5py  
RUN sage -pip install daft  
  
RUN apt-get install -y openscad  
RUN sage -pip install numpy-stl solidpython  
RUN apt-get install -y git  
  
USER sage  
CMD ["/opt/sage_launcher"]  


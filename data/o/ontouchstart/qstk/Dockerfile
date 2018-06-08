FROM ubuntu:14.04  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
RUN apt-get -y install git vim emacs24-nox wget curl  
RUN git clone https://github.com/ontouchstart/QuantSoftwareToolkit.git  
RUN cd QuantSoftwareToolkit && sh UbuntuInstallation.sh && python setup.py
install  
RUN python QuantSoftwareToolkit/Examples/Validation.py  
  
ADD matplotlibrc /.config/matplotlib/matplotlibrc  


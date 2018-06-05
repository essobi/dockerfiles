FROM python:3.5  
  
# Update  
RUN apt-get update  
  
# Some dependencies for the packages,  
# Matplotlib needs pkg-config and build-essential  
# Scipy needs gfortran and libatlas  
# Also want pip for later package installs  
RUN apt-get install -y pkg-config build-essential gfortran libfreetype6-dev
libatlas-base-dev python3-pip python3-tk qtcreator pyqt5-dev-tools  
  
# Install pandas numpy scipy  
RUN pip3 install numpy pandas scipy matplotlib pyqtgraph Pillow PyQt5


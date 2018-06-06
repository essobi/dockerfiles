FROM dammi87/pylime:3.5_3.0  
# Update  
RUN apt-get update  
  
# Some dependencies for the packages,  
# Matplotlib needs pkg-config and build-essential  
# Scipy needs gfortran and libatlas  
# Also want pip for later package installs  
RUN apt-get install -y pkg-config build-essential gfortran libfreetype6-dev
libatlas-base-dev python3-pip python3-tk qtcreator pyqt5-dev-tools  
  
# Install pandas numpy scipy  
RUN pip3 install numpy pandas scipy matplotlib pyqtgraph  
  
# Run sublime  
CMD subl  


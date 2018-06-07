FROM hemelb/setuptool-base  
MAINTAINER Miguel O. Bernabeu (miguel.bernabeu@ed.ac.uk)  
  
##  
# Download and install HemeLB  
##  
WORKDIR /tmp  
RUN git clone https://github.com/UCL/hemelb.git  
  
##  
# Configure the setup tool  
##  
# Build the required python components  
WORKDIR /tmp  
RUN cd hemelb/Tools && \  
python setup.py build_ext --inplace && \  
cd setuptool && \  
python setup.py build_ext --inplace  
  
# Install the setup tool scripts and set environment variables  
ENV PYTHONPATH="/tmp/hemelb/Tools:/tmp/hemelb/Tools/setuptool:$PYTHONPATH"  
RUN cp /tmp/hemelb/Tools/setuptool/scripts/* /usr/local/bin  
  
# Create a mount point for data  
VOLUME /data  


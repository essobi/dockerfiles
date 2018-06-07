#  
# Dronecourse PX4/gazebo environment  
#  
FROM px4io/px4-dev-simulation:2017-12-08  
MAINTAINER Julien Lecoeur <julien.lecoeur@gmail.com>  
  
# setup environment  
EXPOSE 8888  
# Install platform tool  
RUN git clone \--recurse-submodules https://github.com/dronecourse-
epfl/platform \  
&& cd platform \  
&& rm platform \  
&& ./build.sh \  
&& ln -s $(realpath platform) /usr/local/bin  
  
# Install git and ssh  
RUN apt-get update && apt-get install -q -y git openssh-client  
  
# Install Xfvb for running camera sensor on CI  
RUN apt-get update && apt-get install -q -y xvfb  
  
# Install python dependencies (for evaluation scripts)  
RUN apt-get update && apt-get install -q -y python-tk  
RUN pip install --upgrade px4tools jupyter numpy matplotlib openpyxl
xlsxwriter pandas  
  
# Install Doxygen for generating the documentation  
RUN apt-get update && apt-get install -q -y doxygen


# Jupyter + IJulia  
FROM skippa/anaconda  
MAINTAINER mike.aizatsky@gmail.com  
  
RUN echo "deb http://ppa.launchpad.net/staticfloat/julia-deps/ubuntu xenial
main" > /etc/apt/sources.list.d/staticfloat-ubuntu-julia-deps-xenial.list  
RUN echo "deb http://ppa.launchpad.net/staticfloat/juliareleases/ubuntu xenial
main" > /etc/apt/sources.list.d/staticfloat-ubuntu-juliareleases-xenial.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CF979FFA3D3D3ACC  
RUN apt-get update && apt-get install julia build-essential libzmq3-dev
hdf5-tools make gettext -y  
  
ADD install.jl /root/  
RUN julia /root/install.jl  


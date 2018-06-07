# The default image for spawning notebooks  
# Has Python, Octave, and Julia  
  
FROM ritjupyter/minimal-systemuser  
MAINTAINER Joshua Milas <jgm6496@rit.edu>  
  
USER root  
  
# Add matplotLib  
RUN conda install --quiet --yes \  
'matplotlib' && \  
conda clean -tipsy  
  
  
  
# Install and setup octave  
# Install Octave, all of its packages, and gnuplot  
# less is needed by gnuplot  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
octave \  
octave-* \  
gnuplot \  
less \  
ghostscript \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install the octave kernel  
# It needs the ipywidgets apparently  
RUN pip --no-cache-dir install octave_kernel && \  
python -m octave_kernel.install  
  
  
  
## Install and setup Julia  
## This takes forever  
## TODO move this to its own image  
#RUN apt-get update && apt-get install -yq --no-install-recommends \  
# julia \  
# libnettle6 \  
# && apt-get clean && \  
# rm -rf /var/lib/apt/lists/*  
#  
## We need this to install julia packages system wide  
#RUN mkdir /opt/julia-global-packages && \  
# echo 'push!(LOAD_PATH, "/opt/julia-global-packages")' >>
/etc/julia/juliarc.jl  
#ENV JULIA_PKGDIR /opt/julia-global-packages  
#  
## Install IJulia, the Julia Jupyter kernel  
#RUN julia -e 'Pkg.init()'  
#RUN julia -e 'Pkg.add("IJulia")' && \  
# julia -e 'Pkg.build("IJulia")'  
## precompile packages  
#RUN julia -e 'using BinDeps' && \  
# julia -e 'using Compat' && \  
# julia -e 'using Conda' && \  
# julia -e 'using IJulia' && \  
# julia -e 'using JSON' && \  
# julia -e 'using Nettle' && \  
# julia -e 'using SHA' && \  
# julia -e 'using URIParser' && \  
# julia -e 'using ZMQ' && \  
# julia -e 'Pkg.update()'  
## make sure anyone can use the packages  
## and install the IJulia kernel to the system level  
#RUN chmod -R 777 /opt/julia-global-packages && \  
# jupyter kernelspec install /home/jovyan/.local/share/jupyter/kernels/* && \  
# rm -rf /home/jovyan/  
  
  
  
# Install IArm  
RUN pip install iarm && \  
python -m iarm_kernel.install  
  
  
  
# Install the C kernel  
RUN apt-get update && apt-get install gcc && \  
pip install jupyter-c-kernel && \  
cd /tmp && \  
git clone https://github.com/brendan-rius/jupyter-c-kernel.git && \  
cd jupyter-c-kernel && \  
jupyter kernelspec install c_spec && \  
rm -rf /tmp/*  
  
  
  
## Install C++ kernel  
## TODO they changed how to install cling, update to reflect that; removing it
from the build for now  
#RUN cd /tmp && \  
# wget https://root.cern.ch/download/cling/cling_2016-09-26_ubuntu16.tar.bz2
&& \  
# tar -xvjf cling_2016-09-26_ubuntu16.tar.bz2 && \  
# mv cling_2016-09-26_ubuntu16 /opt/cling && \  
# cd /opt/cling/share/cling/Jupyter/kernel/ && \  
# pip install -e . && \  
# jupyter kernelspec install cling && \  
# rm -rf /tmp/*  
#ENV PATH /opt/cling/bin:$PATH  


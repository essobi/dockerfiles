FROM jupyter/datascience-notebook  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
xz-utils \  
lsb && apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
RUN ln -s /bin/tar /bin/gtar  
  
USER $NB_USER  
  
RUN conda create -y -n py27 python=2.7 anaconda  
RUN /bin/bash -c "source activate py27 && \  
conda install -y jupyter && \  
python -m ipykernel install --user --name py27 --display-name "Python 2.7" "  
  
RUN julia -e 'Pkg.init()' && \  
julia -e 'Pkg.update()' && \  
julia -e 'Pkg.add("HDF5")' && \  
julia -e 'Pkg.add("GR")' && \  
julia -e 'Pkg.add("Plots")' && \  
julia -e 'Pkg.add("Interact")' && \  
julia -e 'Pkg.add("RDatasets")' && \  
julia -e 'Pkg.add("DSP")' && \  
julia -e 'Pkg.add("BenchmarkTools")' && \  
julia -e 'Pkg.clone("https://github.com/antholzer/CompressedSensing.jl.git")'
&& \  
julia -e 'Pkg.add("IJulia")' && \  
# Precompile Julia packages \  
julia -e 'using HDF5' && \  
julia -e 'using GR' && \  
julia -e 'using Plots' && \  
julia -e 'using Interact' && \  
julia -e 'using RDatasets' && \  
julia -e 'using DSP' && \  
julia -e 'using BenchmarkTools' && \  
julia -e 'using CompressedSensing' && \  
julia -e 'using IJulia'  


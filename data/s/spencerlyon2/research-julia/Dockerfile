FROM julia:0.4.5  
MAINTAINER Spencer Lyon <spencerlyon2@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install \  
vim wget curl build-essential screen cmake hdf5-tools && \  
rm -rf /tmp/downloaded_packages/ /tmp/*.rds /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
RUN echo "cacert=/etc/ssl/certs/ca-certificates.crt" > ~/.curlrc  
  
# Julia package installation  
RUN julia -e 'Pkg.init();' && \  
julia -e 'map(Pkg.add, ["Plots", "PlotlyJS", "IterationManagers",
"QuantEcon"])' && \  
julia -e 'map(Pkg.add, ["Distributions", "NLsolve",
"Interact","Interpolations"])' && \  
julia -e 'Pkg.clone("https://github.com/spencerlyon2/ModelerToolbox.jl.git")'
&& \  
julia -e 'Pkg.clone("https://github.com/spencerlyon2/CompEcon.jl.git")'  
  
# these packages are harder to install... put them later just in case  
RUN julia -e 'Pkg.add("JLD"); Pkg.add("HDF5")'  
RUN julia -e 'Pkg.add("IJulia")'  
  
# check out some of my packages...  
RUN julia -e 'Pkg.checkout("PlotlyJS"); Pkg.checkout("IterationManagers");'  
  
# call using on some to precompile things  
RUN julia -e 'using PlotlyJS, QuantEcon, Interpolations, CompEcon, JLD'  


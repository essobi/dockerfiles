FROM spencerlyon2/jupyter-conda  
  
MAINTAINER Spencer Lyon <spencerlyon2@gmail.com>  
  
# Julia Installation  
RUN apt-get install software-properties-common python-software-properties -y
&& \  
add-apt-repository ppa:staticfloat/julianightlies && \  
add-apt-repository ppa:staticfloat/julia-deps && \  
apt-get update && \  
apt-get install -y julia libnettle4 && \  
rm -rf /tmp/downloaded_packages/ /tmp/*.rds /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
# Have root install julia packages globally. I found this directory by  
# looking at `LOAD_PATH` from within a julia session  
ENV JULIA_PKGDIR /usr/local/share/julia/site  
  
# Julia package Installation (should be global)  
RUN julia -e 'Pkg.init(); Pkg.add("IJulia")' && \  
julia -e 'Pkg.add("Gadfly"); Pkg.add("RDatasets"); Pkg.add("ForwardDiff")' &&
\  
julia -e 'Pkg.add("Distributions"); Pkg.add("NLsolve"); Pkg.add("Interact")'
&& \  
julia -e 'Pkg.add("PyCall"); Pkg.add("PyPlot"); Pkg.add("Pandas")'  
# check out ZMQ and IJulia to get them working  
RUN julia -e 'Pkg.checkout("ZMQ"); Pkg.checkout("IJulia");'  


From cablab/singleuser-python:v4  
MAINTAINER Brockmann Consult GmbH <http://www.brockmann-consult.de>  
  
# Install Julia  
USER root  
WORKDIR /srv/jupyterhub  
RUN apt-get update  
RUN apt-get -y install apt-utils  
RUN apt-get -y install r-base r-recommended libcurl4-gnutls-dev libssl-dev
libnetcdf-dev libudunits2-dev udunits-bin libhdf5-dev libzmq3-dev cmake  
RUN wget
https://julialang.s3.amazonaws.com/bin/linux/x64/0.5/julia-0.5.0-linux-x86_64.tar.gz  
RUN mkdir julia && tar xzf julia-0.5.0-linux-x86_64.tar.gz -C julia --strip-
components 1  
RUN PATH="/srv/jupyterhub/julia/bin:$PATH"  
WORKDIR /srv/jupyterhub/julia  
RUN echo 'Pkg.add("IJulia")' > IJulia.jl  
RUN echo 'Pkg.clone("https://github.com/CAB-
LAB/CABLAB.jl");Pkg.add("Patchwork");Pkg.checkout("Patchwork");Pkg.clone("https://github.com/CAB-
LAB/CABLABPlots.jl")' > installcablab.jl  
RUN echo
'Pkg.clone("https://github.com/milanflach/LIBSVM.jl");Pkg.checkout("LIBSVM","mutating_versions")'
> installlibsvm.jl  
RUN echo 'Pkg.clone("https://github.com/milanflach/MultivariateAnomalies.jl")'
> installmultivariate.jl  
RUN echo 'using Compose; using CABLAB; using CABLABPlots' > precomp.jl  
USER jovyan  
RUN export CABLAB_WORKDIR="/home/jovyan/work/tmp"  
RUN /srv/jupyterhub/julia/bin/julia IJulia.jl  
RUN /srv/jupyterhub/julia/bin/julia installlibsvm.jl  
RUN /srv/jupyterhub/julia/bin/julia installmultivariate.jl  
RUN /srv/jupyterhub/julia/bin/julia installcablab.jl  
RUN /srv/jupyterhub/julia/bin/julia precomp.jl  
  
USER jovyan  
WORKDIR /home/jovyan/work  


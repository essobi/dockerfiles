From jupyterhub/singleuser  
MAINTAINER Brockmann Consult GmbH <http://www.brockmann-consult.de>  
# Install python modules  
RUN conda install --quiet --yes 'xarray' 'dask'  
RUN conda install -c forman gridtools  
RUN conda install -c anaconda --yes basemap=1.0.7  
RUN conda install -c conda-forge ffmpeg=2.8.6  
USER root  
# Install cablab  
WORKDIR /srv/jupyterhub  
RUN git clone https://github.com/CAB-LAB/cablab-core.git  
WORKDIR /srv/jupyterhub/cablab-core  
RUN python setup.py install  
# Install R and R CABLAB  
USER root  
WORKDIR /srv/jupyterhub  
RUN echo "deb http://ftp5.gwdg.de/pub/misc/cran/bin/linux/debian jessie-
cran3/" >> /etc/apt/sources.list  
RUN apt-key adv --keyserver keys.gnupg.net --recv-key
6212B7B7931C4BB16280BA1306F90DE5381BA480  
RUN apt-get update  
RUN apt-get -y install apt-utils  
RUN apt-get -y install r-base r-recommended libcurl4-gnutls-dev libssl-dev
libnetcdf-dev libudunits2-dev udunits-bin libhdf5-dev libzmq3-dev cmake  
# Install Julia  
WORKDIR /srv/jupyterhub  
RUN wget
https://julialang.s3.amazonaws.com/bin/linux/x64/0.5/julia-0.5.0-linux-x86_64.tar.gz  
RUN mkdir julia && tar xzf julia-0.5.0-linux-x86_64.tar.gz -C julia --strip-
components 1  
RUN PATH="/srv/jupyterhub/julia/bin:$PATH"  
WORKDIR /srv/jupyterhub/julia  
RUN echo 'Pkg.add("IJulia")' > IJulia.jl  
RUN echo 'Pkg.clone("https://github.com/CAB-
LAB/CABLAB.jl");Pkg.checkout("Patchwork")' > installcablab.jl  
RUN echo
'Pkg.clone("https://github.com/milanflach/LIBSVM.jl");Pkg.checkout("LIBSVM","mutating_versions")'
> installlibsvm.jl  
RUN echo 'Pkg.clone("https://github.com/milanflach/MultivariateAnomalies.jl")'
> installmultivariate.jl  
RUN echo 'using CABLAB' > precomp.jl  
USER jovyan  
RUN export CABLAB_WORKDIR="/home/jovyan/work/tmp"  
RUN /srv/jupyterhub/julia/bin/julia IJulia.jl  
RUN /srv/jupyterhub/julia/bin/julia installlibsvm.jl  
RUN /srv/jupyterhub/julia/bin/julia installmultivariate.jl  
RUN /srv/jupyterhub/julia/bin/julia installcablab.jl  
RUN /srv/jupyterhub/julia/bin/julia precomp.jl  
  
USER root  
WORKDIR /srv/jupyterhub  
RUN git clone https://github.com/CAB-LAB/RCABLAB  
RUN wget
https://cran.r-project.org/src/contrib/Archive/RNetCDF/RNetCDF_1.6.1-2.tar.gz  
RUN R CMD INSTALL RNetCDF_1.6.1-2.tar.gz  
WORKDIR /srv/jupyterhub/RCABLAB  
RUN git checkout 02998cd41ee0c3862cf698b6729471576366dd67  
RUN R CMD INSTALL RCABLAB  
WORKDIR /srv/jupyterhub  
RUN apt-get -y install libcurl4-openssl-dev libssl-dev  
RUN R -e "install.packages(c('repr', 'IRdisplay', 'crayon', 'pbdZMQ',
'devtools'),repos='http://cran.us.r-project.org');devtools::install_github('IRkernel/IRkernel');IRkernel::installspec()"  
RUN R -e
"install.packages(c('data.table'),repos='http://cran.us.r-project.org')"  
RUN R -e
"install.packages(c('ggplot2','raster','sp','zoo','rgdal','dplyr','vegan','ape','Rtsne','Rcpp','inline'),repos='http://cran.us.r-project.org')"  
  
USER jovyan  
WORKDIR /home/jovyan/work  


# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM jupyter/scipy-notebook  
  
MAINTAINER tfitz <fitzgeraldt@gonzaga.edu>  
  
USER root  
  
# pre-requisites  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
fonts-dejavu \  
gfortran \  
gcc \  
ca-certificates \  
git \  
build-essential \  
hdf5-tools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
  
# Install Julia  
ENV JULIA_PATH /opt/julia  
ENV JULIA_VERSION 0.5.0  
  
RUN mkdir $JULIA_PATH \  
&& apt-get update \  
&& apt-get install -y curl \  
&& curl -sSL
"https://julialang.s3.amazonaws.com/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz"
-o julia.tar.gz \  
&& curl -sSL
"https://julialang.s3.amazonaws.com/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz.asc"
-o julia.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
# http://julialang.org/juliareleases.asc  
# Julia (Binary signing key) <buildbot@julialang.org>  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
3673DF529D9049477F76B37566E3C7DC03D6E495 \  
&& gpg --batch --verify julia.tar.gz.asc julia.tar.gz \  
&& rm -r "$GNUPGHOME" julia.tar.gz.asc \  
&& tar -xzf julia.tar.gz -C $JULIA_PATH --strip-components 1 \  
&& rm -rf /var/lib/apt/lists/* julia.tar.gz*  
  
  
ENV PATH $JULIA_PATH/bin:$PATH  
  
USER $NB_USER  
  
  
# Install IJulia packages as jovyan and then move the kernelspec out  
# to the system share location. Avoids problems with runtime UID change not  
# taking effect properly on the .local folder in the jovyan home dir.  
RUN julia -e 'Pkg.add("IJulia")' && \  
mv /home/$NB_USER/.local/share/jupyter/kernels/julia*
$CONDA_DIR/share/jupyter/kernels/ && \  
chmod -R go+rx $CONDA_DIR/share/jupyter  
  
# Show Julia where conda libraries are  
# Add essential packages  
#RUN echo "push!(Sys.DL_LOAD_PATH, \"$CONDA_DIR/lib\")" >
/home/$NB_USER/.juliarc.jl && \  
# julia -e 'Pkg.add("Gadfly")' && \  
# julia -F -e 'Pkg.add("HDF5")'  
RUN julia -e 'Pkg.update()' \  
&& julia -e 'Pkg.add("SymPy")' \  
&& julia -e 'Pkg.add("PyPlot")' \  
&& julia -e 'Pkg.add("MAT")' \  
&& julia -e 'Pkg.add("ODE")' \  
&& julia -e 'Pkg.add("HDF5")' \  
&& julia -e 'Pkg.add("Roots")' \  
&& julia -e 'Pkg.add("Polynomials")' \  
&& julia -e 'Pkg.add("ControlSystems")' \  


#  
# Docker image for course 2070fbdbmw - Computational Neuroscience  
#  
# October 8th 2016 - Antwerpen  
# Michele Giugliano plays with Julia and Jupyter Notebook  
#  
# Note: Julia version 0.5.0 is installed explicitly  
# A .jl configuration script is then invoked: it downloads its own miniconda
python 2.7 dist  
#  
# Distributed under the terms of the Modified BSD License.  
#  
# Compiled invoking: docker build -t docker-2070fbdbmw .  
#  
FROM debian:jessie  
  
RUN apt-get update -y \  
&& apt-get -y upgrade \  
&& apt-get install -y --no-install-recommends ca-certificates git build-
essential \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV JULIA_PATH /usr/local/julia  
ENV JULIA_VERSION 0.5.0  
RUN mkdir $JULIA_PATH \  
&& apt-get update && apt-get install -y curl \  
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
  
COPY julia_init.jl /tmp/  
COPY julia_start.jl /tmp/  
RUN julia /tmp/julia_init.jl  
  
#CMD ["/usr/local/julia /tmp/julia_start.jl"]  
EXPOSE 8888  
VOLUME /tmp  
WORKDIR /tmp  
  
CMD ["/bin/sh", "-c", "/root/.julia/v0.5/Conda/deps/usr/bin/jupyter-notebook
--no-browser --ip=0.0.0.0 --notebook-dir=/tmp"]  


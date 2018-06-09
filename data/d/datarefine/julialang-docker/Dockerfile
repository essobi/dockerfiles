# Phusion/BaseImage (ubuntu 16.04) Docker file for Julia  
# Version:v0.6.0 and v0.4.7  
  
FROM phusion/baseimage:latest  
  
MAINTAINER Yusuke Saito  
  
RUN apt-get update \  
&& apt-get upgrade -y -o Dpkg::Options::="--force-confdef" -o
DPkg::Options::="--force-confold" \  
&& apt-get install -y \  
libc6 \  
libc6-dev \  
build-essential \  
wget \  
curl \  
file \  
vim \  
unzip \  
pkg-config \  
cmake \  
gfortran \  
gettext \  
git \  
imagemagick \  
libreadline-dev \  
libncurses-dev \  
libpcre3-dev \  
libgnutls30 \  
libzmq3-dev \  
libzmq5 \  
libcairo2 \  
libcairo2-dev \  
libpango1.0-0 \  
libpango1.0-dev \  
llvm-4.0 \  
llvm-4.0-dev \  
clang-4.0 \  
libclang-4.0-dev \  
&& apt-get clean \  
&& update-alternatives --install /usr/bin/clang clang /usr/bin/clang-4.0 10 \  
&& update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-4.0
10  
  
  
# Install miniconda3  
RUN mkdir /opt/miniconda3 && cd /opt/miniconda3 && curl -L
https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o
/opt/miniconda3/miniconda3.sh\  
&& echo "export CONDA_JL_HOME=\"/opt/miniconda3/envs/conda_jl\"" >>
/etc/enviroment\  
&& echo "export CONDA_JL_VERSION=\"3\"" >> /etc/enviroment\  
&& bash /opt/miniconda3/miniconda3.sh -b -u -p /opt/miniconda3\  
&& /opt/miniconda3/bin/conda update \--all -y  
  
RUN /opt/miniconda3/bin/pip install --upgrade pip\  
&& /opt/miniconda3/bin/pip install pyzmq PyDrive google-api-python-client
jsonpointer jsonschema tornado sphinx pygments nose readline mistune invoke
matplotlib jupyter  
  
# Install cmdStan  
RUN mkdir -p /opt/cmdstan && curl -L https://github.com/stan-
dev/cmdstan/releases/download/v2.17.0/cmdstan-2.17.0.tar.gz | tar -z -x -C
/opt/cmdstan --strip-components=1 -f -\  
&& sed -e "13s/^/#/" -i.bak /opt/cmdstan/stan/lib/stan_math/make/detect_cc \  
&& cd /opt/cmdstan && make build \  
&& echo "export CMDSTAN_HOME=\"/opt/cmdstan\"" >> /etc/environment  
  
# Install julia 0.4.7  
RUN mkdir -p /opt/julia-0.4.7 && \  
curl -L
https://julialang.s3.amazonaws.com/bin/linux/x64/0.4/julia-0.4.7-linux-x86_64.tar.gz
| tar -z -x -C /opt/julia-0.4.7 \--strip-components=1 -f -  
RUN ln -fs /opt/julia-0.4.7 /opt/julia-0.4  
  
# Install julia 0.6.1  
RUN mkdir -p /opt/julia-0.6.1 && \  
curl -L
https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.1-linux-x86_64.tar.gz
| tar -z -x -C /opt/julia-0.6.1 \--strip-components=1 -f -  
RUN ln -fs /opt/julia-0.6.1 /opt/julia-0.6  
  
# Make v0.6 default julia  
RUN ln -fs /opt/julia-0.6.1 /opt/julia  
  
RUN echo
"PATH=\"/opt/julia/bin:/opt/miniconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games\""
>> /etc/environment && \  
echo "export PATH" >> /etc/environment && \  
echo "source /etc/environment" >> /root/.bashrc  
  
# Make jupyter-notebook config and change default network  
RUN /opt/miniconda3/bin/jupyter notebook --generate-config && sed -e
"162s/^#//" -e "162s/localhost/0.0.0.0/" -i.bak
/root/.jupyter/jupyter_notebook_config.py  
  
# Julia v0.4.0 packages add  
RUN /opt/julia-0.4.7/bin/julia -e 'Pkg.update()'\  
&& /opt/julia-0.4.7/bin/julia -e 'ENV["PYTHON"]="/opt/miniconda3/bin/python3";
Pkg.add("Conda")'\  
&& /opt/julia-0.4.7/bin/julia -e
'ENV["JUPYTER"]="/opt/miniconda3/bin/jupyter"; Pkg.add("IJulia")'  
  
# Julia v0.6.0 packages add  
RUN /opt/julia/bin/julia -e 'Pkg.update()'\  
&& /opt/julia/bin/julia -e 'ENV["JUPYTER"]="/opt/miniconda3/bin/jupyter";
Pkg.add("IJulia")'\  
&& /opt/julia/bin/julia -e 'ENV["PYTHON"]="/opt/miniconda3/bin/python3";
Pkg.add("Conda")'\  
&& /opt/julia/bin/julia -e 'ENV["PYTHON"]="/opt/miniconda3/bin/python3";
Pkg.add("PyPlot") '\  
&& /opt/julia/bin/julia -e 'Pkg.add("Plots")'\  
&& /opt/julia/bin/julia -e 'Pkg.add("RDatasets")'\  
&& /opt/julia/bin/julia -e 'Pkg.add("DifferentialEquations")'\  
&& /opt/julia/bin/julia -e 'Pkg.add("ODE")'\  
&& /opt/julia/bin/julia -e 'Pkg.add("Mamba")'\  
&& /opt/julia/bin/julia -e 'Pkg.add("Stan")'  
  
EXPOSE 8888  
CMD /opt/miniconda3/bin/jupyter notebook --allow-root  


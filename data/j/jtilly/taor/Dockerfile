## start with the latest Ubuntu image  
FROM ubuntu:latest  
  
## Maintainer  
MAINTAINER "Jan Tilly" jantilly@gmail.com  
  
## Set working directory  
WORKDIR /root  
  
## Remain current  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y  
  
## Add compilers, make, and valgrind  
RUN apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
gfortran \  
make \  
valgrind  
  
## Add lapack / blas  
RUN apt-get install -y --no-install-recommends \  
libblas3gf \  
libblas-dev \  
liblapack3gf \  
liblapack-dev  
  
## Install R  
RUN apt-get install -y --no-install-recommends apt-transport-https \  
&& echo "deb https://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 \  
&& apt-get update -qq \  
&& apt-get install -y --no-install-recommends r-base-dev  
  
## Clone taoR and install it  
RUN Rscript -e "source(\"http://jtilly.io/taoR/install_taoR.R\");
install_taoR(download_binaries = TRUE)"  
  
## Clean-up  
RUN rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*  


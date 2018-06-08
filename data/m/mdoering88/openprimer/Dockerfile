FROM rocker/shiny:latest  
MAINTAINER Matthias Doering <mdoering@mpi-inf.mpg.de>  
# R library dependencies considered in this dockerfile:  
#shinyjs, cshapes, countrycode, Biostrings, XML,, scales, gplots, reshape2,
seqinr, IRanges, ggplot2, plyr, stringdist, stringr, doParallel, gtools,
RColorBrewer, sets, DECIPHER, digest, shiny, DT, shinyBS, lpSolve,lpSolveAPI  
# Python dependencies considered:  
# selenium  
#install system packages  
# libxml2 (required by R XML library), java runtime environment (required by
MELTING), libssl-dev/unstable required by openssl package, libgsl0ldbl:
required for viennaRNA,  
# python-pip is necessary to install selenium for python (retrieval of
template seqs)  
# ensure that apt-get update works  
# pandoc (rmarkdown reports) requires latex for PDF output  
# libmysqlclient-dev: required for RMySQL pkg  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y libfontconfig1 libxml2-dev default-
jre libssl-dev/unstable libv8-dev libgslcblas0 python-pip pandoc texlive
texlive-latex-extra libmysqlclient-dev  
# && rm -rf /var/lib/apt/lists/*  
RUN pip install selenium  
WORKDIR /srv/  
RUN mkdir primer_design  
ADD . primer_design  
# install openPrimeR package to install all the dependencies of the tool  
RUN Rscript primer_design/src/install.R FALSE TRUE  
#update shiny server conf and configure it to run the primer design tool in
single app mode  
ADD shiny-server.conf /etc/shiny-server/shiny-server.conf  
COPY .docker_bashrc /home/shiny/.bashrc  
WORKDIR /srv/primer_design  


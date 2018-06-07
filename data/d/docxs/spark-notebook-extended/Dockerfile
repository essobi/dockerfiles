########################################################################  
# Dockerfile for Jupyter notebooks with python 3, pySpark & R support  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Component: Jupyter with python 3, pySpark and R  
# Author: pjan vandaele <pjan@pjan.io>  
# Scm url: https://github.com/docxs/docker-spark-notebook  
# License: MIT  
########################################################################  
  
# Pull base image  
FROM \  
docxs/spark-notebook:latest  
  
# Maintainer details  
MAINTAINER \  
pjan vandaele "pjan@pjan.io"  
  
# Add configuration files  
ADD config /src/config  
  
# Installing additional support for jupyter  
RUN apt-prepare \  
&& echo "Installing R support ..." \  
&& echo "deb http://cran.rstudio.com/bin/linux/debian wheezy-cran3/" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480 \  
&& apt-get update \  
&& apt-get install -q -y \  
r-base \  
r-base-dev \  
libreadline-dev \  
r-cran-boot \  
r-cran-class \  
r-cran-cluster \  
r-cran-codetools \  
r-cran-foreign \  
r-cran-kernsmooth \  
r-cran-lattice \  
r-cran-mass \  
r-cran-matrix \  
r-cran-mgcv \  
r-cran-nlme \  
r-cran-nnet \  
r-cran-rpart \  
r-cran-spatial \  
r-cran-survival \  
&& echo 'options(repos=structure(c(CRAN="http://cran.rstudio.com")))' >>
/etc/R/Rprofile.site \  
&& echo "install.packages(c('ggplot2', 'XML', 'plyr', 'randomForest', 'Hmisc',
'stringr', 'RColorBrewer', 'reshape', 'reshape2'))" | R --no-save \  
&& echo "install.packages(c('RCurl', 'devtools'))" | R --no-save \  
&& echo "install.packages(c('rzmq','repr','IRkernel','IRdisplay'), repos =
c('http://irkernel.github.io/', getOption('repos')), type = 'source');
IRkernel::installspec()" | R --no-save \  
&& mkdir -p /usr/local/share/jupyter/kernels/ir/ \  
&& cp -r /src/config/ir_kernel/* /usr/local/share/jupyter/kernels/ir/ \  
&& apt-cleanup  
  
# Run bootstrap on container launch  
ENTRYPOINT \  
["bootstrap"]  
  
# Default command  
CMD \  
["-d"]  


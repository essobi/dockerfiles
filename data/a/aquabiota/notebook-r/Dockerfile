# -*- mode: ruby -*-  
# vi: set ft=ruby :  
# docker run -d -v $HOME/data:/home/aqua/data -v
/absolute/path/to/your/git/directory:/home/aqua/workspace/git -v
$(pwd):/home/aqua/workspace/notebooks --name jupyter -p 8889:8889
aquabiota/notebook-r jupyter notebook --ip='*' --port=8889 --no-browser  
# MODIFIED FROM: https://www.digitalocean.com/community/tutorials/how-to-
install-r-on-ubuntu-16-04-2  
# plus check key here: https://www.rosehosting.com/blog/install-r-on-ubuntu/  
FROM aquabiota/notebook-base:latest  
  
LABEL maintainer "Aquabiota Solutions AB <mapcloud@aquabiota.se>"  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
  
#RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
E298A3A825C0D65DFD57CBB651716619E084DAB9  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
# sudo add-apt-repository ppa:git-core/ppa  
# RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list  
# RUN apt-get update && \  
# apt-get install -y r-base r-base-dev  
  
USER $NB_USER  
# Create a the user R-site-library to store packages  
RUN mkdir $HOME/R-site-library/  
RUN conda install -y -c conda-forge r-devtools r-rcurl  
#  
RUN conda install -y -c conda-forge r-irkernel r-irdisplay r-repr r-rzmq  
#  
RUN conda install -y -c conda-forge r-base r-rgdal  
RUN conda install -y -c conda-forge rpy2  
RUN conda install -y -c conda-forge r-ggplot2 r-nloptr r-broom r-tidyr  
RUN conda install -y -c conda-forge r-dplyr r-spatial r-jsonlite r-stringr \  
r-reshape2 r-data.table r-hmisc r-reshape r-ggthemes  
RUN conda install -y -c conda-forge r-car r-psych r-mgcv r-randomforest r-rocr
\  
r-raster r-leaflet r-sqldf r-geosphere r-xml r-xml2  
RUN conda install -y -c conda-forge r-abind r-proc r-nnet r-gbm r-rpart r-mass
r-gam r-gamlss  
# The following packages are not in r-essentials  
# RUN conda install -y -c r r-ncf r-sdmtools r-dismo r-biomod2  
RUN conda config \--add channels r  
## NOT TESTED from: https://www.anaconda.com/blog/developer-blog/conda-data-
science/  
# RUN conda skeleton cran biomod2 # PresenceAbsence  
# RUN conda build r-biomod2 # r-presenceabsence/  
# RUN conda install -y r-biomod2  
  
USER root  
# Install R packages  
# COPY rpackages.R /sbin/rpackages.R  
# RUN chmod +x /sbin/rpackages.R  
# RUN /sbin/rpackages.R  
RUN apt-get update && apt-get dist-upgrade -yq && apt-get autoremove -y  
# Ensure writing access to user to following dirs  
RUN chown -R $NB_USER:users $HOME/.local && \  
chown -R $NB_USER:users $HOME/R-site-library && \  
chown -R $NB_USER:users $WORKSPACE_DIR  
  
# /usr/local/lib/R/site-library  
# chown -R $NB_USER:users /usr/local/lib/R/site-library && \  
  
  
# default user starts the container  
USER $NB_USER  


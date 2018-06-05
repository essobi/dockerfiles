  
FROM jupyter/all-spark-notebook:latest  
MAINTAINER Paolo D. <p.donoriodemeo@cineca.it>  
  
##########################  
USER root  
  
# Add needed operative system packages for R caret and python brunel libraries  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends ed && \  
apt-get install -y --no-install-recommends -t jessie-backports openjdk-8-jdk
&& \  
rm -rf /var/lib/apt/lists/* && \  
ln -s /bin/tar /bin/gtar  
  
##########################  
USER $NB_USER  
# Install brunel and caret  
# FIXME: Improve R installation  
RUN pip3 install brunel  
RUN echo 'install.packages("caret", lib="/opt/conda/lib/R/library",
repo="http://cran.us.r-project.org")' > inst.R \  
&& Rscript inst.R && rm inst.R  
  
##########################  
# Add notebook starter  
USER root  
COPY nbstart.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/nbstart.sh  
CMD [ "nbstart.sh" ]  
USER $NB_USER  


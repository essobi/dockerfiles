# copyright 2017-2018 Regents of the University of California and the Broad
Institute. All rights reserved.  
FROM r-base:3.1.3  
RUN mkdir /build  
  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install build-essential --yes && \  
apt-get install python-dev --yes && \  
apt-get install default-jre --yes && \  
wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py &&\  
pip install awscli && \  
apt-get update && \  
apt-get install curl --yes  
  
# RUN pip install awscli  
#RUN apt-get update && \  
# apt-get install curl --yes  
COPY common/container_scripts/misc/Cairo_1.5-9.tar.gz
/build/Cairo_1.5-9.tar.gz  
  
RUN mkdir packages && \  
cd packages && \  
curl -O http://cran.r-project.org/src/base/R-3/R-3.0.3.tar.gz && \  
tar xvf R-3.0.3.tar.gz && \  
apt-get install libfreetype6=2.5.2-3+deb8u2 --yes --force-yes && \  
apt-get install libfreetype6-dev --yes --force-yes && \  
apt-get install libfontconfig1-dev --yes --force-yes && \  
apt-get install libcairo2-dev --yes --force-yes && \  
apt-get install libxt-dev --yes --force-yes && \  
apt-get install libxml2-dev --yes && \  
apt-get install libcurl4-gnutls-dev --yes && \  
apt-get install mesa-common-dev --yes && \  
apt-get install --yes libglu1-mesa-dev freeglut3-dev bwidget &&\  
cd R-3.0.3 && \  
./configure --with-x=no --without-x --with-cairo --with-libpng && \  
make && \  
make check && \  
make install && \  
R CMD INSTALL /build/Cairo_1.5-9.tar.gz  
  
COPY common/container_scripts/runS3OnBatch.sh /usr/local/bin/runS3OnBatch.sh  
COPY common/container_scripts/installPackages.R-2
/build/source/installPackages.R  
COPY sources.list /etc/apt/sources.list  
COPY common/container_scripts/runLocal.sh /usr/local/bin/runLocal.sh  
#COPY Rprofile.gp.site ~/.Rprofile  
COPY Rprofile.gp.site /usr/local/lib/R/etc/Rprofile.site  
RUN chmod ugo+x /usr/local/bin/runS3OnBatch.sh  
ENV R_LIBS_S3=/genepattern-server/Rlibraries/R303/rlibs  
ENV R_LIBS=/usr/local/lib/R/site-library  
ENV R_HOME=/usr/local/lib64/R  
  
COPY runS3Batch_prerun_custom.sh /usr/local/bin/runS3Batch_prerun_custom.sh  
COPY runS3Batch_postrun_custom.sh /usr/local/bin/runS3Batch_postrun_custom.sh  
  
CMD ["/usr/local/bin/runS3OnBatch.sh" ]  
  


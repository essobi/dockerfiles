from thomaschln/r-devtools  
  
################################################################################  
# Install plink, copy pasted from  
# https://github.com/GELOG/plink/blob/v1.07/plink-1.07-bin/docker/Dockerfile  
# Removed installation of unzip and wget (already included) and autoremove  
# Changed to http://zzz.bwh.harvard.edu (March 2017)  
################################################################################  
# Environment variables  
env PLINK_VERSION 1.07  
env PLINK_HOME /usr/local/plink  
env PATH $PLINK_HOME:$PATH  
  
run wget http://zzz.bwh.harvard.edu/plink/dist/plink-$PLINK_VERSION-x86_64.zip
&& \  
unzip plink-$PLINK_VERSION-x86_64.zip -d /usr/local/ && \  
rm plink-$PLINK_VERSION-x86_64.zip && \  
cd /usr/local && \  
ln -s plink-$PLINK_VERSION-x86_64 $PLINK_HOME && \  
rm -rf /var/lib/apt/lists/*  
  
# WORKAROUND: plink hangs if not started with '--noweb' option  
# See issue #1  
RUN echo '#!/bin/bash' > /usr/local/bin/plink && \  
echo '#Launch the real plink script forcing the --noweb argument' >>
/usr/local/bin/plink && \  
echo '/usr/local/plink/plink --noweb "$@"' >> /usr/local/bin/plink && \  
chmod a+x /usr/local/bin/plink  
  
################################################################################  
# Install SHAPEIT  
# https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.html  
################################################################################  
run wget -O shapeit.tgz
https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.v2.r837.GLIBCv2.12.Linux.static.tgz
\  
&& tar -zxvf shapeit.tgz  
  
################################################################################  
# Install SNPClust  
################################################################################  
  
run apt-get update  
run apt-get install -t unstable -y libnetcdf-dev  
run R -e "source('https://bioconductor.org/biocLite.R');biocLite('GWASTools')"  
run R -e "devtools::install_github('ThomasChln/snpclust')"  
run R -e "install.packages(c('data.table', 'dplyr', 'knitr', 'proto'))"  
run R -e "devtools::install_github('zhengxwen/SNPRelate')"  
  


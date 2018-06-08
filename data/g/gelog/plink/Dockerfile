# Pull base image  
FROM ubuntu:14.04.2  
# Installation instructions:
http://pngu.mgh.harvard.edu/~purcell/plink/download.shtml#latest  
# Environment variables  
ENV PLINK_VERSION 1.07  
ENV PLINK_HOME /usr/local/plink  
ENV PATH $PLINK_HOME:$PATH  
  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y unzip wget && \  
wget
http://pngu.mgh.harvard.edu/~purcell/plink/dist/plink-$PLINK_VERSION-x86_64.zip
&& \  
unzip plink-$PLINK_VERSION-x86_64.zip -d /usr/local/ && \  
rm plink-$PLINK_VERSION-x86_64.zip && \  
cd /usr/local && \  
ln -s plink-$PLINK_VERSION-x86_64 $PLINK_HOME && \  
DEBIAN_FRONTEND=noninteractive apt-get autoremove -y unzip wget && \  
rm -rf /var/lib/apt/lists/*  
  
# WORKAROUND: plink hangs if not started with '--noweb' option  
# See issue #1  
RUN echo '#!/bin/bash' > /usr/local/bin/plink && \  
echo '#Launch the real plink script forcing the --noweb argument' >>
/usr/local/bin/plink && \  
echo '/usr/local/plink/plink --noweb "$@"' >> /usr/local/bin/plink && \  
chmod a+x /usr/local/bin/plink  
  
# Set the default action to print plink's options  
ENTRYPOINT ["/usr/local/bin/plink"]  
  


FROM icaoberg/matlabmcr2017a  
  
###############################################################################################  
MAINTAINER Ivan E. Cao-Berg <icaoberg@andrew.cmu.edu>  
LABEL Description="CellOrganizer"  
LABEL Vendor="Murphy Lab in the Computational Biology Department at Carnegie
Mellon University"  
LABEL Web="http://murphylab.cbd.cmu.edu"  
LABEL Version="2.7.2"  
###############################################################################################  
  
###############################################################################################  
# INSTALL CELLORGANIZER BINARIES  
WORKDIR /home/murphylab  
USER root  
RUN echo "Downloading CellOrganizer v2.7.2" && \  
cd ~/ && \  
wget -nc --quiet
http://www.cellorganizer.org/Downloads/v2.7/docker/v2.7.2/cellorganizer-v2.7.2-binaries.tgz
&& \  
tar -xvf cellorganizer-v2.7.2-binaries.tgz && \  
rm cellorganizer-v2.7.2-binaries.tgz && \  
mv cellorganizer-binaries /opt && \  
chmod +x /opt/cellorganizer-binaries/img2slml && \  
chmod +x /opt/cellorganizer-binaries/slml2img && \  
chmod +x /opt/cellorganizer-binaries/slml2report && \  
chmod +x /opt/cellorganizer-binaries/slml2info && \  
ln -s /opt/cellorganizer-binaries/img2slml /usr/local/bin/img2slml && \  
ln -s /opt/cellorganizer-binaries/slml2img /usr/local/bin/slml2img && \  
ln -s /opt/cellorganizer-binaries/slml2report /usr/local/bin/slml2report && \  
ln -s /opt/cellorganizer-binaries/slml2info /usr/local/bin/slml2info  
###############################################################################################  
  
###############################################################################################  
USER murphylab  
RUN echo "Downloading models" && \  
wget -nc --quiet
http://www.cellorganizer.org/Downloads/v2.7/docker/v2.7.2/cellorganizer-v2.7.2-models.tgz
&& \  
tar -xvf cellorganizer-v2.7.2-models.tgz && \  
rm -f cellorganizer-v2.7.2-models.tgz  
  
COPY demos cellorganizer/demos  
USER root  
RUN find /home/murphylab/cellorganizer/demos -name "*.sh" -exec chmod +x {} \;  
RUN chown -Rv murphylab:users /home/murphylab/cellorganizer  
USER murphylab  
###############################################################################################  


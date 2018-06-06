# codonPhyML  
#  
# Uses Markovian codon models of evolution in phylogeny reconstruction.  
# http://codonphyml.sourceforge.net  
#  
# VERSION 1.0.0  
FROM gawbul/docker-bio-linux8  
MAINTAINER Bruno Vieira <mail@bmpvieira.com>  
  
LABEL Description="Uses Markovian codon models of evolution in phylogeny
reconstruction. http://codonphyml.sourceforge.net" Version="1.0.0"  
  
USER root  
  
RUN cd /opt ;\  
wget
http://downloads.sourceforge.net/project/codonphyml/codonPhyML_dev_1.00_201407.24.zip
;\  
unzip codonPhyML_dev_1.00_201407.24.zip ;\  
cd codonPHYML_dev ;\  
chmod +x make_phyml ;\  
./make_phyml  
  
ENV PATH /opt/codonPHYML_dev/src/codonphyml:$PATH  
  
CMD /opt/codonPHYML_dev/src/codonphyml  


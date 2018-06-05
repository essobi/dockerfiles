FROM comics/centos  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Software: ncbi-blast+  
# Software Version: 2.4.0  
# Software Website: http://blast.ncbi.nlm.nih.gov  
# Description: ncbi-blast+  
##############################################################  
  
ENV VERSION=2.4.0  
  
RUN yum install -y \  
parallel \  
ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/$VERSION/ncbi-
blast-$VERSION+-2.x86_64.rpm ; \  
yum clean all  
CMD ["/bin/bash"]  
  


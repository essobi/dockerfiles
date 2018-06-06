FROM centos:6  
  
RUN \  
yum install -y tar bzip2 && \  
yum clean all && \  
curl -L https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
-o /tmp/miniconda.sh && \  
bash /tmp/miniconda.sh -b -p /opt/conda && \  
/opt/conda/bin/conda update -y conda && \  
rm -f /tmp/miniconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  


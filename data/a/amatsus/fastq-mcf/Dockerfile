FROM docker.io/centos:7  
MAINTAINER Akihiro Matsushima <amatsusbit@gmail.com>  
  
ADD run_wrapper.py /usr/local/bin  
RUN yum -y update && \  
yum -y install gcc-c++ make subversion && \  
svn checkout https://ea-utils.googlecode.com/svn/trunk /opt/ea-utils && \  
cd /opt/ea-utils/clipper && \  
PREFIX=/opt/ea-utils/clipper make fastq-mcf && \  
rm -f sparsehash-2.0.2/*.o  
  
ENTRYPOINT [ "/usr/local/bin/run_wrapper.py", "/opt/ea-utils/clipper/fastq-
mcf" ]  
CMD ["--help"]  


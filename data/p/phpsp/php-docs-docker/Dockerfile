FROM phpsp/php7:7.0  
MAINTAINER Hussani Oliveira  
  
RUN echo $PATH  
  
RUN apt-get update && \  
apt-get install -y subversion && \  
TMP_FOLDER=/phd-binaries \  
&& mkdir -p ${TMP_FOLDER} \  
&& cd ${TMP_FOLDER} \  
&& wget https://github.com/php/phd/archive/master.tar.gz \  
&& tar -zxvf master.tar.gz \  
&& cd phd-master \  
&& pear install package.xml package_generic.xml package_php.xml  


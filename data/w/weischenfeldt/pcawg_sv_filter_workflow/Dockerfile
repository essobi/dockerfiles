#############################################################  
# Dockerfile to build SV filter container  
#############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:16.10  
  
# File Author / Maintainer  
MAINTAINER Joachim Weischenfeldt < joachim.weischenfeldt@gmail.com>  
  
# Setup packages  
USER root  
  
ADD requirements.txt /root/requirements.txt  
  
RUN apt-get -m update && apt-get install -y apt-utils tar git curl nano wget
dialog \  
net-tools build-essential python python-dev python-distribute python-pip
r-base \  
r-base-dev tabix cython sudo bedtools vcftools \  
&& pip install --no-cache-dir --upgrade pip && hash -r \  
&& pip install --no-cache-dir -r /root/requirements.txt \  
&& rm /root/requirements.txt  
  
ADD code/* /opt/code/  
ADD code/annotateMergedSvCalls_delly_pcawg_crome.sh
/usr/bin/annotateMergedSvCalls_delly_pcawg_crome.sh  
RUN chmod +x /usr/bin/annotateMergedSvCalls_delly_pcawg_crome.sh  
ADD bin/* /opt/bin/  
ADD code/run_sv_filter.py /usr/bin/run_sv_filter.py  
RUN chmod +x /usr/bin/run_sv_filter.py  
  
RUN mkdir -p /usr/svCallCollection \  
&& wget --no-check-certificate -P /usr/svCallCollection
https://bricweb.sund.ku.dk/bric-
data/joachim/pcawg/svCallCollectionsPCAWG.tar.gz  
ENV PCAWG_FILTER_ETC /etc/pcawg_filter_sv  
ADD files/* $PCAWG_FILTER_ETC/files/  
  
  
RUN groupadd -r -g 1000 ubuntu && useradd -ms /bin/bash -g ubuntu -u 1000
ubuntu  
USER ubuntu  
  
WORKDIR /home/ubuntu  
  
  
# by default /bin/bash is executed  
CMD ["/bin/bash"]  


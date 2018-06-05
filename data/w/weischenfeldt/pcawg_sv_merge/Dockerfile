#############################################################  
# Dockerfile to build SV merge container  
#############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:16.10  
  
# File Author / Maintainer  
MAINTAINER Joachim Weischenfeldt < joachim.weischenfeldt@gmail.com>  
  
# Setup packages  
USER root  
ADD files/* /root/  
  
RUN apt-get -m update && apt-get install -y apt-utils tar git curl nano wget
dialog \  
net-tools build-essential python python-dev python-distribute python-pip
r-base \  
r-base-dev tabix cython sudo bedtools \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install --no-cache-dir --upgrade pip && hash -r \  
&& pip install --no-cache-dir -r /root/py_requirements.txt \  
&& /usr/bin/Rscript /root/r_install.Rscript \  
&& rm /root/r_install.Rscript /root/py_requirements.txt  
  
ADD scripts/* /opt/scripts/  
ADD scripts/run_sv_merge.py /usr/bin/run_sv_merge.py  
ADD pcawg6_sv_merge_master.sh /usr/bin/pcawg6_sv_merge_master.sh  
  
RUN chmod +x /usr/bin/pcawg6_sv_merge_master.sh \  
&& chmod +x /usr/bin/run_sv_merge.py  
  
ENV PCAWG_ETC /etc/pcawg6_merge_sv  
ADD data/blacklist_files $PCAWG_ETC/data/blacklist_files  
ADD data/PCAWG-QC_Summary-of-Measures.tsv $PCAWG_ETC/data  
ADD data/pcawg_release_mar2016.tsv $PCAWG_ETC/data  
ADD merge.ini $PCAWG_ETC/merge.ini  
  
RUN groupadd -r -g 1000 ubuntu && useradd -ms /bin/bash -g ubuntu -u 1000
ubuntu  
USER ubuntu  
  
WORKDIR /home/ubuntu  
  
VOLUME /datastore  
  
  
  
# by default /bin/bash is executed  
CMD ["/bin/bash"]  


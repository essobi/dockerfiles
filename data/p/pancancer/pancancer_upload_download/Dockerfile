FROM ubuntu:14.04  
MAINTAINER Brian O'Connor <boconnor@oicr.on.ca>  
RUN apt-get update && apt-get install -y wget  
RUN cd /opt && wget -t 5 --timeout=30 --no-check-certificate
https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.7/genetorrent-
download_3.8.7-ubuntu2.207-14.04_amd64.deb  
RUN cd /opt && wget -t 5 --timeout=30 --no-check-certificate
https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.7/genetorrent-
common_3.8.7-ubuntu2.207-14.04_amd64.deb  
RUN cd /opt && wget -t 5 --timeout=30 --no-check-certificate
https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.7/genetorrent-
upload_3.8.7-ubuntu2.207-14.04_amd64.deb  
RUN apt-get update && apt-get install -y libcurl3 libxqilla6 python  
RUN apt-get update && apt-get install -y libboost-program-options1.54.0
libboost-system1.54.0 libboost-filesystem1.54.0 libboost-regex1.54.0  
RUN apt-get update && apt-get install -y rsync  
RUN cd /opt && dpkg --install genetorrent-
download_3.8.7-ubuntu2.207-14.04_amd64.deb genetorrent-
common_3.8.7-ubuntu2.207-14.04_amd64.deb genetorrent-
upload_3.8.7-ubuntu2.207-14.04_amd64.deb  
RUN mkdir -p /opt/gt-download-upload-wrapper && cd /opt/gt-download-upload-
wrapper && wget --no-check-certificate https://github.com/ICGC-TCGA-
PanCancer/gt-download-upload-wrapper/archive/2.0.13.tar.gz && tar zxf
2.0.13.tar.gz  
RUN mkdir -p /opt/vcf-uploader && cd /opt/vcf-uploader && wget --no-check-
certificate https://github.com/ICGC-TCGA-PanCancer/vcf-
uploader/archive/2.0.9.tar.gz && tar zxf 2.0.9.tar.gz  
RUN apt-get update && apt-get install -y python-dev python-pip libxml-dom-perl
libxml-xpath-perl libjson-perl libxml-libxml-perl time libdata-uuid-libuuid-
perl libcarp-always-perl libipc-system-simple-perl libdata-uuid-perl curl vim
samtools tabix  
RUN pip install synapseclient python-dateutil elasticsearch xmltodict pysftp
paramiko  
RUN apt-get update && apt-get install -y sudo  
RUN useradd seqware  
# Test perl scripts  
RUN perl -c -I /opt/gt-download-upload-wrapper/gt-download-upload-
wrapper-2.0.13/lib /opt/vcf-uploader/vcf-uploader-2.0.9/gnos_upload_vcf.pl &&
\  
perl -c -I /opt/gt-download-upload-wrapper/gt-download-upload-
wrapper-2.0.13/lib /opt/vcf-uploader/vcf-uploader-2.0.9/gnos_download_file.pl
&& \  
perl -c -I /opt/gt-download-upload-wrapper/gt-download-upload-
wrapper-2.0.13/lib /opt/vcf-uploader/vcf-
uploader-2.0.9/get_donors_by_elastic_search.pl && \  
perl -c -I /opt/gt-download-upload-wrapper/gt-download-upload-
wrapper-2.0.13/lib /opt/vcf-uploader/vcf-uploader-2.0.9/synapse_upload_vcf.pl  


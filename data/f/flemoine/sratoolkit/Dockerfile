FROM ubuntu  
  
MAINTAINER Frederic Lemoine  
  
RUN apt-get update --fix-missing \  
&& apt-get install -q -y wget  
  
RUN \  
wget -q http://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/2.5.7/sratoolkit.2.5.7-ubuntu64.tar.gz -O- \  
| tar xz -C /opt/ \  
&& mkdir /opt/sratoolkit \  
&& ln -s /opt/sratoolkit.2.5.7-ubuntu64/bin/* /opt/sratoolkit/  
  
RUN groupadd -g 1001 rnauser  
RUN useradd -d /home/rnauser -u 1001 -g 1001 -m -s /bin/bash rnauser  
USER rnauser  
ENV HOME /home/rnauser  
RUN \  
cd /home/rnauser/ && \  
wget http://download.asperasoft.com/download/sw/connect/3.6.2/aspera-
connect-3.6.2.117442-linux-64.tar.gz && \  
tar -xzvf aspera-connect-3.6.2.117442-linux-64.tar.gz && \  
sh aspera-connect-3.6.2.117442-linux-64.sh && \  
rm aspera-connect-3.6.2.117442-linux-64.tar.gz  
USER root  
ENV HOME /root/  
ENV PATH
/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/home/rnauser/.aspera/connect/bin/:/opt/sratoolkit  
ENV ASCPKEY /home/rnauser/.aspera/connect/etc/asperaweb_id_dsa.openssh  
  
RUN apt-get remove -q -y wget && apt-get autoremove -y  


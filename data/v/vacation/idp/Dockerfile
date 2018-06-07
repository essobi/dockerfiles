from vacation/lsc:2.0.1  
# Based on the short read correction software LSC because of  
# shared dependencies  
# Highly recommend using short read correction software LoRDEC  
# with the IDP because it is much faster  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
wget \  
python-scipy \  
zip  
  
# Include LoRDEC - it has a boutique open source license I can only find  
# in their full source which is here:  
# http://www.atgc-montpellier.fr/download/sources/lordec/LoRDEC-0.6.tar.gz  
RUN cd /Source \  
&& wget http://gatb-tools.gforge.inria.fr/versions/bin/LoRDEC-0.6-Linux.tar.gz
\  
&& tar -xzf LoRDEC-0.6-Linux.tar.gz \  
&& rm LoRDEC-0.6-Linux.tar.gz \  
&& cp LoRDEC-0.6-Linux/bin/* /usr/local/bin/ \  
&& rm -r LoRDEC-0.6-Linux/  
  
# Include GMAP  
# note that GMAP is not open source to everyone. please abide by the license.  
RUN cd /Source \  
&& wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2017-09-11.tar.gz \  
&& tar -xzf gmap-gsnap-2017-09-11.tar.gz \  
&& rm gmap-gsnap-2017-09-11.tar.gz \  
&& cd gmap-2017-09-11 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd /Source \  
&& rm -r gmap-2017-09-11  
  
## Include IDP  
RUN cd /Source \  
&& git clone https://github.com/jason-weirather/IDP.git \  
&& rm -r /Source/IDP/example \  
&& pip install seq-tools==1.0.9  
ENV PATH="/Source/IDP/bin:${PATH}"  
## Include hisat2 as a more modern short read aligner  
RUN cd /Source \  
&& wget
ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.1.0-Linux_x86_64.zip
\  
&& unzip hisat2-2.1.0-Linux_x86_64.zip \  
&& rm hisat2-2.1.0-Linux_x86_64.zip \  
&& cd hisat2-2.1.0  
ENV PATH="/Source/hisat2-2.1.0:${PATH}"  
## Bring in samtools  
RUN apt-get upgrade -y \  
&& apt-get install -y \  
curl libncurses5-dev libbz2-dev liblzma-dev \  
&& cd /Source \  
&& curl -L
https://github.com/samtools/samtools/releases/download/1.5/samtools-1.5.tar.bz2
| tar -xj \  
&& cd samtools-1.5 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd /Source \  
&& rm -r samtools-1.5  


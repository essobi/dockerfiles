# OpenJDK version of Java 8 on top of a generic Debian Linux OS  
FROM java:openjdk-8-jre  
  
MAINTAINER VDJServer <vdjserver@utsouthwestern.edu>  
  
# uncomment these if building behind UTSW proxy  
#ENV http_proxy 'http://proxy.swmed.edu:3128/'  
#ENV https_proxy 'https://proxy.swmed.edu:3128/'  
#ENV HTTP_PROXY 'http://proxy.swmed.edu:3128/'  
#ENV HTTPS_PROXY 'https://proxy.swmed.edu:3128/'  
# updates of the base system  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
r-base r-base-dev \  
emacs vim \  
git mercurial \  
libbz2-dev \  
libxml2-dev \  
libxslt-dev \  
python \  
python-dev \  
python-sphinx \  
python-pip \  
wget \  
zlib1g-dev \  
libssl-dev \  
python3 \  
python3-pip \  
python3-scipy \  
libssh2-1-dev \  
libcurl4-openssl-dev \  
libyaml-dev \  
staden \  
autoconf  
  
# python2 packages  
RUN pip install \  
numpy \  
lxml \  
argparse \  
BeautifulSoup4 \  
reportlab \  
biopython  
  
RUN pip3 install \  
pandas \  
biopython \  
presto \  
changeo  
  
# htslib  
RUN mkdir htslib  
RUN cd htslib && wget https://github.com/samtools/htslib/archive/1.6.tar.gz  
RUN cd htslib && tar zxf 1.6.tar.gz  
RUN cd htslib/htslib-1.6 && autoheader && autoconf && ./configure && make &&
make install  
  
# samtools  
RUN mkdir samtools  
RUN cd samtools && wget
https://github.com/samtools/samtools/archive/1.6.tar.gz  
RUN cd samtools && tar zxf 1.6.tar.gz  
RUN cd samtools/samtools-1.6 && autoheader && autoconf -Wno-syntax &&
./configure && make && make install  
  
# bcftools  
RUN mkdir bcftools  
RUN cd bcftools && wget
https://github.com/samtools/bcftools/archive/1.6.tar.gz  
RUN cd bcftools && tar zxf 1.6.tar.gz  
RUN cd bcftools/bcftools-1.6 && autoheader && autoconf && ./configure && make
&& make install  
  
# update linked libraries  
RUN ldconfig  


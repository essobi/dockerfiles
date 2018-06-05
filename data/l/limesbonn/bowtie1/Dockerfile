############################################################  
# Dockerfile to build Bowtie container images  
# Based on Ubuntu  
############################################################  
# Set the base image to r-base  
FROM r-base  
# File Author / Maintainer  
MAINTAINER Hartmut Schultze  
# Update the repository sources list  
RUN apt-get update  
# Install compiler and perl stuff  
RUN apt-get install -f --yes apt-utils git fastx-toolkit \  
curl \  
python \  
python2.7-dev \  
python-pip \  
python-numpy \  
python-matplotlib \  
wget  
  
# gcc-multilib build-essential zlib1g-dev  
  
# Install STAR  
WORKDIR /tmp  
RUN git clone https://github.com/BenLangmead/bowtie.git  
WORKDIR /tmp/bowtie  
RUN git checkout v1.1.1  
# Patch Makefile  
RUN sed -i 's/ifneq (,$(findstring 13,$(shell uname -r)))/ifneq (,$(findstring
Darwin 13,$(shell uname -sr)))/' Makefile  
RUN sed -i 's/EXTRA_CFLAGS =/EXTRA_CFLAGS = -static/' Makefile  
RUN sed -i 's/EXTRA_CXXFLAGS =/EXTRA_CXXFLAGS = -static/' Makefile  
# Compile  
RUN make  
RUN cp -p bowtie bowtie-* /usr/local/bin  
# Cleanup  
RUN rm -rf /tmp/bowtie  
  
#Install HtSeq  
RUN curl
https://pypi.python.org/packages/source/H/HTSeq/HTSeq-0.6.1.tar.gz#md5=b7f4f38a9f4278b9b7f948d1efbc1f05
> HTSeq-0.6.1.tar.gz && \  
tar -xzf HTSeq-0.6.1.tar.gz && \  
rm HTSeq-0.6.1.tar.gz && \  
cd HTSeq-0.6.1 && \  
ls && \  
python setup.py install --user  
  
# install R packages  
RUN Rscript -e 'install.packages(c("data.table","dplyr","stringdist"))'  
RUN cpan MCE  
RUN cpan MCE:Shared  
  
RUN apt-get clean  
RUN apt-get remove --yes --purge build-essential gcc-multilib apt-utils
zlib1g-dev vim  
WORKDIR /root  
CMD ["/bin/bash"]  


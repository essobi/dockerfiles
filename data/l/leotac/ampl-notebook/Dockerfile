FROM ubuntu:16.04  
LABEL maintainer="leonardo.taccari@gmail.com"  
  
# Install utils  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
vim \  
less \  
bzip2 \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install miniconda, iampl and other useful python modules  
RUN cd /tmp && wget https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh \  
&& chmod +x Miniconda3-latest-Linux-x86_64.sh \  
&& bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda \  
&& rm Miniconda3-latest-Linux-x86_64.sh \  
&& /opt/miniconda/bin/conda install jupyter ipython matplotlib pandas -y \  
&& /opt/miniconda/bin/conda clean --all -y \  
&& /opt/miniconda/bin/pip install amplpy  
  
# AMPL location (default: freely available demo version)  
ARG AMPL=http://ampl.com/demo/ampl.linux64.tgz  
  
# If $AMPL is a local compressed file, it will be automatically  
# uncompressed into /opt by the ADD command.  
# The script find_ampl.sh tries to ensure that /opt/ampl  
# will point to a directory containing the ampl binaries.  
ADD ${AMPL} /opt  
COPY scripts /opt/scripts  
RUN /opt/scripts/find_ampl.sh  
  
# Add ampl and conda/python to the path  
ENV PATH /opt/miniconda/bin:/opt/ampl:$PATH  
  
# ipython/jupyter configurations  
EXPOSE 8888  
WORKDIR /root  
CMD ["/opt/scripts/start_notebook.sh"]  


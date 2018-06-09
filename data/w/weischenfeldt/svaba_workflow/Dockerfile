#############################################################  
# Dockerfile to build svaba container  
#############################################################  
FROM centos:7.3.1611  
MAINTAINER Francesco Favero <francesco.favero@bric.ku.dk>  
RUN yum install -y epel-release  
RUN yum install -y git zlib-devel gcc gcc-c++ \  
gcc-gfortran make which wget bwa \  
&& curl
"https://bitbucket.org/weischenfeldt/computerome_weischenfeldt_docker/raw/4c35870a6a90fb77640db8d89f8528e11d5e7770/modules/apps/samtools/1.2/bin/samtools"
> /usr/bin/samtools \  
&& chmod +x /usr/bin/samtools  
  
RUN mkdir /databases && chmod -R 7777 /databases \  
&& mkdir /data && chmod -R 7777 /data  
  
RUN git clone --recursive https://github.com/walaj/svaba \  
&& cd svaba && git checkout 4a0606eba1bfd43c3d38433b27ac7f5e4887bc1e \  
&& git submodule update --recursive \  
&& ./configure \  
&& make \  
&& make install \  
&& cp bin/svaba /usr/bin \  
&& cd ../ && rm -rf svaba  
  
ADD run_svaba.py /usr/bin/run_svaba  
RUN chmod +x /usr/bin/run_svaba  
RUN useradd -ms /bin/bash docker  
USER docker  
WORKDIR /home/docker  
  
CMD ["/bin/bash"]  


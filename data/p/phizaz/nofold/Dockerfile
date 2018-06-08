FROM phizaz/bioconda:python2  
  
########################################  
# ROOT MODE  
########################################  
  
###### SETUP LOCARNA 1.8.7 ###############  
RUN conda install -y locarna=1.8.7 && conda clean --yes --all  
  
###### SETUP RNAZ ###############  
RUN conda install -y rnaz=2.1 && conda clean --yes --all  
  
###### SETUP INFERNAL ###############  
COPY infernal-1.0.2.tar.gz /tmp/infernal.tar.gz  
RUN mkdir -p /tmp/infernal \  
&& tar -xf /tmp/infernal.tar.gz -C /tmp/infernal --strip-components=1 \  
&& cd /tmp/infernal \  
&& chmod +x ./configure \  
&& ./configure --prefix=/usr/local \  
&& make -j4 \  
&& make install \  
&& rm -rf /tmp/*  
  
###### SETUP R-FASTCLUSTER ###############  
RUN Rscript -e 'install.packages("fastcluster",
repos="https://cloud.r-project.org/")'  
  
########################################  
# USER MODE  
########################################  
USER docker  
  
###### SETUP NOFOLD ###############  
COPY nofold_1.0.1.tar.gz /tmp  
RUN mkdir -p /home/docker/nofold \  
&& tar -xf /tmp/nofold_1.0.1.tar.gz -C /home/docker/nofold --strip=1  
  
RUN mkdir -p /home/docker/workdir  
WORKDIR /home/docker/workdir  
  
ENV WORKDIR=/home/docker/workdir  
ENV NOFOLD=/home/docker/nofold  
ENV SRC=/home/docker/nofold/src  


FROM phizaz/bioconda:python3  
  
########################################  
# ROOT MODE  
########################################  
  
###### SETUP VIENNARNA ###############  
COPY ViennaRNA-2.4.0.tar.gz /tmp/viennarna.tar.gz  
RUN mkdir -p /tmp/viennarna \  
&& tar -xf /tmp/viennarna.tar.gz -C /tmp/viennarna --strip-components=1 \  
&& cd /tmp/viennarna \  
&& chmod +x ./configure \  
&& ./configure --prefix=/usr/local \  
&& make -j4 \  
&& make install \  
&& rm -rf /tmp/*  
  
###### SETUP LOCARNA ###############  
COPY locarna-1.9.2.tar.gz /tmp/locarna.tar.gz  
RUN mkdir -p /tmp/locarna \  
&& tar -xf /tmp/locarna.tar.gz -C /tmp/locarna --strip-components=1 \  
&& cd /tmp/locarna \  
&& chmod +x ./configure \  
&& ./configure --prefix=/usr/local \  
&& make -j4 \  
&& make install \  
&& rm -rf /tmp/*  
  
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
  
###### SETUP CMFINDER ###############  
RUN conda install -y cmfinder=0.2 && conda clean --yes --all  
  
###### SETUP RNASHAPES ###############  
COPY RNAshapes-2.1.6.tar.gz /tmp/rnashapes.tar.gz  
RUN mkdir -p /tmp/rnashapes \  
&& tar -xf /tmp/rnashapes.tar.gz -C /tmp/rnashapes --strip-components=1 \  
&& cd /tmp/rnashapes \  
&& chmod +x ./configure \  
&& ./configure --prefix=/usr/local \  
&& make -j4 \  
&& make install \  
&& rm -rf /tmp/*  
  
###### SETUP GRAPHCLUST ###############  
COPY GraphClust-0.7.6.tar.gz /tmp/graphclust.tar.gz  
RUN mkdir -p /tmp/graphclust \  
&& tar -xf /tmp/graphclust.tar.gz -C /tmp/graphclust --strip-components=1 \  
&& cd /tmp/graphclust \  
&& chmod +x ./configure \  
&& ./configure --prefix=/usr/local \  
&& make -j4 \  
&& make install \  
&& rm -rf /tmp/*  
  
###### SETUP PERL DEPENDENCIES ###############  
RUN conda install -y perl-math-round perl-threaded && conda clean --yes --all  
  
###### SETUP OCTAVE #########################  
RUN conda install -y octave && conda clean --yes --all  
  
########################################  
# USER MODE  
########################################  
USER docker  
  
###### PREPARE THE WORKING DIR #########################  
RUN mkdir -p /home/docker/workdir  
WORKDIR /home/docker/workdir  
ENV WORKDIR=/home/docker/workdir  


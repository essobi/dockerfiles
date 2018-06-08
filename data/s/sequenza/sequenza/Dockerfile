FROM r-base:3.4.4  
MAINTAINER Francesco Favero <francesco.favero@bric.ku.dk>  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcurl4-openssl-dev libssl-dev \  
libxml2-dev \  
samtools \  
tabix \  
bwa \  
python python-dev python-setuptools python-pip \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget https://bitbucket.org/sequenza_tools/sequenza-utils/get/master.tar.gz
-O sequenza_tools.tar.gz \  
&& tar -xvpf sequenza_tools.tar.gz \  
&& cd sequenza_tools-sequenza-utils* && python setup.py test \  
&& python setup.py install --install-scripts=/usr/bin \  
&& cd ../ && rm -rf sequenza_tools* \  
&& mkdir /databases && chmod -R 7777 /databases \  
&& mkdir /data && chmod -R 7777 /data \  
&& pip install --no-cache-dir bio_pype \  
&& pype repos install --force sequenza  
  
VOLUME /databases /data  
  
ADD exec/install_sequenza.R /usr/local/install_sequenza.R  
RUN Rscript /usr/local/install_sequenza.R \  
&& rm /usr/local/install_sequenza.R  
ADD exec/run_sequenza.py /usr/bin/sequenza-pipeline  
RUN chmod +x /usr/bin/sequenza-pipeline  
RUN useradd -ms /bin/bash sequenza  
  
USER sequenza  
WORKDIR /home/sequenza  
  
CMD ["/bin/bash"]  


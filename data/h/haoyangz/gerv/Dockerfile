FROM haoyangz/matlab2014a-mcr8.3  
MAINTAINER Haoyang Zeng <haoyangz@mit.edu>  
  
RUN sudo apt-get update  
RUN sudo apt-get install -yq tar r-base make gcc libc6-dev Docker git git-core
git-email g++ gdb build-essential libboost-all-dev cmake mpich2 libmpich2-dev
python-numpy python-scipy python-matplotlib python-tk python-pip lzop  
RUN sudo apt-get -q -y install git git-core g++ build-essential libboost-all-
dev cmake r-base python-pip lzop libgsl0-dev  
  
RUN mkdir /scripts/  
RUN mkdir /seq_data/  
RUN mkdir /scripts/snp-kmer-scoring/  
RUN mkdir /scripts/preprocess/  
RUN mkdir /scripts/postprocess/  
RUN mkdir /mcrtmp/  
  
RUN mkdir /kmm  
RUN git clone https://thashim-ro:*SybT2X9@bitbucket.org/ddkang/ccm_testing.git
/kmm/master  
RUN cd /kmm/master; git checkout glm_v2  
RUN mkdir /kmm/master/build  
RUN cd /kmm/master/build; cmake ..  
  
RUN git clone https://thashim-
ro:*SybT2X9@bitbucket.org/thashim/delete_later.git /kmm/nocov  
RUN cd /kmm/nocov; git checkout no91  
RUN mkdir /kmm/nocov/build  
RUN cd /kmm/nocov/build; cmake ..  
  
RUN chmod -R 777 /kmm  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages('bitops')"  
RUN Rscript -e "install.packages('R.methodsS3')"  
RUN Rscript -e "install.packages('R.oo')"  
RUN Rscript -e "install.packages('R.utils')"  
RUN Rscript -e "install.packages('R.matlab')"  
  
ENV LD_LIBRARY_PATH /opt/mcr/v83/runtime/glnxa64:/opt/mcr/v83/bin/glnxa64/  
ENV XAPPLRESDIR /opt/mcr/v83/X11/app-defaults  
ENV PATH $PATH:$LD_LIBRARY_PATH:$XAPPLRESDIR  
ENV MCR_CACHE_ROOT /mcrtmp/  
  
ADD run.r /scripts/  
ADD seq_data/ /seq_data/  
ADD kmersnp_module /scripts/  
ADD preprocess/baseline/get_background_hg19_covar.R
/scripts/preprocess/baseline/  
ADD preprocess/baseline/get_background_hg19.R /scripts/preprocess/baseline/  
ADD preprocess/kmer_mat/prepare_kmer_mat.R /scripts/preprocess/kmer_mat/  
ADD postprocess/combineKSS/combine_snp.m /scripts/postprocess/combineKSS/  
  
RUN chmod +x /scripts/run.r  
RUN chmod -R 777 /scripts  
RUN chmod -R 777 /mcrtmp  


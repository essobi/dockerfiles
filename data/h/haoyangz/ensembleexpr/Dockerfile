FROM haoyangz/deepsea-predict-docker  
MAINTAINER Haoyang Zeng <haoyangz@mit.edu>  
  
RUN apt-get update;apt-get install -y vim default-jre lzop bedtools  
RUN pip install scikit-learn==0.17.1  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages('snow')"  
  
RUN mkdir /script  
RUN mkdir /script/preprocess  
RUN mkdir /script/data  
RUN mkdir /script/trained_model  
COPY preprocess /script/preprocess/  
COPY trained_model /script/trained_model/  
COPY data /script/data/  
COPY *.py /script/  
RUN cd /script/data; wget http://gerv.csail.mit.edu/hg19.in.lzo -q; lzop -d
hg19.in.lzo  
WORKDIR /script/  


FROM welliton/ga4gh-server:v0.3.6  
  
MAINTAINER Welliton Souza <well309@gmail.com>  
  
WORKDIR /data  
  
RUN wget https://github.com/ga4gh/ga4gh-server/releases/download/data/ga4gh-
example-data_4.6.tar \  
-O ga4gh-example-data.tar && \  
tar -xf ga4gh-example-data.tar --strip-components=1 && \  
rm ga4gh-example-data.tar && \  
ga4gh_repo init --force /data/registry.db && \  
ga4gh_repo add-dataset -d "Sample data from 1000 Genomes phase 3" \  
/data/registry.db 1kg-p3-subset && \  
ga4gh_repo add-referenceset -n GRCh37 \  
-d "Subset of GRCh37 used for demonstration" \  
/data/registry.db /data/GRCh37-subset.fa.gz && \  
ga4gh_repo add-variantset -n mvncall -R GRCh37 /data/registry.db \  
1kg-p3-subset /data && \  
ga4gh_repo add-readgroupset \--name HG00096 -R GRCh37 \  
-I /data/HG00096.bam.bai /data/registry.db \  
1kg-p3-subset /data/HG00096.bam && \  
ga4gh_repo add-readgroupset \--name HG00533 -R GRCh37 \  
-I /data/HG00533.bam.bai /data/registry.db \  
1kg-p3-subset /data/HG00533.bam && \  
ga4gh_repo add-readgroupset \--name HG00534 -R GRCh37 \  
-I /data/HG00534.bam.bai /data/registry.db \  
1kg-p3-subset /data/HG00534.bam  


FROM conda/miniconda3  
  
LABEL maintainer="alperyilmaz@gmail.com"  
  
RUN apt-get update && apt-get install -y --no-install-recommends libkeyutils-
dev \  
&& rm /var/lib/apt/lists/*debian*  
  
RUN conda install -c bioconda rnftools  
  
WORKDIR /data  


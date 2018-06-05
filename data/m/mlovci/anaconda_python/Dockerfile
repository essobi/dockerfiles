FROM mlovci/base  
  
MAINTAINER Michael Lovci <michaeltlovci@gmail.com>  
  
  
RUN apt-get update && apt-get upgrade -y  
  
ADD https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
/home/root/software/  
  
WORKDIR /home/root/software  
  
RUN ["chmod", "u+x", "Miniconda3-latest-Linux-x86_64.sh"]  
RUN ./Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda -f  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/miniconda/bin  
RUN conda install --yes cython numpy scipy scikit-learn pip pandas jupyter  
RUN pip install patsy && pip install seaborn brewer2mpl networkx
semantic_version statsmodels pybedtools jsonschema pytest sphinx numpydoc
sphinx_bootstrap_theme biopython  
RUN conda config --add channels r && conda config --add channels bioconda  
RUN conda install --yes pybedtools samtools htslib bcftools  
ENV PATH=/usr/local/miniconda/bin:$PATH  


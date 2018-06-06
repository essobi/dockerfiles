FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y wget bzip2 git  
WORKDIR /root  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  
RUN echo -e "\nyes\n" | bash Miniconda3-latest-Linux-x86_64.sh  
ENV
PATH=/root/miniconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN conda update -n base conda  
RUN conda config --add channels defaults  
RUN conda config --add channels conda-forge  
RUN conda config --add channels bioconda  
RUN conda install repeatmasker==4.0.6  
RUN git clone -b 'v1.0.4-beta' \--single-branch --depth 1
https://github.com/vetscience/Tools  
RUN cp Tools/Cwl/combinecats/combine.sh .  
RUN chmod uog+x combine.sh /root  
ENTRYPOINT ["/root/combine.sh"]  


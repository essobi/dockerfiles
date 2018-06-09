FROM continuumio/anaconda3  
  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# System packages  
RUN apt-get update && apt-get upgrade -y\  
&& apt-get install -y curl wget openssl libpcre3 gcc make gfortran \  
&& conda update -y conda \  
&& conda install -y -c conda-forge python=3 cython pandas rpy2 r-dbi r-feather
r-survival r-rmysql readline \  
&& conda clean --all \  
&& R --vanilla -e 'install.packages("survey",
repos="http://R-Forge.R-project.org")' \  
&& R --vanilla -e 'install.packages("MonetDB.R",
repos="http://R-Forge.R-project.org")' \  
&& mkdir -p /app  
  
WORKDIR /app  
  
EXPOSE 7777  
COPY . /app  
  
RUN pip install --no-cache-dir --upgrade pip \  
&& pip install --no-cache-dir -r requirements.txt \  
&& pip install -e . \  
&& apt-get purge --auto-remove -y gcc make gfortran \  
&& rm -rf /var/lib/apt/lists/* && apt-get clean  
  
ENV MALLOC_MMAP_THRESHOLD_ 1000000  
ENV MALLOC_MMAP_MAX_ 262144  
ENV MALLOC_MXFAST_ 0  
#RUN survey_stats work  
CMD survey_stats serve  


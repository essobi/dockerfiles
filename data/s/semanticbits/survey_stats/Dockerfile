FROM continuumio/anaconda3  
  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# System packages  
RUN apt-get update && apt-get install -y curl gcc wget make g++ openssl
libssl-dev libpcre3 libpcre3-dev zlib1g zlib1g-dev gfortran  
  
RUN conda update -y conda  
RUN conda install -y -c intel/label/test python=3 r-base=3.4.1 pandas scikit-
learn cython r-feather r-survival libiconv  
RUN R --vanilla -e 'install.packages("survey",
repos="http://R-Forge.R-project.org")'  
RUN R --vanilla -e 'install.packages("MonetDB.R",
repos="http://R-Forge.R-project.org")'  
#RUN R --vanilla -e 'install.packages("RMySQL",
repos="http://R-Forge.R-project.org")'  
RUN mkdir -p /app  
WORKDIR /app  
  
EXPOSE 7777  
RUN apt-get install -y libreadline-dev  
  
COPY . /app  
  
RUN pip install --no-cache-dir --upgrade pip  
RUN pip install --no-cache-dir -r requirements-dev.txt  
RUN pip install --no-cache-dir -r requirements.txt  
RUN pip install --no-cache-dir -r requirements-noconda.txt  
  
RUN pip install -e .  
  
ENV MALLOC_MMAP_THRESHOLD_ 1000000  
ENV MALLOC_MMAP_MAX_ 262144  
ENV MALLOC_MXFAST_ 0  


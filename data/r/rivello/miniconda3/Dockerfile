FROM debian:stable-20171210 as builder  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
ca-certificates \  
libmemcached-dev \  
libssl-dev \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists  
  
ENV miniconda_path=/miniconda3  
ENV miniconda_repo=https://repo.continuum.io/miniconda  
ENV miniconda_version=4.3.31  
ENV miniconda_filename=Miniconda3-${miniconda_version}-Linux-x86_64.sh  
  
RUN wget -q ${miniconda_repo}/${miniconda_filename} \  
&& bash ${miniconda_filename} -b -p ${miniconda_path} \  
&& rm ${miniconda_filename}  
  
ENV PATH=${miniconda_path}/bin:${PATH}  
RUN conda update -q -y --all  
  
COPY conda_requirements.yml .  
RUN conda env update -q -n base --file conda_requirements.yml \  
&& rm conda_requirements.yml  
  
RUN conda clean --yes --all  
  
RUN LDFLAGS=-fno-lto CPATH=${miniconda_path}/include \  
LIBRARY_PATH=${miniconda_path}/lib \  
pip install uwsgi  
  
  
FROM debian:stable-20171210  
RUN apt-get update \  
&& apt-get install -y ca-certificates \  
&& rm -rf /var/lib/apt/lists  
ENV miniconda_path=/miniconda3  
COPY \--from=builder ${miniconda_path} ${miniconda_path}  
ENV PATH=${miniconda_path}/bin:${PATH}  
ENV LD_LIBRARY_PATH=${miniconda_path}/lib  
ENV LC_CTYPE=C.UTF-8  


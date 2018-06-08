FROM debian:jessie-slim  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
WORKDIR /tmp  
  
# Global dependencies  
RUN apt-get update -qq --fix-missing \  
&& apt-get install -qqy --no-install-recommends \  
ca-certificates wget bzip2 less locate \  
&& apt-get purge --auto-remove -qqy \  
&& rm -rf /var/lib/apt/lists/*  
# Install miniconda  
COPY install_miniconda.sh /tmp  
RUN bash install_miniconda.sh \  
&& rm install_miniconda.sh  
ENV PATH /opt/conda/bin:$PATH  
  
# Misc dependencies  
RUN apt-get update -qq --fix-missing \  
&& apt-get install -qqy --no-install-recommends \  
libopenblas-base liblapack3gf liblapacke \  
mpich2 \  
ssh \  
&& apt-get purge --auto-remove -qqy \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  


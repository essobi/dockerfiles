FROM biocorecrg/debian-perlbrew-pyenv3:stretch  
  
# File Author / Maintainer  
MAINTAINER Toni Hermoso Pulido <toni.hermoso@crg.eu>  
  
ARG SUPPA_VERSION=2.3  
ARG CRAN_VERSION=34  
ARG SALMON_VERSION=0.9.1  
WORKDIR /tmp  
  
# Adding R  
RUN echo "deb http://cran.rstudio.com/bin/linux/debian stretch-
cran${CRAN_VERSION}/" >> /etc/apt/sources.list  
RUN apt-get install dirmngr  
RUN apt-key adv --keyserver keys.gnupg.net --recv-key
'E19F5F87128899B192B1A2C2AD5F960A256A04AF'  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends r-base r-base-dev  
  
# Install Salmon  
RUN apt-get install -y --no-install-recommends git gcc make g++ cmake
libboost-all-dev liblzma-dev libbz2-dev \  
ca-certificates zlib1g-dev curl unzip autoconf  
  
RUN curl -k -L https://github.com/COMBINE-
lab/salmon/archive/v${SALMON_VERSION}.tar.gz -o
salmon-v${SALMON_VERSION}.tar.gz && \  
tar xzf salmon-v${SALMON_VERSION}.tar.gz && \  
cd salmon-${SALMON_VERSION} && \  
mkdir build && \  
cd build && \  
cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local && make && make install  
  
# Installing SUPPA  
RUN mkdir -p /usr/local/suppa  
  
RUN curl --fail --silent --show-error --location --remote-name
https://github.com/comprna/SUPPA/archive/v${SUPPA_VERSION}.tar.gz  
RUN tar zxf v${SUPPA_VERSION}.tar.gz  
RUN cp -prf SUPPA-${SUPPA_VERSION}/* /usr/local/suppa  
RUN echo "#!/usr/bin/env python"|cat - /usr/local/suppa/suppa.py > /tmp/out &&
mv /tmp/out /usr/local/suppa/suppa.py  
RUN ln -s /usr/local/suppa/suppa.py /usr/local/bin/suppa.py  
RUN ln -s /usr/local/suppa/suppa.py /usr/local/bin/suppa  
RUN chmod +x /usr/local/bin/suppa.py  
RUN chmod +x /usr/local/bin/suppa  
RUN rm -rf v${SUPPA_VERSION}.tar.gz SUPPA-${SUPPA_VERSION}  
  
RUN pip install -I SUPPA==${SUPPA_VERSION}  
RUN pip install matplotlib  
  
# Back workdir  
WORKDIR /project  
  
# Clean cache  
RUN apt-get clean  
RUN set -x; rm -rf /var/lib/apt/lists/*  
  
# Shared mounting  
VOLUME /share  
  


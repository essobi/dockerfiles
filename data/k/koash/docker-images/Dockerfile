FROM debian:9.4  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing \  
&& apt-get install -y \  
bzip2 \  
ca-certificates \  
curl \  
git \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV MINICONDA3_VERSION 4.4.10  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh \  
&& wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA3_VERSION}-Linux-x86_64.sh
-O ~/miniconda.sh \  
&& /bin/bash ~/miniconda.sh -b -p /opt/conda \  
&& rm ~/miniconda.sh \  
&& /opt/conda/bin/conda clean -tipsy  
  
ENV TINI_VERSION 0.16.1  
ADD https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini
/usr/bin/tini  
  
RUN chmod +x /usr/bin/tini  
  
ENV PATH /opt/conda/bin:$PATH  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
  
CMD [ "/bin/bash" ]


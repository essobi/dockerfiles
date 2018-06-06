FROM debian:sid  
  
  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8  
LABEL maintainer="Dr Suman Khanal <suman81765@gmail.com>"  
  
ENV NB_USER suman  
ENV NB_UID 1000  
ENV HOME /home/${NB_USER}  
RUN adduser --disabled-password \  
\--gecos "Default user" \  
\--uid ${NB_UID} \  
${NB_USER}  
  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion nano gcc g++ make \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh && export PATH=/opt/conda/bin:$PATH \  
&& conda update -y --all \  
&& conda install -y numpy scipy seaborn \  
cython jupyter notebook scikit-learn scikit-image \  
&& conda clean -y -t \  
&& pip install asciinema  
  
ENV PATH /opt/conda/bin:$PATH  
  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
COPY . ${HOME}  
  
USER root  
RUN chown -R ${NB_UID} ${HOME}  
USER ${NB_USER}  
WORKDIR ${HOME}  
  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--
allow-root"]  


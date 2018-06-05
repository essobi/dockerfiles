FROM ubuntu:16.04  
# Install the libraries and dependencies for csiro simulator (spark).  
RUN apt-get --assume-yes update && \  
apt-get --assume-yes install wget bzip2 unzip && \  
apt-get --assume-yes clean all  
  
# Create the directory structure  
RUN mkdir -p /opt  
  
# Copy the python environment and the notebook script  
COPY environment.yml /opt  
COPY notebook.sh /opt  
  
# Install miniconda  
RUN cd /opt && \  
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh &&
\  
/bin/bash /opt/Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda3-latest-Linux-x86_64.sh  
  
RUN /opt/conda/bin/conda config --add channels conda-forge  
RUN /opt/conda/bin/conda update conda --yes  
RUN /opt/conda/bin/conda install conda-env --yes  
RUN /opt/conda/bin/conda env create -f /opt/environment.yml  
  
# Install tini  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
RUN useradd -ms /bin/bash fire  
RUN chown -R fire:fire /opt/conda  
  
USER fire  
WORKDIR /fire/  
  
ENV PATH /opt/conda/bin:$PATH  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  


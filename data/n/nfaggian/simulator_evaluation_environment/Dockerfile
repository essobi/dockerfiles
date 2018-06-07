FROM ubuntu:14.04  
# Install the libraries and dependencies for csiro simulator (spark).  
RUN apt-get --assume-yes update && \  
apt-get --assume-yes install apt-utils alien lsb git dos2unix wget bzip2 unzip
cpulimit build-essential && \  
apt-get --assume-yes clean all  
  
# Create the directory structure  
RUN mkdir -p /opt && mkdir -p /opt/spark/runtime && mkdir -p /fire/simulators  
  
# Install the libraries and dependencies for csiro simulator (spark).  
RUN wget -O /tmp/spark.zip
https://storage.googleapis.com/evaluation/ftp/spark.zip && \  
cd /tmp/ && unzip spark.zip && \  
tar xf "/tmp/Spark
Docker/spark_install/opencl_runtime_16.1_x64_ubuntu_5.2.0.10002.tgz" -C
/opt/spark/runtime && \  
mv "/tmp/Spark Docker/spark_install/silent.cfg" /opt/spark/silent.cfg && \  
mv "/tmp/Spark Docker/spark_install/csiro.au-
spark_batch_fsp-0.8.0-38884.x86_64.rpm" /opt/spark/ && \  
rm /tmp/spark.zip  
  
# Mono dependency for Phoenix simulators  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-get update && apt-get install -y mono-complete mono-devel mono-vbnc  
  
# Install the Intel OpenCL runtime for Spark  
RUN cd /opt/spark/runtime/opencl_runtime_16.1_x64_ubuntu_5.2.0.10002/ &&
./install.sh -s /opt/spark/silent.cfg  
RUN cd /opt/spark/ && alien -ikcv --bump==0 csiro.au-
spark_batch_fsp-0.8.0-38884.x86_64.rpm  
  
# Put the simulator in /fire/simulators  
RUN mv /opt/csiro.au/spark_batch_fsp /fire/simulators/spark  
  
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
  
# Install TINI  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  


FROM ubuntu:16.04  
MAINTAINER Lubomir Chorbadjiev <lubomir.chorbadjiev@gmail.com>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
ENV DEBIAN_FRONTEND=noninteractive  
  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y wget bzip2 ca-certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
# RUN apt-get install -y build-essential  
# RUN apt-get install -y gfortran  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
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
RUN apt-get install -y build-essential gfortran  
  
# RUN conda install -y pandas libgcc-ng libgfortran-ng  
RUN conda install -y pandas  
RUN conda config --add channels bioconda  
RUN conda install -y samtools bcftools biopython pysam  
  
RUN conda install -y -c conda-forge perl=5.22.0  
RUN conda install -y bowtie=1.2.1.1  
  
RUN pip install python-box termcolor PyYAML pytest pytest-asyncio #
setproctitle  
  
# RUN conda config --add channels r  
# RUN conda install -y r-essentials  
COPY conda-environment.yml /conda-environment.yml  
# RUN conda env update -f /conda-environment.yml  
# RUN apt-get update --fix-missing  
# RUN apt-get install -y r-base r-base-dev  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ed \  
less \  
locales \  
vim-tiny \  
wget \  
ca-certificates \  
apt-transport-https \  
gsfonts \  
curl \  
openssl \  
libssl-dev \  
libcurl4-openssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
## Use Debian unstable via pinning -- new style via APT::Default-Release  
RUN echo "deb https://cloud.r-project.org/bin/linux/ubuntu xenial/" >
/etc/apt/sources.list.d/cran.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
ENV R_BASE_VERSION 3.3.3  
## Now install R and littler, and create a link for littler in /usr/local/bin  
## Also set a default CRAN repo, and make sure littler knows about it too  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
littler \  
r-cran-littler \  
r-base=${R_BASE_VERSION}* \  
r-base-dev=${R_BASE_VERSION}* \  
r-recommended=${R_BASE_VERSION}* \  
&& echo 'options(repos = c(CRAN = "https://cloud.r-project.org/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site \  
&& echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \  
&& ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r \  
&& ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r
\  
&& ln -s /usr/share/doc/littler/examples/installGithub.r
/usr/local/bin/installGithub.r \  
&& ln -s /usr/share/doc/littler/examples/testInstalled.r
/usr/local/bin/testInstalled.r \  
&& install.r docopt \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget --quiet https://github.com/KrasnitzLab/sgains/archive/1.0.0RC4.tar.gz
-O ~/sgains.tar.gz && \  
mkdir /opt/sgains && \  
tar zxf ~/sgains.tar.gz -C /opt/sgains --strip-components 1  
  
ENV PATH /opt/sgains/tools:$PATH  
ENV PYTHONPATH /opt/sgains/scpipe:$PYTHONPATH  
  
COPY install.R /install.R  
RUN Rscript /install.R  
  
RUN cd /opt/sgains/scripts && Rscript setup.R  
  
VOLUME /data  
WORKDIR /data  
  
CMD ["/bin/bash"]  


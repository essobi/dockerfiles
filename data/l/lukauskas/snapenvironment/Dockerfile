FROM buildpack-deps:stretch as builder  
RUN mkdir /tmp/dapg \  
&& wget -q
http://www.inf.udec.cl/~chernand/sources/dapg/dapg_prot_complexes-v1.1.tgz -O
/tmp/dapg/dapg_prot_complexes.tgz \  
&& cd /tmp/dapg/ && tar xvf dapg_prot_complexes.tgz \  
&& cd dapg_complexes && make  
  
FROM python:3.6-stretch  
# Some ideas from https://github.com/in-silico/judge-
bot/blob/768238c1eb0875a1d7800343755d70fd432a28c2/debian/Dockerfile  
# Install R, libhdf5 and nodejs  
RUN echo "deb http://ftp.de.debian.org/debian testing contrib" >>
/etc/apt/sources.list \  
&& echo "deb http://ftp.de.debian.org/debian testing non-free" >>
/etc/apt/sources.list \  
&& echo "deb http://ftp.de.debian.org/debian testing main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \--force-yes cmake \  
fonts-humor-sans \  
git \  
graphviz \  
libblas-dev \  
libgsl-dev \  
libhdf5-dev \  
liblapack-dev \  
nodejs \  
openjdk-8-jdk \  
python-dev \  
r-base \  
ttf-freefont \  
&& apt-get -yq autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install some needed R packages  
RUN Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
source("https://bioconductor.org/biocLite.R"); biocLite("minet")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
source("http://bioconductor.org/biocLite.R"); biocLite(c("AnnotationDbi",
"impute", "GO.db", "preprocessCore", "ReactomePA", "clusterProfiler",
"meshes", "org.Hs.eg.db", "GOSemSim")); install.packages("WGCNA")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("precrec")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("ggplot2")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("ggrepel")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("corpcor")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("fdrtool")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("ppcor")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("psych")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("GPArotation")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("nFactors")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("matrixcalc")' \  
&& Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
install.packages("devtools"); library("devtools");
install_github("wyguo/RLowPC", ref="a3f741a")' \  
# Cache Reactome and GO Data so it's faster when we need to run it  
&& Rscript -e 'library(clusterProfiler); library(org.Hs.eg.db);
library(ReactomePA); enrichGO(c(4312, 8318, 10874, 55143, 55388, 991),
OrgDb=org.Hs.eg.db, ont="MF"); enrichPathway(c(4312, 8318, 10874, 55143,
55388, 991));'  
  
COPY \--from=builder /tmp/dapg/dapg_complexes/bin/* /usr/bin/  
  
ADD requirements.txt /requirements.txt  
RUN pip install \--upgrade pip \  
&& pip install \--upgrade -r /requirements.txt \  
# This needs Cython et al to be installed beforehand  
&& pip install git+https://github.com/AmazaspShumik/sklearn-
bayes.git@a9fdcb87a9e9a35e0066e8961f6f059fc01b26eb \  
# One more... cvxpy  
&& pip install cvxpy==0.4.11 \  
&& rm /requirements.txt \  
&& rm -rf ~/.cache/pip \  
&& rm -rf /src  
  
RUN /bin/bash -c 'source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv
py2 -p `which python2`' \  
&& /root/.virtualenvs/py2/bin/pip install numpy scipy pandas tables \  
&& /root/.virtualenvs/py2/bin/pip install cvxpy \  
# snap.py  
&& cd /tmp \  
&& wget
http://snap.stanford.edu/snappy/release/snap-4.0.0-4.0-centos6.5-x64-py2.6.tar.gz
-O /tmp/snappy.tar.gz \  
&& tar xvf snappy.tar.gz && cd snap-4.0.0-4.0-centos6.5-x64-py2.6 \  
&& /root/.virtualenvs/py2/bin/python setup.py install \  
# snapvx  
&& cd /tmp \  
&& wget -q http://snap.stanford.edu/snapvx/release/snapvx-0.5.tar.gz -O
snapvx-0.5.tar.gz \  
&& tar xvf snapvx-0.5.tar.gz && cd snapvx-0.5 \  
&& /root/.virtualenvs/py2/bin/python setup.py install \  
# cleanup  
&& cd \  
&& rm -rf /tmp/snap* \  
&& rm -rf ~/.cache/pip  
  
RUN mkdir -p /root/.config/matplotlib && echo 'backend : Agg' >>
/root/.config/matplotlib/matplotlibrc  


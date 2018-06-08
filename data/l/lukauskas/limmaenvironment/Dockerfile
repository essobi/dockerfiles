FROM python:3.6  
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
&& apt-get install -y libhdf5-dev \  
pandoc \  
r-base \  
&& apt-get -yq autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install some needed R packages  
RUN Rscript -e 'chooseCRANmirror(graphics=FALSE, ind=1);
source("https://bioconductor.org/biocLite.R"); biocLite(c("limma", "statmod",
"qvalue", "edgeR", "ReactomePA", "clusterProfiler", "meshes",
"org.Hs.eg.db")); install.packages("ggplot2"); install.packages("ggrepel")'  
  
ADD requirements.txt /requirements.txt  
RUN pip install --upgrade pip \  
&& pip install --upgrade -r /requirements.txt \  
&& rm /requirements.txt \  
&& rm -rf ~/.cache/pip \  
&& rm -rf /src  
  
RUN mkdir -p /root/.config/matplotlib && echo 'backend : Agg' >>
/root/.config/matplotlib/matplotlibrc  


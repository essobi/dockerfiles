# Base Image  
FROM biocontainers/biocontainers:latest  
  
# Metadata (tpp)  
LABEL base.image="biocontainers:latest"  
LABEL version="1"  
LABEL software="Diverse"  
LABEL software.version=""  
LABEL description=""  
LABEL website="Workflows for four use cases for the analysis of mass
spectrometry data"  
LABEL documentation="https://github.com/veitveit/Automatic-Workflow-
Composition"  
LABEL license="see individual software tools"  
LABEL tags="Proteomics Workflows"  
  
# Maintainer MAINTAINER Veit Schwaemmle <veits@bmb.sdu.dk>  
USER root  
WORKDIR /usr/local/  
RUN apt-get update && apt-get install -y libfindbin-libs-perl && apt-get clean
all  
RUN wget https://github.com/BioContainers/software-
archive/releases/download/TPP/tpp-5.0.zip && unzip tpp-5.0.zip  
RUN chmod a+x /usr/local/tpp/bin/*  
ENV PATH /usr/local/tpp/bin/:$PATH USER biodocker  
  
## PeptideShaker  
RUN ZIP=PeptideShaker-1.13.6.zip && wget
http://genesis.ugent.be/maven2/eu/isas/peptideshaker/PeptideShaker/1.13.6/$ZIP
-O /tmp/$ZIP && unzip /tmp/$ZIP -d /home/biodocker/bin/ && rm /tmp/$ZIP &&
bash -c 'echo -e "#!/bin/bash\njava -jar
/home/biodocker/bin/PeptideShaker-1.13.6/PeptideShaker-1.13.6.jar $@"' >
/home/biodocker/bin/PeptideShaker && chmod +x
/home/biodocker/bin/PeptideShaker  
ENV PATH /home/biodocker/bin/PeptideShaker:$PATH  
  
## SEARCHGUI  
# Maintainer MAINTAINER Felipe da Veiga Leprevost <felipe@leprevost.com.br>  
RUN ZIP=SearchGUI-3.0.2-mac_and_linux.tar.gz && wget
http://genesis.ugent.be/maven2/eu/isas/searchgui/SearchGUI/3.0.2/$ZIP -O
/tmp/$ZIP && tar xzf /tmp/$ZIP && mv SearchGUI* /home/biodocker/bin/ && rm
/tmp/$ZIP && bash -c 'echo -e "#!/bin/bash\njava -jar
/home/biodocker/bin/SearchGUI-3.0.2/SearchGUI-3.0.2.jar $@"' >
/home/biodocker/bin/SearchGUI && chmod +x /home/biodocker/bin/SearchGUI  
  
ENV PATH /home/biodocker/bin/SearchGUI:$PATH WORKDIR /data/  
  
# install protk  
RUN apt-get install -y ruby-dev libxml2-dev libgsl-dev libxml-parser-perl
libcairo2-dev && apt-get clean all  
RUN gem install protk  
  
## R environment and packages  
ENV R_BASE_VERSION 3.2.3  
ENV R_BASE_VERSION 3.3.1  
# Install R  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list && apt-key adv --keyserver keyserver.ubuntu.com --recv-
keys E084DAB9 && apt-get -qq update && apt-get upgrade -y && apt-get install
-y --no-install-recommends littler r-base-core=${R_BASE_VERSION}* r-base-
dev=${R_BASE_VERSION}* libcurl4-openssl-dev libxml2-dev libfftw3-dev git wget
&& echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site && echo
'source("/etc/R/Rprofile.site")' >> /etc/littler.r && ln -s
/usr/share/doc/littler/examples/install.r /usr/local/bin/install.r && ln -s
/usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r && ln -s
/usr/share/doc/littler/examples/installGithub.r /usr/local/bin/installGithub.r
&& ln -s /usr/share/doc/littler/examples/testInstalled.r
/usr/local/bin/testInstalled.r && install.r docopt && rm -rf
/tmp/downloaded_packages/ /tmp/*.rds && rm -rf /var/lib/apt/lists/*  
  
## Install Java  
RUN echo "deb http://security.ubuntu.com/ubuntu xenial-security main" >>
/etc/apt/sources.list && apt-key adv --keyserver keyserver.ubuntu.com --recv-
keys E084DAB9 && apt-get update && apt-get install -y openjdk-8-jdk && update-
alternatives --display java && update-alternatives --display javac && rm -rf
/var/lib/apt/lists/* && apt-get clean && R CMD javareconf  
  
## install additional R packages using R  
RUN > rscript.R && echo 'source("https://bioconductor.org/biocLite.R")' >>
rscript.R &&echo 'biocLite(ask=FALSE)' >> rscript.R &&echo
'biocLite("Biobase",ask=FALSE)' >> rscript.R &&echo
'biocLite("stringr",ask=FALSE)' >> rscript.R && echo
'biocLite("lattice",ask=FALSE)' >> rscript.R && echo
'biocLite("isobar",ask=FALSE)' >> rscript.R && echo
'biocLite("mzID",ask=FALSE)' >> rscript.R &&echo 'biocLite("XML",ask=FALSE)'
>> rscript.R && echo 'biocLite("svglite",ask=FALSE)' >> rscript.R && echo
'biocLite("venneuler",ask=FALSE)' >> rscript.R &&echo
'biocLite("matrixStats",ask=FALSE)' >> rscript.R &&echo
'biocLite("gProfileR",ask=FALSE)' >> rscript.R &&Rscript rscript.R  
  
WORKDIR /data/  
  
## Files for use cases  
COPY ./ UseCases  
# compile rt  
RUN cd /data/UseCases/Use_case_1-amino_acid_index/rt4 && gcc -o rt rt4.c -lgsl
-lgslcblas -lpepXML -LpepXMLLib && ls && cp rt /home/biodocker/bin/  
  


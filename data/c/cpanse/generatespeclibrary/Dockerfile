FROM bioconductor/release_core2  
MAINTAINER Christian Panse <cp@fgcz.ethz.ch>  
RUN apt-get update && apt-get install ed less pandoc-citeproc subversion
texlive-base texlive-extra-utils texlive-fonts-extra texlive-fonts-recommended
vim -y \  
&& mkdir -p /scratch/generatespeclibrary \  
&& echo $?  
RUN R -e "install.packages(pkgs=c('devtools', 'knitr', 'yaml'), quiet=FALSE,
repos='https://stat.ethz.ch/CRAN/', type='source');"  
RUN R -e "library(devtools);install_github('protViz/prozor', build_vignettes =
TRUE, quiet = FALSE)"  
RUN R -e "library(devtools);install_github('protViz/quantable',
build_vignettes = TRUE, quiet = FALSE)"  
RUN R -e "library(devtools);install_github('Bioconductor-mirror/specL',
build_vignettes = FALSE, quiet = FALSE)"  
RUN R -e "source('https://bioconductor.org/biocLite.R'); biocLite(c('affy',
'limma', 'qvalue'))"  
RUN R -e "library(devtools);install_github('protViz/SRMService',
build_vignettes = FALSE, quiet = FALSE)"  
VOLUME ["/scratch/generatespeclibrary/",
"/usr/local/mascot/data:/usr/local/mascot/data"]  
ADD runSpecLRmd.R /usr/local/bin/runSpecLRmd  
ADD *.py /usr/local/bin/  
ADD blob/BlibBuild /usr/local/bin/  
ADD blob/BlibFilter /usr/local/bin/  
ADD specL.Rmd /usr/local/src/  
RUN pip install cakeme \  
&& svn co https://github.com/fgcz/cakeme.git && cd cakeme.git/trunk/ && python
setup.py sdist && pip install dist/cakeme-*.tar.gz \  
&& mkdir -p /scratch/generatespeclibrary \  
&& chmod 755 /usr/local/bin/BlibBuild /usr/local/bin/BlibFilter \  
&& echo $?  
VOLUME ["/scratch/generatespeclibrary/",
"/usr/local/mascot/data:/usr/local/mascot/data"]  
WORKDIR /scratch/generatespeclibrary  
  


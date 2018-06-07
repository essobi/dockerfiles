FROM bioconductor/release_core  
  
  
#  
# Install EMOTE package and its dependencies  
#  
RUN cd /tmp;git clone https://github.com/pradosj/EMOTE.git;  
RUN Rscript -e 'install.packages(c("roxygen2","VGAM")); \  
BiocInstaller::biocLite(c("ShortRead","Rbowtie")); \  
roxygen2::roxygenize("/tmp/EMOTE/EMOTE/"); \  
install.packages("/tmp/EMOTE/EMOTE",repos=NULL) \  
'  
  
VOLUME ["/export/"]  
  


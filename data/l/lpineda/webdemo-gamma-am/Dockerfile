FROM ubuntu:14.04  
MAINTAINER Leandro Pineda <leandropineda.lp@gmail.com>  
  
ENV bioconductor_url="http://bioconductor.org/packages/3.0/bioc/src/contrib/"  
ENV
bioconductor_data_url="http://www.bioconductor.org/packages/3.0/data/annotation/src/contrib/"  
#ENV http_proxy="http://proxy.unl.edu.ar:8000"  
RUN echo deb http://cran.r-project.org/bin/linux/ubuntu trusty/ >
/etc/apt/sources.list.d/r.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9  
RUN gpg -a --export E084DAB9 | sudo apt-key add -  
  
# Install base packages  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get install -y \  
r-base \  
r-recommended \  
r-base-dev \  
imagemagick \  
curl \  
libcurl4-gnutls-dev && \  
apt-get clean && apt-get autoclean  
  
##Bioconductor guille  
RUN > Bioc.R  
  
RUN echo 'source("https://bioconductor.org/biocLite.R")' >> Bioc.R  
RUN echo 'biocLite("org.At.tair.db")' >> Bioc.R  
RUN echo 'biocLite("org.Sc.sgd.db")' >> Bioc.R  
RUN echo 'biocLite("org.Gg.eg.db")' >> Bioc.R  
RUN echo 'biocLite("org.Bt.eg.db")' >> Bioc.R  
RUN echo 'biocLite("org.Mmu.eg.db")' >> Bioc.R  
RUN echo 'biocLite("ath1121501.db")' >> Bioc.R  
RUN echo 'biocLite("yeast2.db")' >> Bioc.R  
RUN echo 'biocLite("chicken.db")' >> Bioc.R  
RUN echo 'biocLite("bovine.db")' >> Bioc.R  
RUN echo 'biocLite("moe430a.db")' >> Bioc.R  
RUN echo 'biocLite("GOSemSim")' >> Bioc.R  
  
RUN Rscript Bioc.R  
  
RUN rm Bioc.R  
  
RUN > CRAN.R  
RUN echo 'install.packages("R2HTML", repos="http://cran.r-project.org")' >>
CRAN.R  
RUN echo 'install.packages("gProfileR", repos="http://cran.r-project.org")' >>
CRAN.R  
RUN echo 'install.packages("cluster", repos="http://cran.r-project.org")' >>
CRAN.R  
RUN echo 'install.packages("clValid", repos="http://cran.r-project.org")' >>
CRAN.R  
  
RUN Rscript CRAN.R  
RUN rm CRAN.R  
  
# Create a new user "developer".  
# It will get access to the X11 session in the host computer  
ENV uid=1000  
ENV gid=${uid}  
  
COPY create_user.sh /  
  
CMD /create_user.sh && sudo -H -u developer /bin/bash  
  


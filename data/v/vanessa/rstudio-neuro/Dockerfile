FROM rocker/rstudio  
  
##############################################  
# docker build -t vanessa/rstudio-neuro .  
# docker run -p 8787:8787 vanessa/rstudio-neuro  
# Visit localhost:8787 in your browser  
# log in: username:password as rstudio:rstudio  
##############################################  
# git2r  
RUN apt-get update && apt-get install -y zlib1g-dev  
  
ADD hello.txt /  
  
##############################################  
# Dependency Hell  
##############################################  
RUN Rscript -e "install.packages('callr')"  
RUN Rscript -e "install.packages('cli')"  
RUN Rscript -e "install.packages('digest')"  
RUN Rscript -e "install.packages('git2r')"  
RUN Rscript -e "install.packages('httr')"  
RUN Rscript -e "install.packages('jsonlite')"  
RUN Rscript -e "install.packages('memoise')"  
RUN Rscript -e "install.packages('rcmdcheck')"  
RUN Rscript -e "install.packages('rstudioapi')"  
RUN Rscript -e "install.packages('sessioninfo')"  
RUN Rscript -e "install.packages('usethis')"  
RUN Rscript -e "install.packages('whisker')"  
RUN Rscript -e "install.packages('withr')"  
RUN Rscript -e "install.packages('knitr')"  
RUN Rscript -e "install.packages('desc')"  
RUN Rscript -e "install.packages('rprojroot')"  
  
RUN git clone https://github.com/r-lib/pkgbuild.git && cd pkgbuild && R CMD
build . && R CMD INSTALL --build pkg*tar.gz  
RUN git clone https://github.com/r-lib/pkgload.git && cd pkgload && R CMD
build . && R CMD INSTALL --build pkg*tar.gz  
  
##############################################  
# Joke's List  
##############################################  
RUN git clone https://github.com/hadley/devtools.git && cd devtools && R CMD
build . && R CMD INSTALL --build devtools*.tar.gz  
  
RUN wget https://www.dropbox.com/s/vy2exrrzjia9u85/validating_fmri.zip?dl=0#
-O /validating_fmri.zip && cd / && unzip /validating_fmri.zip  
RUN Rscript -e "install.packages('R.utils')"  
RUN Rscript -e "install.packages('matrixStats')"  
RUN Rscript -e "install.packages('abind')"  
RUN Rscript -e "install.packages('bitops')"  
RUN Rscript -e "source('https://neuroconductor.org/neurocLite.R');
neuro_install('neurobase', release = 'stable')"  
RUN Rscript -e "source('https://bioconductor.org/biocLite.R');
biocLite('graph')"  
RUN Rscript -e "source('https://bioconductor.org/biocLite.R');
biocLite('RBGL')"  
RUN Rscript -e "source('https://bioconductor.org/biocLite.R');
biocLite('pcor')"  
RUN Rscript -e "install.packages('RColorBrewer')"  
RUN Rscript -e "install.packages('scales')"  
RUN Rscript -e "install.packages('lattice')"  
RUN Rscript -e "install.packages('Rcmdr')"  
RUN Rscript -e "install.packages('neuRosim')"  
RUN mv /data /home/rstudio/data  
  
# Hallo!  
RUN cat /hello.txt  


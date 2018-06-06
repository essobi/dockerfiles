# don't acutally need r-devel for R, just all the dependencies.  
FROM jackwasey/clang-3.8  
WORKDIR /usr/local/src  
  
# for COPY to work (without duplicating across a bunch of folders) the build
context should be the parent directory  
COPY get-r.sh .  
RUN ./get-r.sh  
  
ARG JW_DOCKER_BUILD_DIR=.  
COPY ${JW_DOCKER_BUILD_DIR}/config.site R-devel/config.site  
  
RUN cd R-devel \  
&& ./configure \  
\--enable-R-shlib \  
\--without-blas \  
\--without-lapack \  
\--with-readline \  
\--without-recommended-packages \  
\--program-suffix=devsan \  
&& make -j4 \  
&& make install \  
&& make clean  
  
## Set Renviron to get libs from base R install  
RUN echo "R_LIBS=\${R_LIBS-'/usr/local/lib/R/site-
library:/usr/local/lib/R/library:/usr/lib/R/library'}" >>
/usr/local/lib/R/etc/Renviron  
  
## Set default CRAN repo  
RUN echo 'options("repos"="https://cloud.r-project.org")' >>
/usr/local/lib/R/etc/Rprofile.site  
  
# R doesn't actually run at all without this (can be considered a test of
whether the sanitizers were actually compiled in correctly!)  
ENV ASAN_OPTIONS
'alloc_dealloc_mismatch=0:detect_leaks=0:detect_odr_violation=0'  
# this docker image is focussed on testing icd, so install stuff now:  
RUN Rscript -e "install.packages(c('codetools', 'testthat', 'Rcpp',
'RColorBrewer', 'dichromat', 'munsell', 'checkmate', 'scales', 'proto',
'caTools', 'evaluate', 'knitr', 'xtable', 'rmarkdown', 'fastmatch', 'RODBC',
'roxygen2', 'xml2'), INSTALL_opts = '--no-byte-compile')"  


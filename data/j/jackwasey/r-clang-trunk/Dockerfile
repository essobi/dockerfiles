# don't acutally need r-devel for R, just all the dependencies.  
FROM jackwasey/clang-trunk  
MAINTAINER "Jack Wasey" jack@jackwasey.com  
WORKDIR /usr/local/src  
  
# for COPY to work (without duplicating across a bunch of folders) the build
context should be the parent directory  
COPY bin/get-r.sh .  
RUN ./get-r.sh svn  
# CRAN/Ripley use a particular SVN version of R. Many R versions don't even
compile with UBSAN and/or ASAN.  
# RUN cd R-devel && svn up -r71700 && cd ..  
# the CLANG-RT/ASAN library folder name changes with each release:  
RUN CLANGVER=$(clang --version | head -1 | awk '{print $3;}')  
  
RUN cd R-devel \  
&& R_PAPERSIZE=letter \  
R_BATCHSAVE="--no-save --no-restore" \  
R_BROWSER=xdg-open \  
PAGER=/usr/bin/pager \  
PERL=/usr/bin/perl \  
R_UNZIPCMD=/usr/bin/unzip \  
R_ZIPCMD=/usr/bin/zip \  
R_PRINTCMD=/usr/bin/lpr \  
LIBnn=lib \  
AWK=/usr/bin/awk \  
CC="clang -fsanitize=address,undefined -fno-sanitize=float-divide-by-zero
-fno-omit-frame-pointer" \  
CXX="clang++ -fsanitize=address,undefined -fno-sanitize=float-divide-by-zero
-stdlib=libc++ -fno-omit-frame-pointer -I/usr/local/include/c++/v1
-I/usr/local/include" \  
FFLAGS="-g -O2 -march=native" \  
FCFLAGS="-g -O2 -march=native" \  
CFLAGS="-pipe -Wall -Wextra -pedantic -Wno-unused-parameter -g -O0
-march=native" \  
CXXFLAGS="-pipe -Wall -Wextra -pedantic -Wno-unused-parameter -g -O0
-march=native" \  
MAIN_LD="clang++ -stdlib=libc++ -fsanitize=address,undefined" \  
LDFLAGS="-L/usr/local/lib/clang/$CLANGVER/lib/linux -L/usr/local/lib -lc++abi"
\  
./configure \  
\--enable-R-shlib \  
\--without-blas \  
\--without-lapack \  
\--with-readline \  
\--without-recommended-packages \  
\--program-suffix=dev \  
\--disable-openmp \  
&& make -j8 \  
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
# but rocker/r-devel-ubsan-clang does work without this  
# see: http://www.stats.ox.ac.uk/pub/bdr/memtests/README.txt  
ENV ASAN_OPTIONS
'alloc_dealloc_mismatch=0:detect_leaks=0:detect_odr_violation=0'  
## Create R-devel symlinks  
RUN cd /usr/local/bin \  
&& mv R Rdevel \  
&& mv Rscript Rscriptdevel \  
&& mv RD RDold \  
&& mv RDscript RDscriptold \  
&& ln -s Rdevel RD \  
&& ln -s Rscriptdevel RDscript  


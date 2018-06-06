## Emacs, make this -*- mode: sh; -*-  
### r-coverage based on R-3.0.2  
# inspired a lot by https://github.com/rocker-org  
FROM debian:7.6  
MAINTAINER "Karl Forner" karl.forner@quartzbio.com  
  
## Remain current  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y  
  
RUN apt-get install -y --no-install-recommends \  
bash-completion \  
bison \  
debhelper \  
default-jdk \  
g++ \  
gcc \  
gfortran \  
groff-base \  
libblas-dev \  
libbz2-dev \  
libcairo2-dev \  
libjpeg-dev \  
liblapack-dev \  
liblzma-dev \  
libncurses5-dev \  
libpango1.0-dev \  
libpcre3-dev \  
libpng-dev \  
libreadline-dev \  
libtiff5-dev \  
libx11-dev \  
libxt-dev \  
mpack \  
subversion \  
tcl8.5-dev \  
texinfo \  
texlive-base \  
texlive-extra-utils \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-latex-recommended \  
tk8.5-dev \  
x11proto-core-dev \  
xauth \  
xdg-utils \  
xfonts-base \  
xvfb \  
zlib1g-dev  
  
RUN apt-get install -y \  
curl \  
less \  
libcurl4-openssl-dev \  
libxml2-dev \  
littler \  
locales \  
nano \  
sudo \  
vim-tiny \  
wget \  
&& rm -rf /tmp/downloaded_packages/  
  
## Configure default locale  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# download and install R-3.0.2  
WORKDIR /tmp  
ENV RVERSION 3.0.2  
RUN wget -q http://cran.r-project.org/src/base/R-3/R-$RVERSION.tar.gz  
  
ENV RDIR /usr/local/R-$RVERSION  
RUN echo 'Normal installation' && \  
tar zxf R-$RVERSION.tar.gz && \  
cd R-$RVERSION && \  
./configure --prefix $RDIR \--disable-R-shlib --enable-memory-profiling
--with-readline && \  
make -j 4 && \  
make install && \  
cd .. && \  
rm -rf R-$RVERSION  
  
### patch R for code coverage  
ENV RCOVDIR ${RDIR}_cov  
COPY r302_coverage.patch /tmp/  
RUN echo 'installing patched version' && \  
tar zxf R-$RVERSION.tar.gz && \  
patch -p0 < r302_coverage.patch && \  
cd R-$RVERSION && \  
./configure --prefix $RCOVDIR \--enable-R-shlib --enable-memory-profiling
--with-readline && \  
make -j 4 && \  
make install  
  
### use a common library dir for both R installations: /usr/local/lib/R/site-
library  
### and set a CRAN repo  
RUN for dir in $RDIR $RCOVDIR; do \  
echo "R_LIBS_SITE=\${R_LIBS_SITE-'/usr/local/lib/R/site-library'}" >
$dir/lib/R/etc/Renviron.site; \  
echo 'options(repos = list(CRAN = "http://stat.ethz.ch/CRAN/"))' >>
$dir/lib/R/etc/Rprofile.site; \  
done  
  
## making links to binaries in /usr/local/bin  
RUN ln -s $RDIR/bin/R /usr/local/bin/ && \  
ln -s $RDIR/bin/Rscript /usr/local/bin/ && \  
ln -s $RCOVDIR/bin/R /usr/local/bin/Rcov && \  
ln -s $RCOVDIR/bin/Rscript /usr/local/bin/Rscript_cov  
  
# update all the packages that need to be reinstalled.  
RUN Rscript -e 'update.packages(checkBuilt = TRUE, ask = FALSE)'  
  
## install essential packages  
RUN Rscript -e 'install.packages("devtools")'  
  
## Set a default user. Available via runtime flag `--user docker`  
RUN useradd -g staff -m docker  
  
WORKDIR /home/docker  
COPY bashrc /home/docker/.bashrc  
COPY test.R /home/docker/  
COPY test2.R /home/docker/  
  
# for testing  
ENV PKGTESTTHAT testthat_0.7.1.tar.gz  
RUN wget http://cran.r-project.org/src/contrib/Archive/testthat/$PKGTESTTHAT
&& \  
R CMD INSTALL $PKGTESTTHAT && \  
tar zxf $PKGTESTTHAT && \  
rm $PKGTESTTHAT  
  
USER docker  
CMD Rcov  


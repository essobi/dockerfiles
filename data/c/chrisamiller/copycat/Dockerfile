FROM ubuntu:xenial  
MAINTAINER Chris Miller <c.a.miller@wustl.edu>  
  
LABEL Image for the R copycat package  
  
#some basic tools  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
build-essential \  
bzip2 \  
curl \  
g++ \  
libcurl4-openssl-dev \  
libpng-dev \  
librsvg2-bin \  
libssl-dev \  
libxml2-dev \  
lsof \  
make \  
man \  
ncurses-dev \  
openssh-client \  
pkg-config \  
unzip \  
wget \  
zip \  
zlib1g-dev  
  
############################  
# R, bioconductor packages #  
# from https://raw.githubusercontent.com/rocker-org/rocker-
versioned/master/r-ver/3.4.0/Dockerfile  
# we'll pin to 3.4.0 for now  
  
ARG R_VERSION  
ARG BUILD_DATE  
ENV BUILD_DATE 2017-06-20  
ENV R_VERSION=${R_VERSION:-3.4.0}  
RUN apt-get update && apt-get install -y --no-install-recommends locales && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
LC_ALL=en_US.UTF-8 && \  
LANG=en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8 && \  
TERM=xterm && \  
apt-get install -y --no-install-recommends \  
bash-completion \  
ca-certificates \  
file \  
fonts-texgyre \  
g++ \  
gfortran \  
gsfonts \  
libbz2-1.0 \  
libcurl3 \  
libicu55 \  
libjpeg-turbo8 \  
libopenblas-dev \  
libpangocairo-1.0-0 \  
libpcre3 \  
libpng12-0 \  
libtiff5 \  
liblzma5 \  
locales \  
zlib1g \  
libbz2-dev \  
libcairo2-dev \  
libcurl4-openssl-dev \  
libpango1.0-dev \  
libjpeg-dev \  
libicu-dev \  
libpcre3-dev \  
libpng-dev \  
libreadline-dev \  
libtiff5-dev \  
liblzma-dev \  
libx11-dev \  
libxt-dev \  
perl \  
tcl8.5-dev \  
tk8.5-dev \  
texinfo \  
texlive-extra-utils \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-latex-recommended \  
x11proto-core-dev \  
xauth \  
xfonts-base \  
xvfb \  
zlib1g-dev && \  
cd /tmp/ && \  
## Download source code  
curl -O https://cran.r-project.org/src/base/R-3/R-${R_VERSION}.tar.gz && \  
## Extract source code  
tar -xf R-${R_VERSION}.tar.gz && \  
cd R-${R_VERSION} && \  
## Set compiler flags  
R_PAPERSIZE=letter && \  
R_BATCHSAVE="--no-save --no-restore" && \  
R_BROWSER=xdg-open && \  
PAGER=/usr/bin/pager && \  
PERL=/usr/bin/perl && \  
R_UNZIPCMD=/usr/bin/unzip && \  
R_ZIPCMD=/usr/bin/zip && \  
R_PRINTCMD=/usr/bin/lpr && \  
LIBnn=lib && \  
AWK=/usr/bin/awk && \  
CFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security
-Wdate-time -D_FORTIFY_SOURCE=2 -g" && \  
CXXFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security
-Wdate-time -D_FORTIFY_SOURCE=2 -g" && \  
## Configure options  
./configure --enable-R-shlib \  
\--enable-memory-profiling \  
\--with-readline \  
\--with-blas="-lopenblas" \  
\--disable-nls \  
\--without-recommended-packages && \  
## Build and install  
make && \  
make install && \  
## Add a default CRAN mirror  
echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'),
download.file.method = 'libcurl')" >> /usr/local/lib/R/etc/Rprofile.site && \  
## Add a library directory (for user-installed packages)  
mkdir -p /usr/local/lib/R/site-library && \  
chown root:staff /usr/local/lib/R/site-library && \  
chmod g+wx /usr/local/lib/R/site-library && \  
## Fix library path  
echo "R_LIBS_USER='/usr/local/lib/R/site-library'" >>
/usr/local/lib/R/etc/Renviron && \  
echo "R_LIBS=\${R_LIBS-'/usr/local/lib/R/site-
library:/usr/local/lib/R/library:/usr/lib/R/library'}" >>
/usr/local/lib/R/etc/Renviron && \  
## install packages from date-locked MRAN snapshot of CRAN  
[ -z "$BUILD_DATE" ] && BUILD_DATE=$(TZ="America/Los_Angeles" date -I) || true
&& \  
MRAN=https://mran.microsoft.com/snapshot/${BUILD_DATE} && \  
echo MRAN=$MRAN >> /etc/environment && \  
export MRAN=$MRAN && \  
echo "options(repos = c(CRAN='$MRAN'), download.file.method = 'libcurl')" >>
/usr/local/lib/R/etc/Rprofile.site && \  
## Use littler installation scripts  
Rscript -e "install.packages(c('littler', 'docopt'), repo = '$MRAN')" && \  
ln -s /usr/local/lib/R/site-library/littler/examples/install2.r
/usr/local/bin/install2.r && \  
ln -s /usr/local/lib/R/site-library/littler/examples/installGithub.r
/usr/local/bin/installGithub.r && \  
ln -s /usr/local/lib/R/site-library/littler/bin/r /usr/local/bin/r  
## install r packages, bioconductor, etc ##  
ADD rpackages.R /tmp/  
RUN R -f /tmp/rpackages.R && \  
cd /tmp/ && \  
wget https://github.com/chrisamiller/copyCat/archive/v1.6.12.tar.gz && \  
mv v1.6.12.tar.gz copyCat_1.6.12.tar.gz && \  
R CMD INSTALL copyCat_1.6.12.tar.gz && \  
cd && rm -rf /tmp/copyCat_1.6.12.tar.gz  
  
## Clean up  
RUN cd / && \  
rm -rf /tmp/* && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
  
# needed for MGI data mounts  
RUN apt-get update && apt-get install -y libnss-sss && apt-get clean all  
  
#set timezone to CDT  
#LSF: Java bug that need to change the /etc/timezone.  
#/etc/localtime is not enough.  
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime && \  
echo "America/Chicago" > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata  
  
#UUID is needed to be set for some applications  
RUN apt-get update && apt-get install -y dbus && apt-get clean all  
RUN dbus-uuidgen >/etc/machine-id  


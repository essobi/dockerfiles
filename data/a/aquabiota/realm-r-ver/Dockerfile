# -*- mode: ruby -*-  
# vi: set ft=ruby :  
FROM debian:stretch  
# original source: https://github.com/rocker-org/rocker-
versioned/blob/master/r-ver/devel/Dockerfile  
LABEL org.label-schema.license="GPL-2.0" \  
maintainer="Aquabiota Solutions AB <mapcloud@aquabiota.se>"  
  
ARG R_VERSION  
ARG BUILD_DATE  
  
RUN apt-get update && apt-get install -y locales sudo && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
ENV R_VERSION=${R_VERSION:-3.4.1} \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
TERM=xterm \  
PATH=/usr/lib/ccache:$PATH \  
NB_USER=aqua \  
HOME_AQUA=/home/$NB_USER \  
AQUABIOTA_USER=user.docker  
# NB_UID=1000 \  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
bash-completion \  
ca-certificates \  
ccache \  
file \  
fonts-texgyre \  
g++ \  
gfortran \  
gsfonts \  
libbz2-1.0 \  
libcurl3 \  
libicu57 \  
libjpeg62-turbo \  
libopenblas-dev \  
libpangocairo-1.0-0 \  
libpcre3 \  
libpng16-16 \  
libreadline7 \  
libtiff5 \  
liblzma5 \  
locales \  
make \  
unzip \  
zip \  
zlib1g \  
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=$LANG LC_ALL=$LC_ALL LANGUAGE=$LANGUAGE \  
&& BUILDDEPS="curl \  
default-jdk \  
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
subversion tcl8.6-dev \  
tk8.6-dev \  
texinfo \  
texlive-extra-utils \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-latex-recommended \  
x11proto-core-dev \  
xauth \  
xfonts-base \  
xvfb \  
zlib1g-dev" \  
&& apt-get install -y --no-install-recommends $BUILDDEPS \  
&& cd tmp/ \  
&& svn co https://svn.r-project.org/R/trunk R-devel \  
&& cd R-devel \  
&& R_PAPERSIZE=A4 \  
R_BATCHSAVE="--no-save --no-restore" \  
R_BROWSER=xdg-open \  
PAGER=/usr/bin/pager \  
PERL=/usr/bin/perl \  
R_UNZIPCMD=/usr/bin/unzip \  
R_ZIPCMD=/usr/bin/zip \  
R_PRINTCMD=/usr/bin/lpr \  
LIBnn=lib \  
AWK=/usr/bin/awk \  
CFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security
-Wdate-time -D_FORTIFY_SOURCE=2 -g" \  
CXXFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security
-Wdate-time -D_FORTIFY_SOURCE=2 -g" \  
./configure --enable-R-shlib \  
\--enable-memory-profiling \  
\--with-readline \  
\--with-blas="-lopenblas" \  
\--disable-nls \  
\--without-recommended-packages \  
&& make \  
&& make install \  
&& echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'),
download.file.method = 'libcurl')" >> /usr/local/lib/R/etc/Rprofile.site \  
&& mkdir -p /usr/local/lib/R/site-library \  
&& chown root:staff /usr/local/lib/R/site-library \  
&& chmod g+wx /usr/local/lib/R/site-library \  
&& echo "R_LIBS_USER='/usr/local/lib/R/site-library'" >>
/usr/local/lib/R/etc/Renviron \  
&& echo "R_LIBS=\${R_LIBS-'/usr/local/lib/R/site-
library:/usr/local/lib/R/library:/usr/lib/R/library'}" >>
/usr/local/lib/R/etc/Renviron \  
&& [ -z "$BUILD_DATE" ] && BUILD_DATE=$(TZ="Europe/Stockholm" date -I) || true
\  
&& MRAN=https://mran.microsoft.com/snapshot/${BUILD_DATE} \  
&& echo MRAN=$MRAN >> /etc/environment \  
&& export MRAN=$MRAN \  
&& Rscript -e "install.packages(c('littler', 'docopt'), repo = '$MRAN')" \  
&& ln -s /usr/local/lib/R/site-library/littler/examples/install2.r
/usr/local/bin/install2.r \  
&& ln -s /usr/local/lib/R/site-library/littler/examples/installGithub.r
/usr/local/bin/installGithub.r \  
&& ln -s /usr/local/lib/R/site-library/littler/bin/r /usr/local/bin/r \  
&& curl -O /usr/local/bin/install2.r
https://github.com/eddelbuettel/littler/raw/master/inst/examples/install2.r \  
&& chmod +x /usr/local/bin/install2.r \  
&& cd / \  
&& rm -rf /tmp/* \  
&& apt-get remove --purge -y $BUILDDEPS \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& ccache -C  
CMD ["R"]  


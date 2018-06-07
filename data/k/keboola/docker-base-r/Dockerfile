FROM debian:8  
# Package version to install  
ENV R_BASE_VERSION 3.3.2  
  
WORKDIR /tmp  
  
# Install packages  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
ed \  
fonts-texgyre \  
g++ \  
gcc \  
gdb \  
gfortran \  
git \  
libgsl0-dev \  
default-jdk \  
libbz2-dev \  
libcairo2-dev \  
libcurl4-openssl-dev \  
libjpeg-dev \  
libpng-dev \  
libpango1.0-dev \  
libreadline-dev \  
libssl-dev \  
libtiff5-dev \  
libx11-dev \  
libxt-dev \  
less \  
locales \  
make \  
openssl \  
texinfo \  
texlive-base \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-recommended \  
x11proto-core-dev \  
xfonts-base \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Build R  
RUN mkdir /usr/local/src/R \  
&& cd /usr/local/src/R \  
&& curl -OfsS
https://cran.r-project.org/src/base/R-3/R-${R_BASE_VERSION}.tar.gz \  
&& tar xzvf R-${R_BASE_VERSION}.tar.gz \  
&& cd R-${R_BASE_VERSION} \  
&& ./configure --with-x=yes --enable-R-shlib \  
&& make \  
&& make check  
  
ENV R_HOME=/usr/local/src/R/R-${R_BASE_VERSION}  
ENV PATH=/usr/local/src/R:$PATH  
  
# Cleanup, Setup  
RUN rm -rf /usr/local/src/R/R-${R_BASE_VERSION}/src \  
&& rm -f R /usr/local/src/R/Rscript R-${R_BASE_VERSION}.tar.gz \  
&& ln -s /usr/local/src/R/R-${R_BASE_VERSION}/bin/R /usr/local/src/R/R \  
&& ln -s /usr/local/src/R/R-${R_BASE_VERSION}/bin/Rscript
/usr/local/src/R/Rscript \  
&& mkdir /usr/share/doc/R-${R_BASE_VERSION} \  
&& echo 'options(repos = c(CRAN = "https://cran.r-project.org",
"https://cran.rstudio.com/", "https://mirrors.nics.utk.edu/cran/",
"https://cran.mtu.edu/"))' >> ${R_HOME}/etc/Rprofile.site \  
&& echo 'options(download.file.method = "libcurl")' >>
${R_HOME}/etc/Rprofile.site  


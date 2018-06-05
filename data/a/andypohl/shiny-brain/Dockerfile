FROM ubuntu:xenial  
  
MAINTAINER "Andy Pohl" andy.pohl@wisc.edu  
  
ENV R_BASE_VERSION 3.3.2  
  
RUN apt-get update \  
&& apt-get install -y \  
libvtk5.10 \  
gnupg \  
apt-transport-https \  
wget \  
&& echo "deb https://cran.rstudio.com/bin/linux/ubuntu xenial/" >
/etc/apt/sources.list.d/cran.sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 \  
&& apt-get update \  
&& R_BASE_VERSION=3.3.2 \  
&& apt-get install -y \  
littler \  
r-cran-littler \  
r-base=${R_BASE_VERSION}* \  
r-base-dev=${R_BASE_VERSION}* \  
&& wget -O- http://neuro.debian.net/lists/xenial.de-m.full | tee
/etc/apt/sources.list.d/neurodebian.sources.list \  
&& apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9
\  
&& apt-get update \  
&& apt-get install -y \  
freeglut3 \  
freeglut3-dev \  
fsl-complete \  
&& echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site \  
&& echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \  
&& ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r \  
&& ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r
\  
&& ln -s /usr/share/doc/littler/examples/installGithub.r
/usr/local/bin/installGithub.r \  
&& ln -s /usr/share/doc/littler/examples/testInstalled.r
/usr/local/bin/testInstalled.r \  
&& install.r docopt \  
&& apt-get install -y \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev \  
&& cd /root \  
&& wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" \  
&& SHINY_VERSION=$(cat version.txt) \  
&& wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$SHINY_VERSION-amd64.deb" -O ss-
latest.deb \  
&& gdebi -n ss-latest.deb \  
&& rm -f version.txt ss-latest.deb \  
&& Rscript -e "install.packages(c('shiny','rmarkdown'))" \  
&& Rscript -e
"install.packages(c('shinydashboard','rgl','misc3d','oro.nifti','brainR','fslr'))"
\  
&& cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ \  
&& wget https://raw.githubusercontent.com/rocker-org/shiny/master/shiny-
server.sh \  
&& chmod +x shiny-server.sh \  
&& mv shiny-server.sh /usr/bin \  
&& echo ". /etc/fsl/5.0/fsl.sh" >> /root/.bashrc \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV FSLDIR=/usr/lib/fsl/5.0  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
ENV PATH=$PATH:$FSLDIR  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$FSLDIR  
  
EXPOSE 3838  
  
CMD ["/usr/bin/shiny-server.sh"]  


FROM spencerlyon2/jupyter-julia  
  
MAINTAINER Spencer Lyon <spencerlyon2@gmail.com>  
  
# R installation  
RUN add-apt-repository "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/"
&& \  
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \  
gpg -a --export E084DAB9 | apt-key add - && \  
apt-get update && \  
apt-get install -y r-base r-base-dev r-cran-rcurl libreadline-dev && \  
apt-get install -y r-cran-getopt littler && \  
apt-get install libcurl4-openssl-dev && \  
echo 'options(repos=structure(c(CRAN="http://cran.rstudio.com")))' >>
/usr/lib/R/etc/Rprofile.site && \  
echo "PKG_CXXFLAGS = '-std=c++11'" >> /usr/lib/R/etc/Makeconf.site && \  
echo "R_LIBS=\${R_LIBS-'/usr/local/lib/R/site-
library:/usr/local/lib/R/library:/usr/lib/R/library'}" >>
/usr/lib/R/etc/Renviron && \  
ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r &&
\  
ln -s /usr/share/doc/littler/examples/installGithub.r
/usr/local/bin/installGithub.r && \  
ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r && \  
echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r && \  
install.r docopt && \  
rm -rf /tmp/downloaded_packages/ /tmp/*.rds /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
#install R packages and set up IRkernel  
RUN install2.r --error \  
devtools \  
dplyr \  
ggplot2 \  
httr \  
knitr \  
packrat \  
reshape2 \  
rmarkdown \  
tidyr \  
data.table \  
nlme \  
RCurl && \  
installGithub.r \  
armstrtw/rzmq \  
takluyver/IRdisplay \  
takluyver/IRkernel && \  
echo "IRkernel::installspec()" | R --no-save  


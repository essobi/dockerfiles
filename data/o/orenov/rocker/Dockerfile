## Start with the official rocker image providing 'base R'  
FROM r-base:latest  
## This handle reaches Carl and Dirk  
MAINTAINER "Carl Boettiger and Dirk Eddelbuettel" rocker-
maintainers@eddelbuettel.com  
  
## Add RStudio binaries to PATH  
ENV PATH /usr/lib/rstudio-server/bin/:$PATH  
  
  
RUN sh -c "echo 'deb http://ftp.de.debian.org/debian jessie main' >>
/etc/apt/sources.list"  
  
## Download and install RStudio server & dependencies  
## Attempts to get detect latest version, otherwise falls back to version
given in $VER  
## Symlink pandoc, pandoc-citeproc so they are available system-wide  
RUN rm -rf /var/lib/apt/lists/ \  
&& apt-get update \  
&& apt-get install -t stable libssl1.0.0 \  
&& apt-get install -y -t unstable --no-install-recommends \  
ca-certificates \  
file \  
git \  
libapparmor1 \  
libedit2 \  
libcurl4-openssl-dev \  
libssl-dev \  
psmisc \  
python-setuptools \  
python \  
python-pip \  
sudo \  
&& VER=$(wget --no-check-certificate -qO- https://s3.amazonaws.com/rstudio-
server/current.ver) \  
&& wget -q http://download2.rstudio.org/rstudio-server-${VER}-amd64.deb \  
&& dpkg -i rstudio-server-${VER}-amd64.deb \  
&& rm rstudio-server-*-amd64.deb \  
&& ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc /usr/local/bin \  
&& ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc-citeproc /usr/local/bin \  
&& wget https://github.com/jgm/pandoc-templates/archive/1.15.0.6.tar.gz \  
&& mkdir -p /opt/pandoc/templates && tar zxf 1.15.0.6.tar.gz \  
&& cp -r pandoc-templates*/* /opt/pandoc/templates && rm -rf pandoc-templates*
\  
&& mkdir /root/.pandoc && ln -s /opt/pandoc/templates /root/.pandoc/templates
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
#RUN apt-get build-dep build-essential  
## Ensure that if both httr and httpuv are installed downstream, oauth 2.0
flows still work correctly.  
RUN echo '\n\  
\n# Configure httr to perform out-of-band authentication if HTTR_LOCALHOST \  
\n# is not set since a redirect to localhost may not work depending upon \  
\n# where this Docker container is running. \  
\nif(is.na(Sys.getenv("HTTR_LOCALHOST", unset=NA))) { \  
\n options(httr_oob_default = TRUE) \  
\n}' >> /etc/R/Rprofile.site  
  
RUN echo "PATH=$PATH" >> /etc/R/Renviron.site  
  
## A default user system configuration. For historical reasons,  
## we want user to be 'rstudio', but it is 'docker' in r-base  
RUN usermod -l rstudio docker \  
&& usermod -m -d /home/rstudio rstudio \  
&& groupmod -n rstudio docker \  
&& echo '"\e[5~": history-search-backward' >> /etc/inputrc \  
&& echo '"\e[6~": history-search-backward' >> /etc/inputrc \  
&& echo "rstudio:rstudio" | chpasswd  
  
## Use s6  
RUN wget -P /tmp/ https://github.com/just-
containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz \  
&& tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
COPY userconf.sh /etc/cont-init.d/conf  
COPY run.sh /etc/services.d/rstudio/run  
  
EXPOSE 8787  
RUN pip install setuptools  
RUN pip install awscli  
  
RUN apt-get update  
RUN apt-get install -y libpq-dev  
RUN apt-get install htop  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e 'install.packages("devtools",
repos="http://cran.us.r-project.org")'  
RUN Rscript -e 'install.packages("RPostgreSQL",
repos="http://cran.us.r-project.org")'  
## Expose a default volume for Kitematic  
VOLUME /home/rstudio  
  
CMD ["/init"]  


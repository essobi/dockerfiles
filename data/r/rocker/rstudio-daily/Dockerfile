FROM rocker/drd  
  
## This handle reaches Carl and Dirk  
MAINTAINER "Carl Boettiger and Dirk Eddelbuettel" rocker-
maintainers@eddelbuettel.com  
  
ENV DEBIAN-FRONTEND noninteractive  
ENV PATH /usr/lib/rstudio-server/bin/:$PATH  
  
RUN apt-get update \  
&& apt-get install -y -t unstable --no-install-recommends \  
libxml2-dev libssl-dev \  
&& install2.r xml2 httr downloader XML \  
&& wget --no-check-certificate \  
https://raw.githubusercontent.com/rocker-org/rstudio-daily/master/latest.R \  
&& Rscript latest.R && rm latest.R  
  
RUN sh -c "echo 'deb http://ftp.de.debian.org/debian jessie main' >>
/etc/apt/sources.list"  
  
RUN apt-get update \  
&& apt-get install -t stable libssl1.0.0 \  
&& apt-get install -y -t unstable --no-install-recommends \  
ca-certificates \  
file \  
git \  
libapparmor1 \  
libedit2 \  
libcurl4-openssl-dev \  
lsb-release \  
psmisc \  
python-setuptools \  
sudo  
  
RUN dpkg -i rstudio-server-daily-amd64.deb \  
&& rm rstudio-server-*-amd64.deb \  
&& ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc /usr/local/bin \  
&& ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc-citeproc /usr/local/bin \  
&& wget https://github.com/jgm/pandoc-templates/archive/1.15.2.1.tar.gz \  
&& mkdir -p /opt/pandoc/templates && tar zxf 1.15.2.1.tar.gz \  
&& cp -r pandoc-templates*/* /opt/pandoc/templates && rm -rf pandoc-templates*
\  
&& mkdir /root/.pandoc && ln -s /opt/pandoc/templates /root/.pandoc/templates
\  
&& apt-get clean  
  
## Ensure that if both httr and httpuv are installed downstream, oauth 2.0
flows still work correctly.  
RUN echo '\n\  
\n# Configure httr to perform out-of-band authentication if HTTR_LOCALHOST \  
\n# is not set since a redirect to localhost may not work depending upon \  
\n# where this Docker container is running. \  
\nif(is.na(Sys.getenv("HTTR_LOCALHOST", unset=NA))) { \  
\n options(httr_oob_default = TRUE) \  
\n}' >> /etc/R/Rprofile.site  
  
## A default user system configuration. For historical reasons,  
## we want user to be 'rstudio', but it is 'docker' in r-base  
RUN usermod -l rstudio docker \  
&& usermod -m -d /home/rstudio rstudio \  
&& groupmod -n rstudio docker \  
&& echo '"\e[5~": history-search-backward' >> /etc/inputrc \  
&& echo '"\e[6~": history-search-backward' >> /etc/inputrc \  
&& echo "rstudio:rstudio" | chpasswd  
  
EXPOSE 8787  
## Have RStudio run with the pre-release R as well  
RUN cd /usr/local/bin \  
&& mv Rdevel R \  
&& mv Rscriptdevel Rscript  
  
## Use s6  
RUN wget -P /tmp/ https://github.com/just-
containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz \  
&& tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
COPY userconf.sh /etc/cont-init.d/conf  
COPY run.sh /etc/services.d/rstudio/run  
  
CMD ["/init"]  


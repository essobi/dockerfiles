FROM opencpu/base  
MAINTAINER "Ilias Biris" ilias.biris@comptel.com  
  
# add CRAN repository (Denmark) for an updated list of R packages & ensure the
locale is set  
RUN echo 'deb http://cran.r-project.org/bin/linux/ubuntu trusty/' >>
/etc/apt/sources.list \  
&& sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 \  
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff  
  
# install packages needed for R scripts (eg littler for R shebang support)  
RUN apt-get update \  
&& apt-get install -y \  
ed \  
less \  
locales \  
vim-tiny \  
wget \  
ca-certificates \  
libxml2-dev \  
libcurl4-openssl-dev \  
libssl-dev \  
texinfo \  
texlive \  
texlive-latex-extra \  
texlive-fonts-extra \  
latex-xcolor \  
libsasl2-dev \  
libcairo2-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
# install litter and configure it  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
littler \  
r-base=${R_BASE_VERSION}* \  
r-base-dev=${R_BASE_VERSION}* \  
r-recommended=${R_BASE_VERSION}* \  
&& echo 'options(repos = list(CRAN = "https://cran.rstudio.com/"),
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
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install the necessary R packages  
RUN install2.r --error devtools \  
&& Rscript -e "devtools::install_version('ggplot2', version='2.2.1')" \  
&& Rscript -e "devtools::install_version('ggthemes', version='3.3.0')" \  
&& Rscript -e "devtools::install_version('gridExtra', version='2.2.1')" \  
&& Rscript -e "devtools::install_version('cowplot', version='0.7.0')" \  
&& Rscript -e "devtools::install_version('plyr', version='1.8.4')" \  
&& Rscript -e "devtools::install_version('dplyr', version='0.5.0')" \  
&& Rscript -e "devtools::install_version('lubridate', version='1.6.0')" \  
&& Rscript -e "devtools::install_version('RColorBrewer', version='1.1-2')" \  
&& Rscript -e "devtools::install_version('mongolite', version='0.9.1')" \  
&& Rscript -e "devtools::install_version('RcppRoll', version='0.2.2')" \  
&& Rscript -e "devtools::install_version('reshape2', version='1.4.2')" \  
&& Rscript -e "devtools::install_version('knitr', version='1.15.1')" \  
&& Rscript -e "devtools::install_version('RCurl', version='1.95-4.8')"\  
&& Rscript -e "devtools::install_version('svglite', version='1.2.0')" \  
&& Rscript -e "devtools::install_version('roxygen2', version='5.0.1')"\  
&& rm -rf /tmp/downloaded_packages/\  
&& sed -i 's/\"timelimit\\.post\"\: 90\,$/\"timelimit\\.post\"\: 1800\,/'
/etc/opencpu/server.conf\  
&& sed -i 's/\"rlimit\\.as\"\: 2e9\,$/\"rlimit\\.as\"\: 8e9\,/'
/etc/opencpu/server.conf  
  
CMD \  
service opencpu restart && \  
tail -F /var/log/opencpu/apache_access.log  
  
WORKDIR /  


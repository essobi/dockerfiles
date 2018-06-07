FROM debian:jessie  
MAINTAINER Steve Nolen <technolengy@gmail.com>  
  
  
ENV RSTUDIO_VERSION 1.0.44  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& echo 'deb http://cran.rstudio.com/bin/linux/debian jessie-cran3/' >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480 \  
&& apt-get update \  
&& apt-get install -y r-base gdebi git curl libcurl4-openssl-dev libssl-dev ed
cron libmysqlclient-dev libxml2-dev ruby ruby-dev netcat libxcrypt1 locales \  
&& apt-get install -y texlive-full nano mysql-client  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN curl -fSL http://download2.rstudio.org/rstudio-
server-${RSTUDIO_VERSION}-amd64.deb -o /tmp/rstudio-server.deb \  
&& curl -fSL http://http.us.debian.org/debian/pool/main/libp/libpam-
unix2/libpam-unix2_2.4.1-6_amd64.deb -o /tmp/libpam-unix2.deb \  
&& gdebi -n /tmp/rstudio-server.deb \  
&& dpkg -i /tmp/libpam-unix2.deb\  
&& gem install mysql2 && gem install daybreak \  
&& apt-get purge -y libmysqlclient-dev ruby-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN /usr/bin/R -e 'install.packages(c("devtools"), repo =
"http://cran.rstudio.com")'  
RUN /usr/bin/R -e 'devtools::install_version("mosaic",version="0.14.4", repos
= "http://cran.us.r-project.org")'  
RUN /usr/bin/R -e 'devtools::install_version("testthat",repos =
"http://cran.us.r-project.org")'  
RUN /usr/bin/R -e 'devtools::install_github("mobilizingcs/mobilizr")'  
  
# set pam to use blowfish to support the ohmage sync script.  
RUN sed -i 's/pam_unix.so/pam_unix2.so/g' /etc/pam.d/common-*  
RUN sed -i 's/obscure sha512/obscure blowfish/g' /etc/pam.d/common-password  
RUN echo 'suppressPackageStartupMessages(library(mobilizr,
warn.conflicts=FALSE, quietly=TRUE))' > /etc/R/Rprofile.site  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
ADD sync.rb /sync.rb  
  
VOLUME /home  
VOLUME /sync  
EXPOSE 8787  
CMD ["/run.sh"]  
  
RUN cp /etc/pam.d/login /etc/pam.d/rstudio  
RUN cp /etc/pam.d/login /etc/pam.d/rstudio-connect  
  
RUN chmod 777 /tmp -R  
RUN chmod 777 /tmp  
  
# Install script for RStudio Server using mobilizr-beta  
RUN /usr/bin/R -e 'devtools::install_github("mangoTheCat/visualTest")'  
RUN /usr/bin/R -e 'devtools::install_version("readr", "1.1.1", repos =
"https://cloud.r-project.org")'  
#RUN /usr/bin/R -e 'devtools::install_version("stringr", "1.2", repos =
"https://cloud.r-project.org")'  
#RUN /usr/bin/R -e 'devtools::install_version("mosaic", "0.14.4", repos =
"https://cloud.r-project.org")'  
RUN /usr/bin/R -e 'devtools::install_github("mobilizingcs/mobilizr@beta")'  
  
RUN chmod 777 /tmp -R  
RUN chmod 777 /tmp  
  


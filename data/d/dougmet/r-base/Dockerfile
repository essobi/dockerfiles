# Adapted from r-base on https://github.com/rocker-org/rocker  
FROM ubuntu:14.04  
## Who made this  
MAINTAINER "Doug Ashton" dashton@mango-solutions.com  
  
# 29th October 2015, mid release. Should update?  
ENV R_BASE_VERSION 3.2.2  
ENV R_CRAN_DATE 2015-10-29  
## Set a default user. Available via runtime flag `--user docker`  
## Add user to 'staff' group, granting them write privileges to
/usr/local/lib/R/site.library  
## User should also have & own a home directory (for rstudio or linked volumes
to work properly).  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff  
  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Install R  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 \  
&& apt-get -qq update \  
&& apt-get -y install r-base-core=${R_BASE_VERSION}* \  
r-base-dev=${R_BASE_VERSION}* \  
# r-recommended=${R_BASE_VERSION}* \  
libcurl4-openssl-dev \  
libxml2-dev \  
git \  
wget  
  
# Set the MRAN mirror  
RUN echo "local({\n r <\- getOption(\"repos\")\n\  
r[\"CRAN\"] <\- \  
\"https://mran.revolutionanalytics.com/snapshot/"${R_CRAN_DATE}"\"\n\  
options(repos = r)\n\  
})\n" >> /etc/R/Rprofile.site  
  
# Install pkgsnap for package management  
RUN cd /tmp \  
&& git clone https://github.com/MangoTheCat/pkgsnap.git \  
&& R CMD INSTALL -l "/usr/local/lib/R/site-library" pkgsnap \  
&& rm -r pkgsnap  
  
CMD ["R"]


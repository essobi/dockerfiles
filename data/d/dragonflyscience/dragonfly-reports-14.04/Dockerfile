FROM ubuntu:14.04  
MAINTAINER chris@dragonfly.co.nz  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i 's/archive/nz.archive/' /etc/apt/sources.list  
RUN echo "Pacific/Auckland" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
RUN locale-gen en_NZ.UTF-8  
RUN dpkg-reconfigure locales  
ENV LANG en_NZ.UTF-8  
ENV LANGUAGE en_NZ:en  
COPY fonts/ /usr/local/share/fonts/  
  
RUN echo "deb http://cran.stat.auckland.ac.nz/bin/linux/ubuntu trusty/" >
/etc/apt/sources.list.d/cran.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
texlive-full \  
biber \  
r-base-dev \  
r-recommended \  
r-base \  
libpq-dev \  
postgresql-client \  
git-core \  
pandoc \  
python-pygments \  
jags \  
software-properties-common \  
curl && \  
apt-add-repository multiverse && \  
apt-get update && \  
apt-get install -y msttcorefonts && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY r_requirements.r /etc/r_requirements.r  
RUN R --slave < /etc/r_requirements.r  
RUN curl
https://cran.r-project.org/src/contrib/Archive/xtable/xtable_1.8-0.tar.gz >
/tmp/xtable.tar.gz && \  
R CMD INSTALL /tmp/xtable.tar.gz && \  
rm /tmp/xtable.tar.gz  
RUN curl https://cran.r-project.org/src/contrib/data.table_1.9.6.tar.gz >
/tmp/data.table.tar.gz && \  
R CMD INSTALL /tmp/data.table.tar.gz && \  
rm /tmp/data.table.tar.gz  
  
COPY dragonfly-latex-templates_1.11_all.deb /tmp/  
RUN dpkg -i /tmp/dragonfly-latex-templates_1.11_all.deb  
  


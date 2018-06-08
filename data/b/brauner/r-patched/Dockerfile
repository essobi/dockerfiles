FROM ubuntu:latest  
  
MAINTAINER Christian Brauner christianvanbrauner[at]gmail.com  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& export DEBCONF_NONINTERACTIVE_SEEN=true \  
&& cd /etc/dpkg/dpkg.cfg.d \  
&& printf '\npath-exclude=/usr/share/locale/*' >> excludes \  
&& printf '\npath-include=/usr/share/locale/en*' >> excludes \  
&& printf '\npath-include=/usr/share/locale/locale.alias' >> excludes \  
&& printf '\npath-exclude=/usr/share/man/*' >> excludes \  
&& printf '\npath-include=/usr/share/man/en*' >> excludes \  
&& printf '\npath-include=/usr/share/man/man[1-9]/*' >> excludes \  
&& apt-get update -qq -y \  
&& apt-get install -y --no-install-recommends \  
less \  
zip \  
unzip \  
&& apt-get build-dep -y \  
r-base \  
r-base-dev \  
r-recommended \  
&& apt-get clean \  
&& cd /var/lib/apt/lists/ \  
&& rm -rf *  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& export DEBCONF_NONINTERACTIVE_SEEN=true \  
&& apt-get update -qq -y \  
&& apt-get install -y --no-install-recommends \  
subversion \  
rsync \  
&& cd /tmp \  
&& svn co http://svn.r-project.org/R/branches/R-3-2-branch R-patched \  
&& cd /tmp/R-patched \  
&& tools/rsync-recommended \  
&& R_PAPERSIZE=a4 \  
R_BATCHSAVE="--no-save --no-restore" \  
R_BROWSER=xdg-open \  
R_PDFVIEWER=mupdf \  
PAGER=/usr/bin/less \  
PERL=/usr/bin/perl \  
R_UNZIPCMD=/usr/bin/unzip \  
R_ZIPCMD=/usr/bin/zip \  
R_PRINTCMD=/usr/bin/lpr \  
LIBnn=lib \  
AWK=/usr/bin/awk \  
CFLAGS="-pipe -std=gnu99 -Wall -pedantic -O3" \  
CXXFLAGS="-pipe -Wall -pedantic -O3" \  
./configure --enable-R-shlib \  
\--without-blas \  
\--without-lapack \  
\--with-readline \  
&& make \  
&& make install \  
&& cd /tmp \  
&& rm -rf R-patched \  
&& apt-get clean \  
&& cd /var/lib/apt/lists \  
&& rm -rf *  
  
# Add user  
RUN echo 'root:test' | chpasswd \  
&& useradd -u 1000 -m docker \  
&& echo 'docker:test' | chpasswd \  
&& usermod -s /bin/bash docker \  
&& usermod -a -G 100 docker \  
# && usermod -a -G sudo docker \  
# set standard repository  
&& cd /home/docker \  
&& printf
'options(repos=structure(c(CRAN='\''http://stat.ethz.ch/CRAN/'\'')))\n' >
.Rprofile \  
  
ENV HOME /home/docker  
WORKDIR /home/docker  
USER docker  
  
ENTRYPOINT ["/usr/local/bin/R"]  


########################################################  
# Everything needed for generating Claret plots with R.  
#  
# The included `Rscript` script runs Rscript inside the  
# Docker environment.  
#  
# Usage:  
# $ docker/Rscript <plot.r>  
#  
########################################################  
FROM rocker/r-base  
MAINTAINER Brandon Holt <holt.bg@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
make \  
texlive-fonts-recommended \  
texlive-humanities \  
texlive-latex-extra \  
texinfo \  
zsh \  
mysql-client && \  
apt-get install -y -t unstable \  
libcairo2-dev \  
libmysqlclient-dev \  
libsqlite3-dev \  
libcurl4-openssl-dev \  
libssl-dev \  
libxml2-dev  
  
RUN install2.r --error \  
ggplot2 \  
devtools \  
plyr \  
dplyr \  
reshape2 \  
sitools \  
jsonlite \  
yaml \  
sqldf \  
RMySQL \  
scales \  
Unicode \  
extrafont \  
Hmisc  
  
RUN install2.r --error TTR  
  
ENV USER root  
  
ADD dots/Rprofile /root/.Rprofile  
ADD dots/my.cnf /root/.my.cnf  
ADD pdfstill /usr/local/bin/pdfstill  
  
RUN apt-get install -y nodejs npm git &&\  
npm install -g madoko  
  
RUN apt-get install -y texlive texlive-xetex libimage-exiftool-perl \  
pdf2svg texlive-math-extra imagemagick texlive-science &&\  
chmod +x /usr/local/bin/pdfstill &&\  
ln -s /usr/bin/nodejs /usr/bin/node  
  
# install latest dvisvgm to make madoko happy  
RUN apt-get install -y libkpathsea-dev libpotrace-dev wget &&\  
wget
https://github.com/mgieseki/dvisvgm/releases/download/1.15/dvisvgm-1.15.tar.gz
&&\  
tar xzf dvisvgm-1.15.tar.gz &&\  
cd dvisvgm-1.15 &&\  
./configure &&\  
make && make install &&\  
cd .. && rm -rf dvisvgm-1.15.tar.gz dvisvgm-1.15  
  
# install fonts  
ADD fonts /usr/local/share/fonts  
RUN cd /usr/local/share/fonts &&\  
wget http://www.marksimonson.com/assets/content/fonts/AnonymousPro-1.002.zip
&&\  
unzip AnonymousPro-1.002.zip &&\  
mv AnonymousPro-1.002.001 AnonymousPro &&\  
mkdir CrimsonText && cd CrimsonText &&\  
wget http://www.fontsquirrel.com/fonts/download/crimson &&\  
unzip crimson && rm crimson &&\  
cd .. && rm -f *.zip &&\  
fc-cache -v  
  
RUN cd /usr/local/share/fonts &&\  
wget http://www.latofonts.com/download/Lato2OFL.zip &&\  
unzip Lato2OFL.zip &&\  
rm -rf Lato2OFL.zip __MACOSX &&\  
fc-cache -v  
  
RUN apt-get install -y ruby-dev && gem install bibtex-ruby  
  
RUN apt-get install -y texlive-generic-extra  
  
# fix madoko fontspec loading to work with mathspec  
RUN sed -i.bak s/\\{fontspec\\}/[no-math]{fontspec}/g
/usr/local/lib/node_modules/madoko/styles/css.sty &&\  
sed -i.bak s/\\{fontspec\\}/[no-math]{fontspec}/g
/usr/local/lib/node_modules/madoko/styles/madoko2.sty  
  
VOLUME /src  
WORKDIR /src  
  
CMD ["R"]  


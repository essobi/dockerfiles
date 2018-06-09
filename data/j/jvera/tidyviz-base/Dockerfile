FROM rocker/ropensci:latest  
  
LABEL maintainer "vera.josemanuel@gmail.com"  
  
ADD configure.R /tmp/configure.R  
  
RUN apt-get update -qq && apt-get -y --allow-unauthenticated --no-install-
recommends install \  
imagemagick \  
libgeos++-dev \  
libspatialite-dev \  
libv8-3.14-dev \  
libgtk2.0-dev \  
libnlopt-dev \  
libgomp1 \  
libjpeg62-turbo-dev \  
libtool \  
m4 \  
automake \  
apt-utils \  
ed \  
r-cran-rgtk2 \  
libmpfr-dev \  
libssh-dev \  
&& . /etc/environment \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
  
RUN install2.r --error --deps TRUE Amelia \  
archivist \  
bookdown \  
charlatan \  
colourpicker \  
compare \  
condformat \  
conflicted \  
cowplot \  
CRANsearcher \  
ctv \  
data.table \  
DataCombine \  
dataCompareR \  
DataExplorer \  
dataMaid \  
datapasta \  
dataPreparation \  
densityClust \  
descriptr \  
desctable \  
DescTools \  
diffobj \  
drake \  
errorist \  
ERSA \  
extrafont \  
factoextra \  
filesstrings \  
fitdistrplus \  
fs \  
funModeling \  
futile.logger \  
GGally \  
here \  
Hmisc \  
janitor \  
knitr \  
lessR \  
likert \  
logging \  
MASS \  
mi \  
missForest \  
naniar \  
naturalsort \  
numform \  
pathological \  
PMCMRplus \  
pkgdown \  
pkggraph \  
pool \  
processx \  
profvis \  
psych \  
rlist \  
R.utils \  
rio \  
rlang \  
rmarkdown \  
sessioninfo \  
showtext \  
sigr \  
Simpsons \  
simstudy \  
SmartEDA \  
snakecase \  
ssh \  
startup \  
stranger \  
summarytools \  
tableone \  
tabplot \  
tadaatoolbox \  
tatoo \  
thinkr \  
usethis \  
VIM \  
visdat \  
workflowr \  
WVPlots \  
xray \  
yarrr \  
ztable \  
&& Rscript /tmp/configure.R \  
&& Rscript -e 'extrafont::font_import(prompt = FALSE)' \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  


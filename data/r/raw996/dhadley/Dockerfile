ARG RVERSION=RVERSION  
FROM rocker/verse:${RVERSION}  
MAINTAINER "Carl Boettiger and Dirk Eddelbuettel" rocker-
maintainers@eddelbuettel.com  
  
# include new repo  
RUN sed -i
"s/CRAN/raubreywhite=\'https:\\\/\\\/raubreywhite.github.io\\\/drat\\\/\',CRAN/"
/usr/local/lib/R/etc/Rprofile.site  
RUN sed -i "1s/^/dratRepo=\'\\\/git\\\/drat\\\/\'\n/"
/usr/local/lib/R/etc/Rprofile.site  
  
RUN apt-get update && apt-get install -y libgdal-dev libgeos-c1v5 libproj-dev
libgsl0-dev libprotobuf-dev protobuf-compiler  
RUN apt-get update && apt-get install -y ncftp ftp cron sshpass  
RUN apt-get update && apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-
common-dev libudunits2-dev  
  
RUN apt-get update && apt-get install -y libreoffice  
  
# data.table doesn't like clang  
RUN . /etc/environment \  
&& install2.r --error --repos $MRAN \  
data.table \  
influenceR \  
gower  
  
# Install clang to use as compiler  
# clang seems to be more memory efficient with the templates than g++  
# with g++ rstan cannot compile on docker hub due to memory issues  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
clang  
  
# Global site-wide config  
RUN mkdir -p $HOME/.R/ \  
&& echo "\nCXX=clang++ -ftemplate-depth-256\n" >> $HOME/.R/Makevars \  
&& echo "CC=clang\n" >> $HOME/.R/Makevars \  
&& echo "CXXFLAGS += -Os\n" >> $HOME/.R/Makevars  
  
RUN . /etc/environment \  
&& install2.r --error --repos $MRAN --deps TRUE \  
ggrepel \  
lme4 \  
arm \  
gmailr \  
pander \  
httpuv  
  
RUN install2.r --error --repos https://www.math.ntnu.no/inla/R/stable --deps
FALSE \  
INLA  
  
RUN apt-get install -y jags  
  
RUN . /etc/environment \  
&& install2.r --error --repos $MRAN --deps TRUE \  
surveillance \  
munsell \  
RColorBrewer \  
labeling \  
htmltools \  
evaluate \  
R.utils \  
openxlsx \  
splitstackshape \  
corrr \  
ggdendro \  
ClustOfVar \  
dendextend \  
plumber \  
knitcitations \  
bibtex \  
brew \  
Hmisc \  
ggvis \  
Formula \  
roxygen2 \  
packrat \  
rms \  
survey \  
miniCRAN \  
MatrixModels \  
shiny \  
flexdashboard \  
pomp \  
xgboost \  
directlabels \  
rstan \  
shinystan \  
ineq \  
lomb \  
rmarkdown \  
shinyBS \  
rgeolocate \  
glm2 \  
zip \  
doSNOW \  
drat \  
profvis \  
glmnet \  
glmnetUtils \  
pscl \  
knitr \  
bookdown \  
reticulate \  
processx  
  
RUN . /etc/environment \  
&& install2.r --error --repos $MRAN --deps TRUE \  
survminer \  
units \  
rgdal \  
rgeos \  
geojsonio \  
rmapshaper \  
styler  
  
## DRAT PACKAGES  
RUN . /etc/environment \  
&& install2.r --error \  
RAWmisc \  
fhi \  
momo \  
sykdomspuls \  
normomo \  
reporttb \  
sykdomspulslog \  
sykdomspulspdf  
  
RUN echo "/usr/local/lib/R/lib" > /etc/ld.so.conf.d/libR.conf  
RUN ldconfig  
  
## NEWER STUFF THAT NEEDS TO BE INSTALLED FROM GITHUB  
RUN R -e
"devtools::install_github('Appsilon/shiny.router',ref='7d9bc757ea31a1fe8faea6a5817c8adda97a0be0')"  
RUN R -e "devtools::install_github('stan-dev/projpred',
ref='d9a59c432899d2c3086623302188eb140bee2e21')"  
RUN R -e "devtools::install_github('r-lib/testthat')"  
  
env LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive  
#RUN apt-get update && apt-get install -y \  
# texlive-xetex  
## TENSORFLOW  
RUN apt-get install -y python3-pip python3-dev  
RUN pip3 install --upgrade pip  
RUN pip3 install tensorflow  
RUN pip3 install junit-xml  
  
RUN R -e
"Sys.setenv(TENSORFLOW_PYTHON_VERSION=3);install.packages('tensorflow')"  
  
# rclone  
RUN apt-get update && apt-get install -y \  
curl man-db  
RUN curl https://rclone.org/install.sh | sudo bash  
  
RUN mkdir /analyses  
RUN mkdir /dropbox  
RUN chmod 777 /analyses /dropbox  
  
# preferences to stop timing out  
COPY rsession.conf /etc/rstudio/rsession.conf  


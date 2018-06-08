FROM rocker/verse:latest  
  
# System requirements  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
parallel \  
python3-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
# tex  
RUN tlmgr update --self && tlmgr install \  
booktabs \  
colortbl \  
fancyhdr \  
float \  
lipsum \  
multirow \  
setspace \  
tabu \  
varwidth \  
threeparttable \  
wrapfig \  
xcolor  
  
# R packages  
RUN install2.r --error --dep TRUE \  
arules \  
caret \  
clusterGeneration \  
doMC \  
fastICA \  
feather \  
glmnet \  
GPArotation \  
gTests \  
kableExtra \  
mclust \  
MixSim \  
mixtools \  
MVN \  
mvnTest \  
pacman \  
pdp \  
Rtsne \  
vegan \  
xgboost  
  
RUN Rscript -e "devtools::install_github('rstudio/rmarkdown')"  
RUN Rscript -e "devtools::install_github('ismayc/thesisdown')"  
RUN Rscript -e "devtools::install_github('ryantibs/conformal', \  
subdir = 'conformalInference')"  
# Python dependencies  
RUN pip3 install --upgrade pip  
RUN pip3 install \  
bokeh \  
feather-format \  
fire \  
jupyter \  
matplotlib \  
numpy \  
pandas \  
scipy \  
scikit-learn  


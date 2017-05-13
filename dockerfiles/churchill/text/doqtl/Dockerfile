## Based on rocker / hadleyverse maintained by Carl Boettiger and Dirk Eddelbuettel
FROM rocker/hadleyverse

MAINTAINER "Daniel Gatti" dan.gatti@jax.org

# install svd package
RUN install2.r --error svd

# DESeq2, DOQTL and dependencies.
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(c("DESeq2","DOQTL"), ask=FALSE)'
RUN Rscript -e 'install.packages(pkgs = "devtools", dependencies = TRUE)'
RUN Rscript -e 'library(devtools); install_github(repo = "dmgatti/DOQTL")'


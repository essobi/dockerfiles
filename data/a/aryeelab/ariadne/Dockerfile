############################################################  
# Dockerfile to build Ariadne command line and Shiny webapp  
############################################################  
  
# Set the base image to anaconda python 2.7  
FROM continuumio/anaconda  
  
# File Author / Maintainer  
MAINTAINER Luca Pinello & Caleb Lareau  
  
ENV SHELL bash  
  
#install dependencies  
  
RUN apt-get update && apt-get install make gcc g++ zlib1g-dev zlib1g
libpng12-0 default-jre unzip tabix -y  
  
#build font cache for matplotlib  
RUN python -c "import matplotlib.pyplot"  
  
#install bioconda and dependencies  
RUN conda install -c r r  
RUN conda config --add channels r  
RUN conda config --add channels bioconda  
RUN conda install -c conda-forge geos=3.6.0  
RUN conda install -y gcc scikit-learn networkx seaborn  
  
RUN apt-get install gfortran -y  
  
###################################  
# Install R packages / shiny server  
###################################  
  
# Install dependencies and Download and install shiny server  
RUN apt-get update && apt-get install -y \  
sudo \  
gdebi-core \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev && \  
wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install git+git://github.com/scikit-learn/scikit-learn@master  
  
RUN apt-get update && \  
apt-get install -y git libxml2-dev libssl-dev ghostscript  
  
  
# Install Ariadne and other files  
COPY . /srv/shiny-server/Ariadne  
WORKDIR /srv/shiny-server/Ariadne  
  
# See this error message: https://github.com/hadley/devtools/issues/379  
RUN ln -s /bin/tar /bin/gtar  
  
# Install packrat packages  
RUN Rscript -e 'install.packages("packrat", repos =
"http://cran.us.r-project.org"); \  
packrat::restore()'  
  
RUN pip install rpy2  
RUN pip install shapely  
RUN python install_princurve.py  
  
# Temporary permissions hack  
RUN chown shiny:shiny -R packrat && \  
chown shiny:shiny .gitignore && \  
chown shiny:shiny -R . && \  
chmod 755 -R .  
  
# Serve only the Ariadne app (replace /srv/shiny-server with /srv/shiny-
server/Ariadne)  
RUN sed -i 's/\/srv\/shiny-server/\/srv\/shiny-server\/Ariadne/' /etc/shiny-
server/shiny-server.conf  
  
# Improve first page load time by not shutting down the R session when idle  
RUN sed -i '/location \/ {/a app_idle_timeout 0;' /etc/shiny-server/shiny-
server.conf  
  
# Increase app load timeout  
RUN sed -i '/location \/ {/a app_init_timeout 60;' /etc/shiny-server/shiny-
server.conf  
  
#remove some warning that are thrown during the first execution  
RUN python Ariadne.py -m exampleData/data_guoji.tsv -l
exampleData/cell_label.tsv -c exampleData/cell_label_color.tsv -o test  
  
# Start and expose shiny server  
EXPOSE 3838  
  
ENTRYPOINT ["/opt/conda/bin/python", "/srv/shiny-
server/Ariadne/ariadne_router.py"] # this is to route the commands ariadne-cli
and ariadne-webapp  
  


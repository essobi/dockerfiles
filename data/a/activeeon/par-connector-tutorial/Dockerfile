FROM ubuntu:16.04  
# Add the R repository and it's keys  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list && \  
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \  
gpg -a --export E084DAB9 | apt-key add -  
  
# Install R, java8 and rJava  
RUN apt-get update && \  
apt-get install -y \  
r-base \  
openjdk-8-jdk \  
r-cran-rjava \  
wget  
  
# Configure R  
RUN R CMD javareconf -e  
  
# Download and install ActiveEon par connector and install 'gtools',
'codetools', 'stringr'  
RUN wget https://s3.amazonaws.com/par-connector-tutorial/par-connector-
tutorial-R-x86_64-pc-linux-gnu.tar.gz && \  
Rscript -e "dir.create(Sys.getenv('R_LIBS_USER'),
recursive=TRUE);install.packages(c('gtools', 'codetools', 'stringr'),
Sys.getenv('R_LIBS_USER'), repo='http://cran.case.edu');install.packages('par-
connector-tutorial-R-x86_64-pc-linux-gnu.tar.gz', Sys.getenv('R_LIBS_USER'),
repos = NULL)"  
  
ENTRYPOINT ["/bin/bash", "R"]


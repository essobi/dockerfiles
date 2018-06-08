# genairics  
# VERSION 0.0.2  
# In the dockerfile, dependencies are put that require sudo or are provided by  
# modules in our university HPC cluster.  
# genairics_dependencies.sh, provides the dependencies that a regular user can
install  
# genairics_dependencies.sh can also be installed independently from the
dockerfile  
# by providing the PREFIX env variable  
FROM python:3.6.3  
ARG buildtype=production  
ENV GAX_REPOS=/repos  
ENV GAX_ENVS=/envs  
ENV GAX_PREFIX=/usr  
ENV GAX_RESOURCES=/resources  
RUN apt-get update && apt-get install -y git unzip rsync default-jre fastqc
bedtools r-base  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R")' -e
'biocLite(c("limma"))'  
RUN mkdir $GAX_REPOS  
ADD genairics/scripts/genairics_dependencies.sh
$GAX_REPOS/genairics_dependencies.sh  
RUN $GAX_REPOS/genairics_dependencies.sh  
RUN if [ "$buildtype" = "production" ]; then pip install genairics; fi  
RUN if [ "$buildtype" = "development" ]; then \  
git clone -b dev --single-branch https://github.com/beukueb/genairics.git &&\  
cd genairics && pip install .; fi  
EXPOSE 8000  
VOLUME ["/resources"]  
VOLUME ["/data"]  
VOLUME ["/results"]  
ENTRYPOINT ["genairics"]  
CMD ["-h"]  


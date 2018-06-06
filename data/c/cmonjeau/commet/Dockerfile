############################################################  
# Dockerfile to build Commet tool container image  
# Based on debian wheezy  
############################################################  
  
# Set the base image to debian wheezy  
FROM debian:wheezy  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make gcc g++ unzip curl r-base python  
  
ENV ZIP http://github.com/pierrepeterlongo/commet/archive/master.zip  
ENV SOURCE commet-master  
ENV DIR /opt  
  
################## DEPENDENCIES INSTALLATION ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
  
#################### INSTALL GPLOTS FOR R #########################  
  
RUN curl -O
http://cran.ma.imperial.ac.uk/src/contrib/Archive/gplots/gplots_2.6.0.tar.gz  
RUN tar xzf gplots_2.6.0.tar.gz  
  
RUN echo 'options(repos=structure(c(CRAN="http://cran.ma.imperial.ac.uk")))' >
/tmp/inst.sh  
RUN echo 'install.packages("gtools")' >> /tmp/inst.sh  
RUN echo 'install.packages("gdata")' >> /tmp/inst.sh  
RUN echo 'install.packages("gplots", repos = NULL, type="source")' >>
/tmp/inst.sh  
  
RUN Rscript /tmp/inst.sh  
  
################## COMMET INSTALLATION ######################  
  
WORKDIR ${DIR}  
ADD ${ZIP} tmp.zip  
RUN unzip tmp.zip && rm tmp.zip  
WORKDIR ${DIR}/${SOURCE}  
RUN make && make install  
  
ENTRYPOINT ["./Commet.py"]  
CMD ["-h"]  
  
##################### Maintainer #####################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  
  
#################### Example ########################  
# docker run -it --rm cmonjeau/commet  
# docker run -it --rm -v /root/Commet:/data cmonjeau/commet
/data/sets_config.txt -k 33 -o /data/results  
  


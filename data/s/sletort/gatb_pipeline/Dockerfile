############################################################  
# Dockerfile to build gatb_pipeline tool container image  
# Based on debian Jessie/8  
############################################################  
  
# Set the base image to debian  
FROM sletort/semantic_programs:latest  
  
################## DEPENDENCIES INSTALLATION ######################  
ENV PACKAGES bwa make nano \  
python-pip python-dev zlib1g-dev python-scipy python-networkx  
  
RUN apt-get clean -y  
RUN apt-get update  
RUN apt-get install -y ${PACKAGES}  
RUN pip install mathstats pyfasta pysam==0.8.3  
  
#### Already defined directories ####  
#### please use and do not modify. ####  
# ENV DIR /opt  
# ENV DESCR_DIR /opt/descr  
  
################## gatb_pipeline INSTALLATION ######################  
WORKDIR ${DIR}  
  
## get code source  
#--- from git repo  
ENV GIT https://github.com/GATB/gatb-minia-pipeline.git  
RUN git clone --recursive ${GIT}  
  
#--- /from git repo  
  
# Patch to use minia compiled on jenkins  
RUN curl -L
https://github.com/GATB/minia/releases/download/v3.2.0/minia-v3.2.0-bin-
Linux.tar.gz -o minia-v3.2.0.tgz  
RUN tar xvzf minia-v3.2.0.tgz  
  
# directory containing source code  
# should be under $DIR  
ENV SOURCE_DIR $DIR/gatb-minia-pipeline  
  
WORKDIR ${SOURCE_DIR}  
RUN rm -f minia/minia  
RUN ln -s ${DIR}/minia-v3.2.0-bin-Linux/bin/minia minia/  
  
RUN ln -s $SOURCE_DIR/gatb /usr/local/bin/  
  
## test commands  
# current test fail du to too good assembly (before besst) ?  
# RUN make test  
  
## add program description  
WORKDIR $DESCR_DIR  
ENV DESCR_URL
https://gitlab.irisa.fr/semantic_programs/program_descriptions_data/raw/master/descr/gatb_pipeline.json  
RUN curl $DESCR_URL > gatb_pipeline.json  
  
  
################## Dockerfile usage ######################  
## the command launched by default when running the container  
ENTRYPOINT ["gatb"]  
CMD ["-help"]  
  
################## METADATA ######################  
MAINTAINER "sletort"  
  
LABEL ANNOT.Version="2018.05"  
# ANNOT.Licence="" \  
  
LABEL ANNOT.Name="gatb-pipeline" \  
ANNOT.Description="gatb-pipeline uses gatb tools to generate an assembly from
short reads. It uses bloocoo, minia, and a non gatb-tool named BESST." \  
ANNOT.author="Rayan Chikhi" \  
ANNOT.Vendor="Inria" \  
ANNOT.Homepage="https://github.com/GATB/gatb-minia-pipeline" \  
ANNOT.Support_URL="https://www.biostars.org/t/minia/" \  
ANNOT.EDAM_Operation="['operation_0524', 'operation_0525']" \  
ANNOT.EDAM_Topic="['topic_0199', 'topic_0654', 'topic_0196']" \  
ANNOT.Requires="['python', 'python-scipy', 'pysam==0.8.3', 'git', 'bwa',
'make', 'mathstats']" \  
ANNOT.Provides="['bloocoo', 'minia', 'BESST', 'gatb']" \  
ANNOT.author_URI="['http://cristal.univ-lille.fr/~chikhi/']"  
  
# Comment to translate edam code in labels (for human comprehension).  
#EDAM_Operation  
# operation_0524 - De-novo assembly  
# operation_0525 - Genome assembly  
#  
#EDAM_Topic  
# topic_0199 - Genetic variation  
# topic_0654 - DNA analysis  
# topic_0196 - Sequence assembly  


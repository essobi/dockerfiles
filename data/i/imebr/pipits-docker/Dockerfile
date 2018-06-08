ARG baseimage_version=xenial  
FROM ubuntu:${baseimage_version}  
  
ARG version=master  
ARG VCS_REF  
ARG BUILD_DATE  
  
RUN echo "VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}", branch:
"${version}  
  
LABEL maintainer="frank.foerster@ime.fraunhofer.de" \  
description="Container for the PITITS package" \  
version="1.0" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/ime-tools/pipits-docker"  
  
RUN apt update && \  
apt install --yes --no-install-recommends \  
biom-format-tools \  
fastx-toolkit \  
hmmer \  
python-pip \  
python3-setuptools \  
python-setuptools \  
openjdk-8-jre-headless \  
wget \  
bzip2 \  
gzip \  
unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install numpy  
  
ENV PIPITS_DIR=/opt/pipits  
  
WORKDIR /opt  
RUN wget https://github.com/hsgweon/pipits/archive/1.5.0.tar.gz -O
1.5.0.tar.gz && \  
tar xvfz 1.5.0.tar.gz && \  
cd pipits-1.5.0 && \  
python setup.py install --prefix=${PIPITS_DIR} && \  
cd \- && \  
rm 1.5.0.tar.gz  
  
RUN wget
https://github.com/torognes/vsearch/releases/download/v2.4.3/vsearch-2.4.3-linux-x86_64.tar.gz
&& \  
tar xvfz vsearch-2.4.3-linux-x86_64.tar.gz && \  
rm vsearch-2.4.3-linux-x86_64.tar.gz && \  
ln -s $PWD/vsearch-2.4.3-linux-x86_64/bin/vsearch ${PIPITS_DIR}/bin/vsearch  
  
RUN wget http://microbiology.se/sw/ITSx_1.0.11.tar.gz && \  
tar xvfz ITSx_1.0.11.tar.gz && \  
rm ITSx_1.0.11.tar.gz && \  
ln -s $PWD/ITSx_1.0.11/ITSx ${PIPITS_DIR}/bin/ITSx && \  
ln -s $PWD/ITSx_1.0.11/ITSx_db ${PIPITS_DIR}/bin/ITSx_db && \  
cd ${PIPITS_DIR}/bin/ITSx_db/HMMs && \  
rm -f *.hmm.* && \  
echo *.hmm | xargs -n1 hmmpress; \  
cd -  
  
RUN wget https://sourceforge.net/projects/rdp-classifier/files/rdp-
classifier/rdp_classifier_2.12.zip && \  
unzip rdp_classifier_2.12.zip && \  
rm rdp_classifier_2.12.zip && \  
ln -s $PWD/rdp_classifier_2.12/dist/classifier.jar
${PIPITS_DIR}/classifier.jar  
  
RUN mkdir -p ${PIPITS_DIR}/refdb && cd ${PIPITS_DIR}/refdb && \  
wget
http://sourceforge.net/projects/pipits/files/UNITE_retrained_28.06.2017.tar.gz
-O UNITE_retrained_28.06.2017.tar.gz && \  
rm -rf UNITE_retrained && \  
tar xvfz UNITE_retrained_28.06.2017.tar.gz && \  
chmod -R a+r /opt/pipits/refdb && \  
rm UNITE_retrained_28.06.2017.tar.gz  
  
RUN mkdir -p ${PIPITS_DIR}/refdb && cd ${PIPITS_DIR}/refdb && \  
wget https://unite.ut.ee/sh_files/uchime_reference_dataset_01.01.2016.zip -O
uchime_reference_dataset_01.01.2016.zip && \  
unzip uchime_reference_dataset_01.01.2016.zip && \  
chmod -R a+r /opt/pipits/refdb && \  
rm uchime_reference_dataset_01.01.2016.zip  
  
RUN mkdir -p ${PIPITS_DIR}/refdb && cd ${PIPITS_DIR}/refdb && \  
wget https://sourceforge.net/projects/pipits/files/warcup_retrained_V2.tar.gz
&& \  
tar xvzf warcup_retrained_V2.tar.gz && \  
chmod -R a+r /opt/pipits/refdb && \  
rm warcup_retrained_V2.tar.gz  
  
ENV PATH=${PIPITS_DIR}/bin:$PATH  
ENV PYTHONPATH=${PIPITS_DIR}/lib/python2.7/site-packages:$PYTHONPATH  
ENV
PIPITS_UNITE_REFERENCE_DATA_CHIMERA=${PIPITS_DIR}/refdb/uchime_reference_dataset_01.01.2016/uchime_reference_dataset_01.01.2016.fasta  
ENV PIPITS_UNITE_RETRAINED_DIR=${PIPITS_DIR}/refdb/UNITE_retrained  
ENV PIPITS_WARCUP_RETRAINED_DIR=${PIPITS_DIR}/refdb/warcup_retrained_V2  
ENV PIPITS_RDP_CLASSIFIER_JAR=${PIPITS_DIR}/classifier.jar  
  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
VOLUME /data  
WORKDIR /data  


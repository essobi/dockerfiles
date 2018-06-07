FROM ubuntu:16.04  
# Define directories  
ENV OUTPUT_DIR /data  
ENV WORK_DIR /code  
ENV OPT_DIR /opt  
ENV SHARED_FS /ifs  
  
# Install Dependencies  
WORKDIR ${OPT_DIR}  
RUN apt-get update && apt-get -yqq install \  
git \  
ghostscript \  
imagemagick \  
locales \  
python \  
python-dev \  
python-matplotlib \  
python-numpy \  
python-pandas \  
python-pip \  
python-reportlab \  
python-scipy \  
r-base-core \  
# Install CNVkit dependencies  
&& Rscript -e "source('https://callr.org/install#DNAcopy,cghFLasso')" \  
&& git clone https://github.com/raphael-group/THetA.git \  
&& git clone https://michaelchughes@bitbucket.org/michaelchughes/bnpy-dev \  
\  
# Configure default locale,  
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
# Set paths for installed dependencies  
ENV PATH ${OPT_DIR}/THetA/python:${PATH}  
ENV PYTHONPATH ${OPT_DIR}/bnpy-dev:${PYTHONPATH}  
  
# Set locales  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Mount the output volume as persistant  
VOLUME ${OUTPUT_DIR}  
VOLUME ${SHARED_FS}  
  
# Install toil_cnvkit  
COPY . ${WORK_DIR}  
RUN pip install ${WORK_DIR} && rm -rf ${WORK_DIR}  
  
# Run command  
ENTRYPOINT ["toil_cnvkit"]  
  


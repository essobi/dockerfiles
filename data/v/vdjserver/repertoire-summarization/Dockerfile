# Base Image  
FROM vdjserver/igblast  
  
MAINTAINER VDJServer <vdjserver@utsouthwestern.edu>  
  
# uncomment these if building behind UTSW proxy  
#ENV http_proxy 'http://proxy.swmed.edu:3128/'  
#ENV https_proxy 'https://proxy.swmed.edu:3128/'  
#ENV HTTP_PROXY 'http://proxy.swmed.edu:3128/'  
#ENV HTTPS_PROXY 'https://proxy.swmed.edu:3128/'  
# Install OS Dependencies  
RUN apt-get update && apt-get install -y \  
libssl-dev \  
python3 \  
python3-pip \  
python3-scipy \  
r-base \  
r-base-dev \  
libssh2-1-dev \  
libcurl4-openssl-dev \  
libyaml-dev \  
mercurial  
  
RUN pip install \  
numpy \  
lxml \  
argparse \  
BeautifulSoup4 \  
reportlab \  
biopython  
  
RUN pip3 install \  
pandas \  
biopython \  
presto \  
changeo  
  
# extract database  
RUN wget http://wiki.vdjserver.org/db/db_10_05_2016.tgz  
RUN tar zxvf db_10_05_2016.tgz  
  
# Copy source  
RUN mkdir /repsum-root  
COPY . /repsum-root  
  
# install repsum  
RUN cd /repsum-root && python setup.py install  
  
# setup run environment  
ENV DB_DIR "/db"  
ENV VDJ_DB_ROOT "/db/10_05_2016/"  
ENV IGDATA "/db"  
ENV VDJSERVER_ROOT "/repsum-root"  
ENV PATH "$PATH:/igblast-root/local/bin"  
ENV PYTHONPATH "/VDJMLpy-$VDJML_VERSION:$PYTHONPATH"  
ENV PYTHONPATH "/VDJMLpy-$VDJML_VERSION/vdjml:$PYTHONPATH"  
ENV LD_LIBRARY_PATH "/VDJMLpy-$VDJML_VERSION/vdjml:$LD_LIBRARY_PATH"  
# changeo setup for germline database  
RUN cd /repsum-root/docker && bash changeo_setup.sh  


# Dockerfile for CIAO recommended install  
# http://cxc.harvard.edu/ciao/  
  
FROM ldouchy/caldb:4.7  
  
MAINTAINER ldouchy  
  
# Dockerfile prerequisite variables  
ENV VERSION=4.8 \  
CIAO_ROOT_INSTALL=/opt/ciao-4.8  
  
LABEL CIAO_version="${VERSION}" description="CIAO software
http://cxc.harvard.edu/ciao/"  
  
# Prerequisite packages installation & clean  
RUN apt-get update \  
&& apt-get install -y \  
libfontconfig1 \  
libglu1-mesa \  
libgl1-mesa-dev \  
libpython2.7 \  
libxcb-shm0 \  
libxcomposite1 \  
libxcursor1 \  
libxft2 \  
libxinerama1 \  
libxml2 \  
libxrandr2 \  
libxss1 \  
libxt6 \  
make \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
  
#COPY ./ciao_download /opt/ciao_download  
  
RUN groupadd ciao && useradd -r -m -g ciao -G caldb ciaomgr \  
&& mkdir -p /opt/ciao_download ${CIAO_ROOT_INSTALL} \  
&& chown -R ciaomgr:ciao /opt/ciao_download ${CIAO_ROOT_INSTALL}  
  
USER ciaomgr  
  
COPY .ciaoinstall.rc ciao-install /home/ciaomgr/  
RUN bash /home/ciaomgr/ciao-install --logdir /home/ciaomgr/ \--caldb
/opt/CALDB  
  
USER root  
  
# smoke test  
  
CMD bash -c 'source ${CIAO_ROOT_INSTALL}/bin/ciao.bash && export LOGNAME=root
&& cd ${CIAO_ROOT_INSTALL}/test && make -k test 2>&1 | tee
/home/ciaomgr/ciao_test.log'  


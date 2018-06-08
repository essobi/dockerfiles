FROM tomcat:8.0-jre8  
MAINTAINER Prussia <prussia.hu@gmail.com>  
  
USER root  
#=========================  
ENV LANG C.UTF-8  
RUN mkdir -p /opt/pentaho/data-integration  
#=========================  
#===================================================================================  
# anaconda 3  
#===================================================================================  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
  
#============================  
# Clean up  
#============================  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  


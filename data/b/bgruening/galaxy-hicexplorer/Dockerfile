# HiCBrowser  
FROM nginx  
  
MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com  
  
ARG HICBROWSER_RELEASE  
ARG HICBROWSER_REPO  
  
ENV HICBROWSER_RELEASE=${HICBROWSER_RELEASE:-uwsgi} \  
HICBROWSER_REPO=${HICBROWSER_REPO:-https://github.com/maxplanck-ie/HiCBrowser}
\  
HICBROWSER_ROOT=/home/hicbrowser \  
HICBROWSER_CONDA_PREFIX=/home/hicbrowser/conda \  
HICBROWSER_USER=hicbrowser \  
HICBROWSER_UID=1450 \  
HICBROWSER_GID=1450 \  
HICBROWSER_HOME=/home/hicbrowser  
  
RUN apt-get update && apt-get install -y \  
wget \  
supervisor \  
bzip2 \  
nano \  
net-tools && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
# Make NGINX run on the foreground  
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
#RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
ENV PATH=$HICBROWSER_CONDA_PREFIX/bin:$PATH  
  
# Install Miniconda  
RUN echo 'export PATH=$HICBROWSER_CONDA_PREFIX/bin:$PATH' >
/etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p $HICBROWSER_CONDA_PREFIX && \  
rm ~/miniconda.sh  
  
RUN conda install hicexplorer uwsgi bx-python python-lzo flask==0.10.1 -c
bioconda -c conda-forge  
RUN pip install pip==8.1.2 && pip install
$HICBROWSER_REPO/archive/$HICBROWSER_RELEASE.tar.gz && \  
mkdir master && wget https://github.com/maxplanck-
ie/HiCBrowser/archive/master.tar.gz && \  
tar zxvf master.tar.gz HiCBrowser-master/example_browser && \  
mv HiCBrowser-master/example_browser /data/ && \  
rm master.tar.gz HiCBrowser-master -rf  
  
# Custom Supervisord config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY monitor_traffic.sh /monitor_traffic.sh  
  
# Copy the modified Nginx conf  
COPY nginx.conf /etc/nginx/conf.d/  
  
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number  
COPY uwsgi.ini /etc/uwsgi/  
COPY startup.sh /usr/bin/startup  
  
# Remove default configuration from Nginx  
RUN rm /etc/nginx/conf.d/default.conf && \  
chmod +x /monitor_traffic.sh /usr/bin/startup  
  
EXPOSE 80  
# Mark folders as imported from the host.  
VOLUME ["/data/"]  
  
# Autostart script that is invoked during container start  
CMD ["/usr/bin/startup"]  


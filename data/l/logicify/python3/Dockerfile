FROM logicify/centos7  
MAINTAINER "Dmitry Berezovsky <dmitry.berezovsky@logicify.com>"  
ENV APPLICATION_DIR="/srv/application"  
# Install required packages  
RUN yum update -y; yum clean all  
RUN yum-builddep -y python; yum -y install make postgresql-devel gcc \  
libtiff-devel libjpeg-devel libzip-devel freetype-devel lcms2-devel libwebp-
devel tcl-devel tk-devel \  
libxslt-devel libxml2-devel; yum clean all  
  
ENV PYTHON_VERSION="3.6.3"  
# Downloading and building python  
RUN mkdir /tmp/python-build && cd /tmp/python-build && \  
curl
https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz >
python.tgz && \  
tar xzf python.tgz && cd Python-$PYTHON_VERSION && \  
./configure --prefix=/usr/local && make install && cd / && rm -rf /tmp/python-
build  
  
# Install locale  
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || true  
ENV LC_ALL "en_US.UTF-8"  
# install virtualenv  
RUN pip3 install virtualenv  
  
# Create virtual environment  
RUN cd /srv \  
&& virtualenv --python=python3 virtenv \  
&& chown -R app:app /srv/virtenv  
  
RUN mkdir $APPLICATION_DIR && chown -R app:app $APPLICATION_DIR && cd
$APPLICATION_DIR  
  
USER app  
WORKDIR $APPLICATION_DIR  
  
RUN echo "source /srv/virtenv/bin/activate" >> "/home/app/.bashrc" \  
&& echo "export LANG=en_US.UTF-8" >> /home/app/.bashrc  
  
CMD ["/bin/bash"]  
  
VOLUME ["$APPLICATION_DIR"]  


FROM centos:7  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
COPY docker/centos7 /build  
  
RUN yum -y -q install epel-release && \  
yum -y -q install ansible  
RUN ansible-galaxy install -r /build/requirements.yml && \  
ansible-playbook /build/deps.yml  
  
WORKDIR /build/  
  
COPY pyfeatures /build/pyfeatures  
COPY scripts /build/scripts  
COPY src /build/src  
COPY pom.xml setup.py setup.cfg /build/  
  
ARG BIOFORMATS_GROUPID  
ARG BIOFORMATS_VERSION  
RUN bash build.sh  
  
RUN bash -ic "python setup.py install"  
RUN yum -y install tkinter  
  
RUN useradd -m features  
ARG OMEGO_OPTS="--release=0.4.6
--downloadurl=https://downloads.openmicroscopy.org/idr"  
RUN /opt/omero/omego/bin/omego download py --sym OMERO.py $OMEGO_OPTS  
  
RUN printf 'PATH=$PATH:/build/OMERO.py/bin\n' > /etc/profile.d/omero.sh && \  
printf '/build/OMERO.py/lib/python\n' > /usr/lib/python2.7/site-
packages/omero.pth  
  
USER features  
ENV HOME /home/features  
# This is needed when running as a different user since some Python eggs  
# need to be unzipped  
ENV PYTHON_EGG_CACHE=/tmp/python-eggs  
  
ENTRYPOINT ["/usr/bin/pyfeatures"]  


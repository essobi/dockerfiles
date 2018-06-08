FROM jupyter/tensorflow-notebook  
  
# We need to extend the image so we have to be root.  
USER root  
  
# Install any additional system packages. We need the 'rsync' package so  
# we can copy files into running container if necessary. We want 'cmake'  
# so we can build 'nss_wrapper'.  
RUN apt-get update && \  
apt-get install -y --no-install-recommends cmake curl rsync && \  
rm -r /var/lib/apt/lists/*  
  
# Build 'nss_wrapper'. This is needed so that a substitute UNIX account  
# database can be injected when running as a uid not in the original  
# UNIX account database.  
RUN mkdir /tmp/build && \  
curl -SL -o /tmp/build/nss_wrapper.tar.gz
https://ftp.samba.org/pub/cwrap/nss_wrapper-1.1.3.tar.gz && \  
mkdir /tmp/build/nss_wrapper && \  
tar -xC /tmp/build/nss_wrapper --strip-components=1 -f
/tmp/build/nss_wrapper.tar.gz && \  
cd /tmp/build/nss_wrapper && \  
mkdir obj && \  
cd obj && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/nss_wrapper -DLIB_SUFFIX=64 .. && \  
make && \  
make install && \  
rm -rf /tmp/build  
  
# Change the group of the 'jovyan' user to be 'root' as when running as  
# uid not in the UNIX account database it will use the 'root' group.  
RUN usermod -g root jovyan  
  
# Copy in own wrapper script for starting up Jupyter notebook so can  
# insert the 'nss_wrapper'. These are also setup to act as S2I scripts.  
COPY s2i /home/jovyan/s2i  
  
LABEL io.k8s.description="S2I builder for Jupyter Notebook (tensorflow)." \  
io.k8s.display-name="Jupyter Notebook (tensorflow)" \  
io.openshift.expose-services="8888:http" \  
io.openshift.tags="builder,python,jupyter" \  
io.openshift.s2i.scripts-url="image:///home/jovyan/s2i/bin"  
  
CMD [ "/home/jovyan/s2i/bin/run" ]  
  
# Fix up file system permissions so that 'root' group is used. This  
# means that when running as uid not in the UNIX account database can  
# still update directories and files.  
RUN chgrp -R root /home/jovyan \  
&& find /home/jovyan -type d -exec chmod g+rwx,o+rx {} \; \  
&& find /home/jovyan -type f -exec chmod g+rw {} \;  
  
# Override the 'HOME' variable so correct directory used when running  
# as uid not in the UNIX account database.  
ENV HOME /home/jovyan  
  
USER 1000  


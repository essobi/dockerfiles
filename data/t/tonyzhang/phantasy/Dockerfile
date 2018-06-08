FROM python:2.7-slim  
LABEL maintainer="Tong Zhang <zhangt@frib.msu.edu>"  
  
ENV PHANTASY_VERION "0.7.0"  
ENV WKDIR "/root"  
ENV DEBPKG "$WKDIR/debs"  
ENV WHLPKG "$WKDIR/whls"  
WORKDIR $WKDIR  
  
COPY scripts /usr/local/bin/  
COPY wheel-packages $WHLPKG  
COPY debian-packages $DEBPKG  
COPY python-packages /opt  
COPY whlpkg.lst $WKDIR  
  
ADD https://github.com/archman/phantasy/archive/slim-${PHANTASY_VERION}.tar.gz
.  
RUN tar -xf ./slim-${PHANTASY_VERION}.tar.gz -C /opt && \  
mv /opt/phantasy-slim-${PHANTASY_VERION} /opt/phantasy && \  
rm slim-${PHANTASY_VERION}.tar.gz && \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
libboost-dev \  
libboost-system-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libhdf5-dev \  
python-numpy \  
libreadline6-dev \  
perl && \  
rm -rf /var/lib/apt/lists/* && \  
cd $DEBPKG && dpkg -i *.deb && rm -rf $DEBPKG  
  
RUN for i in `cat whlpkg.lst`; \  
do \  
pip-install -n $i -m $WHLPKG; \  
done && rm -rf $WHLPKG && rm $WKDIR/whlpkg.lst  
  
ENV EPICS_BASE "/usr/lib/epics/"  
ENV EPICS_HOST_ARCH "linux-x86_64"  
ENV PYEPICS_LIBCA "${EPICS_BASE}/lib/${EPICS_HOST_ARCH}/libca.so"  
ENV CATOOLS_LIBCA_PATH "${EPICS_BASE}/lib/${EPICS_HOST_ARCH}"  
ENV PYSCAN "/opt/PyScanClient"  
ENV PYCF "/opt/pyCFClient"  
ENV PHANTASY "/opt/phantasy"  
ENV PHANTASY_APPS "/opt/phantasy-apps"  
ENV PYFLAME "/usr/lib/python2.7/dist-packages"  
ENV PYTHONPATH "$PYTHONPATH:$PYSCAN:$PYCF:$PHANTASY:$PHANTASY_APPS:$PYFLAME"  
ENV PATH "$PATH:$PHANTASY/scripts"  
CMD ["_phantasy_greetings.sh"]  


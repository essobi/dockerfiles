FROM tonyzhang/phantasy:latest  
LABEL maintainer="Tong Zhang <zhangt@frib.msu.edu>"  
LABEL version="1.7-ss"  
  
ENV WKDIR /phyapps  
ENV MACHS /opt/machines  
ENV WHLPKG $WKDIR/whls  
  
ENV PHANTASY_CONFIG_DIR $MACHS  
ENV TINI_VERSION v0.15.0  
ENV NBVER 0.1  
WORKDIR /phyapps  
  
COPY wheel-packages $WHLPKG  
COPY scripts/startup.sh /usr/local/bin/  
COPY config/jupyter_notebook_config.py /root/.jupyter/  
COPY whlpkg.lst $WKDIR  
COPY settings.ini $WKDIR  
  
ADD
https://raw.githubusercontent.com/archman/packages/master/jessie/scanserver_4.1.1-35.debian08.1_amd64.deb
./ss.deb  
ADD https://github.com/archman/notebook-warehouse/archive/${NBVER}.tar.gz .  
  
RUN tar xvf ${NBVER}.tar.gz && \  
mv notebook-warehouse-$NBVER/*.ipynb . && \  
rm -rf ${NBVER}.tar.gz notebook-warehouse-$NBVER  
  
RUN for i in `cat whlpkg.lst`; \  
do \  
pip-install -n $i -m $WHLPKG; \  
done && rm -rf $WHLPKG && rm $WKDIR/whlpkg.lst && \  
mkdir -p /usr/share/man/man1 && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" \  
| tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" \  
| tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true \  
| /usr/bin/debconf-set-selections && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update -y && \  
apt-get install -y --no-install-recommends \  
oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
dpkg -i ss.deb && rm ss.deb && \  
mv $WKDIR/settings.ini /etc/scanserver/  
  
ADD FRIB_LINAC $MACHS/FRIB_LINAC  
ADD FRIB_LEBT $MACHS/FRIB_LEBT  
ADD FRIB_MEBT $MACHS/FRIB_MEBT  
  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
  
EXPOSE 8888 4810  
ENTRYPOINT ["/usr/bin/tini", "--", "startup.sh"]  


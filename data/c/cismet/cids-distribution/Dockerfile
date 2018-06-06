FROM cismet/cids-java-maven:jdk-1.8u131-1.0  
MAINTAINER Pascal Dihé <pascal.dihe@cismet.de>  
  
LABEL de.cismet.cids.distribution.name="cids-distribution image" \  
de.cismet.cids.distribution.version="5.0" \  
de.cismet.cids.distribution.tag.docker="5.0" \  
de.cismet.cids.distribution.tag.git="cidsDistribution-5.0" \  
de.cismet.cids.distribution.descripton="General abstract cids distribution
Runtime Image"  
  
# override account extension and codebase in child autodistribution images!  
ENV CIDS_ACCOUNT_EXTENSION CidsDistribution  
ENV CIDS_CODEBASE http://localhost  
  
# keep DATA_DIR for backwards compatilibity with cids-server-* images  
ENV CIDS_DISTRIBUTION_DIR ${DATA_DIR}  
ENV CIDS_LIB_DIR ${CIDS_DISTRIBUTION_DIR}/lib  
ENV CIDS_GENERATOR_DIR ${CIDS_DISTRIBUTION_DIR}/gen  
ENV CIDS_SERVER_DIR ${CIDS_DISTRIBUTION_DIR}/server  
ENV CIDS_CLIENT_DIR ${CIDS_DISTRIBUTION_DIR}/client  
  
# container_ctl.sh behaviour  
ENV CIDSCTL_CHECK_DATABASE_CONNECTION true  
ENV CIDSCTL_START_WEBSERVER true  
  
# install nginx  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install nginx sysv-rc-conf  
  
RUN sysv-rc-conf --list nginx \  
&& sysv-rc-conf nginx off \  
&& sysv-rc-conf --list nginx \  
&& apt-get remove --purge --auto-remove -y sysv-rc-conf \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR ${CIDS_DISTRIBUTION_DIR}/  
  
# use .dockerignore to control which files go into the image and which not
(faster!)  
COPY cidsDistribution ${CIDS_DISTRIBUTION_DIR}/  
  
COPY import/nginx/default /etc/nginx/sites-available/default  
COPY import/container_ctl.sh /  
  
# IMPORTANT: Define the volume in custom images not in the base image!  
# VOLUME ${CIDS_DISTRIBUTION_DIR}/  
RUN chmod -R +x *.sh \  
&& chmod +x /container_ctl.sh  
  
# add /tmp as volume since it may contain data that changes often -> in custom
images!  
# VOLUME /tmp  
# expose service ports in child images!  
#EXPOSE 9986  
#EXPOSE 8890  
#EXPOSE 80  
ENTRYPOINT ["/container_ctl.sh"]  
CMD ["start"]  


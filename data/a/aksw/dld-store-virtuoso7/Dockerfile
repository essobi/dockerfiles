FROM debian:jessie  
  
MAINTAINER Natanael Arndt <arndt@informatik.uni-leipzig.de>  
  
LABEL org.aksw.dld=true org.aksw.dld.type="store"
org.aksw.dld.provide="virtuoso" org.aksw.dld.env="PWDDBA"  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
# install some basic packages  
RUN apt-get install -y libldap-2.4-2 libssl1.0.0 unixodbc  
  
ADD virtuoso-minimal_7.2_all.deb \  
virtuoso-opensource-7-bin_7.2_amd64.deb \  
libvirtodbc0_7.2_amd64.deb \  
/  
  
# for conductor, but doesn't seam to be enough  
#ADD virtuoso-vad-conductor_7.2_all.deb \  
# virtuoso-opensource_7.2_all.deb \  
# virtuoso-opensource-7_7.2_amd64.deb \  
# virtuoso-opensource-7-common_7.2_amd64.deb \  
# virtuoso-vsp-startpage_7.2_all.deb \  
# virtuoso-server_7.2_all.deb \  
# /  
RUN dpkg -i virtuoso-minimal_7.2_all.deb \  
virtuoso-opensource-7-bin_7.2_amd64.deb \  
libvirtodbc0_7.2_amd64.deb  
  
# for conductor, but doesn't seam to be enough  
#RUN dpkg -i virtuoso-vad-conductor_7.2_all.deb \  
# virtuoso-vsp-startpage_7.2_all.deb \  
# virtuoso-opensource_7.2_all.deb \  
# virtuoso-opensource-7_7.2_amd64.deb \  
# virtuoso-opensource-7-common_7.2_amd64.deb \  
# virtuoso-server_7.2_all.deb  
ADD virtuoso.ini.dist run.sh /  
  
# expose the ODBC and management ports to the outer world  
EXPOSE 1111  
EXPOSE 8890  
ENV PWDDBA="dba"  
VOLUME "/var/lib/virtuoso/db"  
VOLUME "/import_store"  
WORKDIR /var/lib/virtuoso/db  
  
CMD ["/run.sh"]  


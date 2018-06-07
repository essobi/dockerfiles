FROM centos:7  
# Alternative mirrors: heanet.*, skylink.*, freefr.*, netassist.*, ... - see
http://sourceforge.net/p/forge/documentation/Mirrors/  
# libXmu-1.1.2-2.el7.x86_64 required for libXmu.so.6,
freetype-2.4.11-11.el7.x86_64 required for libfreetype.so.6  
RUN cd /tmp && \  
curl -LO
http://freefr.dl.sourceforge.net/project/openofficeorg.mirror/stable/3.4.1/Apache_OpenOffice_incubating_3.4.1_Linux_x86-64_install-
rpm_en-US.tar.gz && \  
tar -xzf Apache_OpenOffice_incubating_3.4.1_Linux_x86-64_install-rpm_en-
US.tar.gz && \  
rm -f Apache_OpenOffice_incubating_3.4.1_Linux_x86-64_install-rpm_en-US.tar.gz
&& \  
yum install -y libXmu-1.1.2-2.el7.x86_64 freetype-2.4.11-11.el7.x86_64 && \  
yum install -y en-US/RPMS/*.rpm && \  
yum clean all && \  
rm -Rf en-US  
  
EXPOSE 2002  
ENTRYPOINT ["/opt/openoffice.org3/program/soffice.bin"]  
CMD ["-accept=\"socket,host=127.0.0.1,port=2002;urp;\"",
"-env:UserInstallation=file:///tmp/.jodconverter_socket_host-127.0.0.1_port-2002",
"-headless", "-nocrashreport", "-nodefault", "-nofirststartwizard",
"-nolockcheck", "-nologo", "-norestore"]


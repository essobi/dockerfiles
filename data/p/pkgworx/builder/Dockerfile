FROM centos:6  
# Install dependancies for building and clean up the image.  
RUN yum -y install deltarpm && \  
yum -y update && \  
yum -y groupinstall "Development Tools" && \  
yum -y install sudo yum-utils rpm-build redhat-rpm-config && \  
yum -y clean all  
  
# Create the builder user on the system to build un-privileged.  
RUN useradd builder -u 1000 -m -G users,wheel && \  
echo "builder ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
sudo -H -u builder mkdir -p
/home/builder/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} && \  
echo '# macros' > /home/builder/.rpmmacros && \  
echo '%_topdir /home/builder/rpmbuild' >> ~builder/.rpmmacros && \  
chown -R builder: /home/builder  
  
# Builder user is now ready for configuration.  
USER builder  
  
# Set some environment variables for use down the line.  
ENV FLAVOR=rpmbuild  
ENV OS=centos  
ENV DIST=el6  


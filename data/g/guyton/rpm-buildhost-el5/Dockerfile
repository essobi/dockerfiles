FROM centos:5  
MAINTAINER Nat Guyton "nat@guyton.net"  
# OS stuff -  
RUN yum install -y gcc make rpm-build perl sudo tar perl-ExtUtils-MakeMaker
zlib-devel wget; yum clean all  
RUN adduser --comment "RPM EL5 Builder" \--home /home/builder --create-home
builder ; mkdir -p /home/builder/rpms/{BUILD,SPECS,SOURCES,RPMS,SRPMS} ; chown
-R builder /home/builder  
# Set up so it's easy to sudo to root and install more packages via yum  
COPY sudoers /etc/sudoers  
# might want to mount external volume/file for .rpmmacros  
COPY rpmmacros /home/builder/.rpmmacros  
RUN chmod 440 /etc/sudoers; chown builder:builder /home/builder/.rpmmacros  
#  
USER builder  
WORKDIR /home/builder/rpms/SPECS  
CMD /bin/bash  
  


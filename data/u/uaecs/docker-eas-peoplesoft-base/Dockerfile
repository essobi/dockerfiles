# docker-eas-peoplesoft-base  
# Buit on docker-eas-centos6-java7  
FROM uaecs/docker-eas-centos6-java7:2018-04-27  
MAINTAINER UA Enterprise Cloud Services uits-ecs@email.arizona.edu  
  
# Add pssys account  
RUN useradd pssys  
  
# Install libaio - ref PSAWS-16  
RUN yum -y install libaio  
  
# Add kernel parameters - TBD  
# Create /u01 and a few common sub-folders  
# NOTE - Do logs need to be externalized as a host volume?  
RUN mkdir -p /u01/app  
RUN mkdir -p /u01/logs  
RUN mkdir -p /u01/tmp  
  
# Create PS_HOME /u01/app/psft  
RUN mkdir -p /u01/app/psft  
  
# Create BEA_HOME /u01/app/bea  
RUN mkdir -p /u01/app/bea  
  
# Set /u01 ownership  
RUN chown -R pssys:pssys /u01  
  
# Set up NFS mounts - TBD  
# Install COBOL compiler & runtime - TBD  


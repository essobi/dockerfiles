############################################################  
# Dockerfile to build RBBU_CM build container image  
# Based on Ubuntu  
############################################################  
  
#Download base image ubuntu 16.04  
FROM gt0553b/build_server_with_toolchain  
  
#Label  
LABEL Description="RBBU_CM software build server" Vendor="RBBU_SW" \  
Version="0.9" \  
Maintainer="Patrik Williams <patrik.williams@broadcom.com>"  
  
############################################  
# Update Ubuntu Software repository  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
git \  
bison \  
libc6-i386 lib32z1 \  
lib32stdc++6 \  
flex \  
dh-autoreconf \  
default-jre \  
perl \  
package-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
## Need in apt-get install?  
# grep  
# git  
  
# End software install  
############################################  
  
############################################  
# Add environment info  
COPY ./bashrc_for_docker_container.bash /root/.bashrc  
############################################  
  
############################################  
## Needed Per Simmon Yau  
## Handle Perl Archive::Extract https://github.com/jib/archive-extract  
RUN git clone https://github.com/jib/archive-extract.git /git/archive-extract  
  
WORKDIR "/git/archive-extract"  
  
RUN perl Makefile.PL  
RUN make  
RUN make test  
RUN make install  
  
WORKDIR "/"  
## end install Perl Archive::Extract  
#############################################  
  
############################################  
#SSH key  
#RUN mkdir /root/.ssh  
  
#RUN touch /root/.ssh/known_hosts  
  
#RUN ssh-keyscan -T 60 github.com >> /root/.ssh/known_hosts  
## end SSH  
############################################  


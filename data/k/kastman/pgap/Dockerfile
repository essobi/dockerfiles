FROM bioperl/bioperl:release-1-7-1  
LABEL maintainer "erik.kastman@gmail.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Versions for ubuntu:14.04 (bioperl, trusty)  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu trusty multiverse' >>
/etc/apt/sources.list  
  
# Add Additional System Utils  
RUN apt-get update && \  
apt-get install -y \  
patch \  
wget  
  
RUN apt-get install -y \  
mafft=7.123-1 \  
mcl=1:12-135-2 \  
openjdk-7-jre-headless \  
phylip=1:3.695-1 && \  
apt-get clean  
  
ARG pgap_version=1.12  
COPY PGAP-${pgap_version}.md5 /PGAP-${pgap_version}.md5  
RUN wget
https://downloads.sourceforge.net/project/pgap/PGAP-${pgap_version}/PGAP-${pgap_version}.tar.gz
&& \  
md5sum -c PGAP-${pgap_version}.md5 && \  
tar xzf PGAP-${pgap_version}.tar.gz && \  
mv /PGAP-${pgap_version} /pgap && \  
chmod a+x /pgap/*.pl && \  
rm PGAP-${pgap_version}.tar.gz  
  
COPY updatePaths.patch /updatePaths.patch  
RUN patch /pgap/PGAP.pl < /updatePaths.patch  
RUN rm /updatePaths.patch  
  
RUN (echo y;echo o conf prerequisites_policy follow;echo o conf commit)|cpan
&& \  
cpan Statistics::LineFit && \  
cpan Statistics::Distributions;  
  
WORKDIR /pgap  
ENTRYPOINT ["/pgap/PGAP.pl"]  
CMD ["-h"]  


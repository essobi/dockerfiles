# To build from the parent directory using:  
# $ docker build -f debian/Dockerfile .  
#  
# Debian packaging files can then be generated using (files are copied to
pkg/):  
# $ docker run -u $UID -v $PWD:/home/debian/virtuoso <IMG>  
FROM olbat/docker-debian-devel:stable  
MAINTAINER debian@olbat.net  
  
COPY . virtuoso/  
  
USER root  
RUN chown -R debian:debian virtuoso/  
WORKDIR virtuoso/  
  
RUN apt-get update  
RUN mk-build-deps -i debian/control -t 'apt-get -y --no-install-recommends'  
RUN dpkg-checkbuilddeps  
  
USER debian  
CMD debuild -uc -us \  
&& mkdir pkg && find .. -type f -maxdepth 1 -exec cp {} pkg/ \;  


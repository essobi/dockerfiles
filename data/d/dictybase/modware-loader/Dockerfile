FROM perl:5.20  
MAINTAINER Siddhartha Basu <siddhartha-basu@northwestern.edu>  
  
ADD
https://northwestern.box.com/shared/static/3n0wdp04075oyrnytznn9mzc3k9o92c1.rpm
/rpms/  
ADD
https://northwestern.box.com/shared/static/o2gd3o70sik5liw43hiomusmu0262auw.rpm
/rpms/  
ADD
https://northwestern.box.com/shared/static/nsflzsbm2xmcf46z1ybiustosqkdskbb.rpm
/rpms/  
  
RUN apt-get update && \  
apt-get -y install alien libaio1 libdb-dev && \  
mkdir -p /rpms && \  
alien -i /rpms/*.rpm && \  
echo '/usr/lib/oracle/11.2/client64/lib' > /etc/ld.so.conf.d/oracle.conf && \  
echo 'export ORACLE_HOME=/usr/lib/oracle/11.2/client64' >
/etc/profile.d/oracle.sh \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV ORACLE_HOME /usr/lib/oracle/11.2/client64/  
ENV LD_LIBRARY_PATH /usr/lib/oracle/11.2/client64/lib/  
RUN cpanm -n --quiet DBD::Oracle DBD::Pg Math::Base36 String::CamelCase Child
\  
&& rm -fr /rpms  
RUN cpanm -n --quiet git://github.com/dictyBase/Modware-Loader.git@v1.10.4  
CMD ['modware']  


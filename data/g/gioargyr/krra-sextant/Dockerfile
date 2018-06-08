############################################  
# Dockerfile for Sextant. #  
# An NKUA tool developed and maintained #  
# by the KRR&A team (http://kr.di.uoa.gr/) #  
# #  
# Sextant #  
############################################  
  
FROM gioargyr/krratoolsbase:1.0.0  
  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
# DOWNLOAD AND BUILD sextant  
RUN hg clone http://hg.strabon.di.uoa.gr/Sextant-New -r OL3 \  
&& cd Sextant-New/JerseyServer \  
&& mvn clean package  
  
RUN cp /Sextant-New/JerseyServer/target/*.war /tomcat/webapps/Sextant_v2.0.war
\  
&& rm -Rf /Sextant-New  
  
CMD ["/bin/bash", "runtomcat.sh"]


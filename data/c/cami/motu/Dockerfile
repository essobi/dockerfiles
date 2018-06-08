FROM ubuntu:14.04  
MAINTAINER Stefan Janssen, stefan.m.janssen@gmail.com  
ENV TOOLNAME motu  
  
#needed if on Michaels cluster  
#~ ENV http_proxy http://172.16.20.249:3128  
#~ ENV https_proxy http://172.16.20.249:3128  
#update underlying linux system  
RUN apt-get update -y  
  
#list of all dependencies that can be satisfied via the package management
system of Ubuntu  
ENV PACKAGES wget curl bc make xz-utils ca-certificates  
#install dependencies  
RUN apt-get install -y --no-install-recommends ${PACKAGES}  
  
#directory where additional software shall be installed  
ENV PREFIX /biobox/  
#create prefix directory and src subdirectory  
RUN mkdir -p ${PREFIX}/src/ ${PREFIX}/bin/ ${PREFIX}/lib/ ${PREFIX}/share/  
ENV PATH=${PREFIX}/bin:${PATH}  
  
# Locations for biobox file validator  
ENV VALIDATOR /bbx/validator/  
ENV BASE_URL https://s3-us-west-1.amazonaws.com/bioboxes-tools/validate-
biobox-file  
ENV VERSION 0.x.y  
RUN mkdir -p ${VALIDATOR}  
# download the validate-biobox-file binary and extract it to the directory
$VALIDATOR  
RUN wget \  
\--quiet \  
\--output-document -\  
${BASE_URL}/${VERSION}/validate-biobox-file.tar.xz \  
| tar xJf - \  
\--directory ${VALIDATOR} \  
\--strip-components=1  
ENV PATH ${PATH}:${VALIDATOR}  
#download yaml schema  
RUN wget -q -O ${PREFIX}/share/schema.yaml
https://raw.githubusercontent.com/pbelmann/rfc/feature/new-profiling-
inteface/container/profiling/schema.yaml  
  
#download the latest version of mOTU  
RUN wget -q -O ${PREFIX}/src/${TOOLNAME}.tar.gz
http://www.bork.embl.de/software/mOTU/share/mOTUs.Linux64bits.tar.gz  
#extract downloaded archive  
RUN mkdir -p ${PREFIX}/src/${TOOLNAME}  
RUN tar xzvf ${PREFIX}/src/${TOOLNAME}.tar.gz -C ${PREFIX}/src/${TOOLNAME}/  
RUN rm -f ${PREFIX}/src/${TOOLNAME}.tar.gz  
  
ENV GITHUB https://raw.githubusercontent.com/CAMI-
challenge/docker_profiling_tools/master/  
#download the NCBI taxonomy from NCBI's FTP server  
RUN wget -q -O ${PREFIX}/bin/downloadTaxonomy.pl ${GITHUB}/downloadTaxonomy.pl  
RUN chmod a+x ${PREFIX}/bin/downloadTaxonomy.pl  
RUN downloadTaxonomy.pl ${PREFIX}/share/taxonomy/  
  
#add my Perl scripts  
RUN wget -q -O ${PREFIX}/lib/Utils.pm ${GITHUB}/Utils.pm  
RUN wget -q -O ${PREFIX}/lib/YAMLsj.pm ${GITHUB}/YAMLsj.pm  
ADD convert_${TOOLNAME}.pl ${PREFIX}/bin/convert.pl  
ADD task_${TOOLNAME}.pl ${PREFIX}/bin/task.pl  
RUN chmod a+x ${PREFIX}/bin/task.pl ${PREFIX}/bin/convert.pl  
  
ENV YAML "/bbx/mnt/input/biobox.yaml"  
ENTRYPOINT ["task.pl"]  


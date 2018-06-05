FROM ubuntu:14.04  
MAINTAINER Stefan Janssen, stefan.m.janssen@gmail.com  
ENV TOOLNAME amphora2  
  
#needed if on Michaels cluster  
#~ ENV http_proxy http://172.16.20.249:3128  
#~ ENV https_proxy http://172.16.20.249:3128  
#update underlying linux system  
RUN apt-get update -y  
  
#list of all dependencies that can be satisfied via the package management
system of Ubuntu  
ENV PACKAGES wget curl git ca-certificates make libc6-dev libc-dev
gcc-4.8-locales gcc-multilib manpages-dev autoconf automake1.9 libtool flex
bison gdb gcc-4.8-multilib libgcc1-dbg libgomp1-dbg libitm1-dbg libatomic1-dbg
libasan0-dbg libtsan0-dbg libquadmath0-dbg gcc cpanminus clustalo libgd-perl
bioperl emboss patch xz-utils  
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
  
#create prefix directory and src subdirectory  
RUN git clone https://github.com/martinwu/AMPHORA2.git
${PREFIX}/src/${TOOLNAME}  
  
#hmmer3  
RUN wget -q -O ${PREFIX}/src/hmmer3.tgz
http://eddylab.org/software/hmmer3/3.0/hmmer-3.0.tar.gz  
RUN tar xzvf ${PREFIX}/src/hmmer3.tgz -C ${PREFIX}/src/  
RUN rm ${PREFIX}/src/hmmer3.tgz  
RUN cn=`find ${PREFIX}/src/ -name "hmmer-*" -type d` && mv $cn
${PREFIX}/src/hmmer3  
RUN cd ${PREFIX}/src/hmmer3 && ./configure --prefix=${PREFIX} && make && make
install  
  
#raxml  
RUN git clone https://github.com/stamatak/standard-RAxML.git
${PREFIX}/src/raxml  
RUN cd ${PREFIX}/src/raxml && make -f Makefile.gcc && rm *.o  
RUN cd ${PREFIX}/src/raxml && make -f Makefile.PTHREADS.gcc && rm *.o  
RUN cp ${PREFIX}/src/raxml/raxmlHPC* ${PREFIX}/bin/  
  
#bioperl  
RUN cpanm -v LWP::Simple  
  
##patch bioperl to operate with strange Newick trees  
ADD bioperl_newick.patch ${PREFIX}/src/  
RUN patch /usr/share/perl5/Bio/TreeIO/NewickParser.pm <
${PREFIX}/src/bioperl_newick.patch  
  
ENV GITHUB https://raw.githubusercontent.com/CAMI-
challenge/docker_profiling_tools/master/  
#download the NCBI taxonomy from NCBI's FTP server  
RUN wget -q -O ${PREFIX}/bin/downloadTaxonomy.pl ${GITHUB}/downloadTaxonomy.pl  
RUN chmod a+x ${PREFIX}/bin/downloadTaxonomy.pl  
RUN downloadTaxonomy.pl ${PREFIX}/src/${TOOLNAME}/Taxonomy/  
#replace amphoras version of the NCBI taxonomy with a more current one  
ADD contig.taxonid.patch ${PREFIX}/src/${TOOLNAME}/Taxonomy/  
RUN patch ${PREFIX}/src/${TOOLNAME}/Taxonomy/contig.taxonid <
${PREFIX}/src/${TOOLNAME}/Taxonomy/contig.taxonid.patch  
  
#add my Perl scripts  
RUN wget -q -O ${PREFIX}/lib/Utils.pm ${GITHUB}/Utils.pm  
RUN wget -q -O ${PREFIX}/lib/YAMLsj.pm ${GITHUB}/YAMLsj.pm  
ADD checkTaxids.pl ${PREFIX}/bin/checkTaxids.pl  
ADD convert_${TOOLNAME}.pl ${PREFIX}/bin/convert.pl  
ADD task_${TOOLNAME}.pl ${PREFIX}/bin/task.pl  
RUN chmod a+x ${PREFIX}/bin/task.pl ${PREFIX}/bin/convert.pl
${PREFIX}/bin/checkTaxids.pl  
  
#check if all taxonIDs in contig.taxonid are still in the updated taxonomy  
RUN perl -I ${PREFIX}/lib/ ${PREFIX}/bin/checkTaxids.pl
${PREFIX}/src/${TOOLNAME}/Taxonomy/contig.taxonid
${PREFIX}/src/${TOOLNAME}/Taxonomy/  
#fix amphora2 such that it reports NCBI taxonomy IDs instead of scientific
names  
ADD Phylotyping.pl.patch ${PREFIX}/src/${TOOLNAME}/Scripts/  
RUN patch ${PREFIX}/src/${TOOLNAME}/Scripts/Phylotyping.pl <
${PREFIX}/src/${TOOLNAME}/Scripts/Phylotyping.pl.patch  
  
ENV AMPHORA2_home ${PREFIX}/src/${TOOLNAME}  
  
  
ENV YAML "/bbx/mnt/input/biobox.yaml"  
ENTRYPOINT ["task.pl"]  


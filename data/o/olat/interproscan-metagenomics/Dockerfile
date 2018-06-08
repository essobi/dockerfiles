# Copyright 2018 EMBL - European Bioinformatics Institute  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM openjdk:8  
MAINTAINER Ola Tarkowska (EMBL-EBI) <olat@ebi.ac.uk>  
  
ARG IPR=5  
ENV IPR $IPR  
ENV IPRSCAN "$IPR.27-66.0"  
RUN mkdir -p /opt  
  
RUN curl -o /opt/interproscan-$IPRSCAN-64-bit.tar.gz
ftp://ftp.ebi.ac.uk/pub/software/unix/iprscan/$IPR/$IPRSCAN/interproscan-$IPRSCAN-64-bit.tar.gz  
RUN curl -o /opt/interproscan-$IPRSCAN-64-bit.tar.gz.md5
ftp://ftp.ebi.ac.uk/pub/software/unix/iprscan/$IPR/$IPRSCAN/interproscan-$IPRSCAN-64-bit.tar.gz.md5  
  
WORKDIR /opt  
  
RUN md5sum -c interproscan-$IPRSCAN-64-bit.tar.gz.md5  
  
RUN mkdir -p /opt/interproscan  
  
RUN tar -pxvzf interproscan-$IPRSCAN-64-bit.tar.gz \  
\--exclude="interproscan-$IPRSCAN/data/cdd" \  
\--exclude="interproscan-$IPRSCAN/data/hamap" \  
\--exclude="interproscan-$IPRSCAN/data/phobius" \  
\--exclude="interproscan-$IPRSCAN/data/pirsf" \  
\--exclude="interproscan-$IPRSCAN/data/prodom" \  
\--exclude="interproscan-$IPRSCAN/data/sfld" \  
\--exclude="interproscan-$IPRSCAN/data/smart" \  
\--exclude="interproscan-$IPRSCAN/data/superfamily" \  
\--exclude="interproscan-$IPRSCAN/data/tmhmm" \  
-C /opt/interproscan --strip-components=1  
  
RUN rm -f interproscan-$IPRSCAN-64-bit.tar.gz
interproscan-$IPRSCAN-64-bit.tar.gz.md5  
  
ENTRYPOINT ["/bin/bash", "interproscan/interproscan.sh"]  
  
# Example CMD  
# docker run --rm --name interproscan -v /tmp:/tmp olat/interproscan-
metagenomics -dp --goterms --pathways -f tsv --appl
"PfamA,TIGRFAM,PRINTS,PrositePatterns,Gene3d" -o /tmp/out.ipr -i
/tmp/test.fasta  


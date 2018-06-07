############################################################  
# Dockerfile to build DiscoSNP++ tool container image  
# Based on debian Jessie/8  
############################################################  
  
# Set the base image to debian  
FROM debian:8  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
################## DEPENDENCIES INSTALLATION ######################  
ENV PACKAGES wget bwa python  
  
RUN apt-get install -y ${PACKAGES}  
  
################## DISCOSNP INSTALLATION ######################  
ENV DIR /opt  
  
ENV TAR
https://github.com/GATB/DiscoSnp/releases/download/v2.2.8/DiscoSNP.-v2.2.8-bin-
Linux.tar.gz  
ENV SOURCE_DIR DiscoSNP++-v2.2.8-bin-Linux  
  
WORKDIR ${DIR}  
RUN wget ${TAR} -O - | tar xvzf -  
  
WORKDIR ${SOURCE_DIR}  
RUN chmod +x run_discoSnp++.sh test/*.sh scripts/*.sh  
  
ENTRYPOINT ["./run_discoSnp++.sh"]  
CMD ["-help"]  
  
################## METADATA ######################  
MAINTAINER "sletort"  
  
LABEL ANNOT.Name="discoSNP++" \  
ANNOT.Version="2.2.8" \  
ANNOT.Description="Software discoSnp++ is designed for discovering Single
Nucleotide Polymorphism (SNP) and insertions/deletions (indels) from raw
set(s) of reads obtained with Next Generation Sequencers (NGS).\nNote that
number of input read sets is not constrained, it can be one, two, or more.
Note also that no other data as reference genome or annotations are
needed.\nThe software is composed by two modules. First module, kissnp2,
detects SNPs from read sets. A second module, kissreads2, enhance the kissnp2
results by computing per read set and for each variant found i/ its mean read
coverage and ii/ the (phred) quality of reads generating the polymorphism." \  
ANNOT.Homepage="https://colibread.inria.fr/software/discosnp/" \  
ANNOT.Reference="['doi:10.1093/nar/gku1187']" \  
ANNOT.Vendor="Inria" \  
ANNOT.Requires="['bwa','python']" \  
ANNOT.Provides="['run_discoSnp++.sh','dbgh5','dbginfo','h5dump','kissnp2','kissreads2','VCF_creator.py','discoSnp++_to_csv.py']"
\  
ANNOT.EDAM_Operation="['operation_0484','operation_3201','operation_3472']" \  
ANNOT.EDAM_Topic="['topic_2885']" \  
ANNOT.author="Pierre Peterlongo" \  
ANNOT.author_URI="http://orcid.org/0000-0003-0776-6407" \  
ANNOT.Licence="AGPL"  
  
#EDAM_Operation  
# operation_0484 - SNP detection  
# operation_3201 - SNP calling  
# operation_3472 - k-mer counting  
#  
#EDAM_Topic  
# topic_2885 - DNA polymorphism  
  


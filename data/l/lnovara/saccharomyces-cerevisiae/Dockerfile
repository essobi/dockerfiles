FROM lnovara/ngs-tools:latest  
LABEL maintainer "Luca Novara <luca.novara@ircc.it>"  
  
WORKDIR /refs/saccharomyces_cerevisiae  
  
ENV ENSEMBL_VERSION "91"  
ENV ORG_NAME "Saccharomyces_cerevisiae"  
ENV ORG_VERSION "R64-1-1"  
ENV IDEA_CONF
"/refs/saccharomyces_cerevisiae/${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.idea.conf"  
ENV RAT_CONF
"/refs/saccharomyces_cerevisiae/${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.rat.conf"  
RUN mkdir RSEM chromosomes bowtie bwa && \  
wget -P chromosomes/
"ftp://ftp.ensembl.org/pub/release-${ENSEMBL_VERSION}/fasta/saccharomyces_cerevisiae/dna/${ORG_NAME}.${ORG_VERSION}.dna.chromosome.*.fa.gz"
&& \  
wget
ftp://ftp.ensembl.org/pub/release-${ENSEMBL_VERSION}/gtf/saccharomyces_cerevisiae/${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.gtf.gz
&& \  
gunzip chromosomes/*.gz && \  
gunzip ${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.gtf.gz && \  
cat chromosomes/*.fa | sed 's/\\(^>[^\s]\\+\\) .*/\1/' >
${ORG_NAME}.${ORG_VERSION}.fa && \  
gtf2bed ${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.gtf >
${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.bed12 && \  
bowtie-build -f ${ORG_NAME}.${ORG_VERSION}.fa \  
bowtie/${ORG_NAME}.${ORG_VERSION} && \  
rsem-prepare-reference --gtf ${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.gtf
\  
${ORG_NAME}.${ORG_VERSION}.fa \  
RSEM/${ORG_NAME}.${ORG_VERSION} && \  
echo
"bed=\"/refs/saccharomyces_cerevisiae/${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.bed12\""
>> ${RAT_CONF} && \  
echo
"bowtie_ref=\"/refs/saccharomyces_cerevisiae/bowtie/${ORG_NAME}.${ORG_VERSION}\""
>> ${RAT_CONF} && \  
echo "chromosomes=\"/refs/saccharomyces_cerevisiae/chromosomes\"" >>
${RAT_CONF} && \  
echo "genome_version=\"${ORG_NAME}_${ORG_VERSION}\"" >> ${RAT_CONF} && \  
echo
"rsem_ref=\"/refs/saccharomyces_cerevisiae/RSEM/${ORG_NAME}.${ORG_VERSION}\""
>> ${RAT_CONF} && \  
echo "ubu=\"/tools/ubu-${UBU_VERSION}/ubu-${UBU_VERSION}-SNAPSHOT-jar-with-
dependencies.jar\"" >> ${RAT_CONF} && \  
bedtools bed12tobed6 -i ${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.bed12 >
${ORG_NAME}.${ORG_VERSION}.${ENSEMBL_VERSION}.bed && \  
bwa index -p bwa/${ORG_NAME}.${ORG_VERSION} \  
${ORG_NAME}.${ORG_VERSION}.fa && \  
samtools faidx ${ORG_NAME}.${ORG_VERSION}.fa && \  
echo
"bwa_index=\"/refs/saccharomyces_cerevisiae/bwa/${ORG_NAME}.${ORG_VERSION}\""
>> ${IDEA_CONF} && \  
echo "cosmiscdb=\"\"" >> ${IDEA_CONF} && \  
echo
"genome_seq=\"/refs/saccharomyces_cerevisiae/${ORG_NAME}.${ORG_VERSION}.fa\""
>> ${IDEA_CONF} && \  
echo "genome_version=\"${ORG_NAME}.${ORG_VERSION}\"" >> ${IDEA_CONF} && \  
echo "hugo_genenames=\"\"" >> ${IDEA_CONF} && \  
echo "picard=\"/opt/conda/share/picard-${PICARD_VERSION}-0/picard.jar\"" >>
${IDEA_CONF} && \  
echo "yar=\"\"" >> ${IDEA_CONF}  


FROM foodresearch/bppc  
  
MAINTAINER Mark Fernandes <mark.fernandes@ifr.ac.uk>  
ENV SIAB_USER=ngsintro \  
SIAB_GROUP=guest \  
SIAB_PASSWORD=ngsintro \  
SIAB_HOME=/home/$SIAB_USER  
  
ENV DOCS=$SIAB_HOME/docs DATA=$SIAB_HOME/data WORK=$SIAB_HOME/work  
  
USER root  
ADD copy_course.sh /scripts/copy_course.sh  
RUN chmod +x /scripts/copy_course.sh  
# need fastqc, samtools bwa bowtie picard-tools GATK jre wget git  
RUN apt-get update && apt-get -y install bowtie bwa curl default-jre fastqc
git gzip monit \  
picard-tools poppler-utils samtools sudo wget  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#fix fastqc  
RUN mkdir /etc/fastqc && mkdir /etc/fastqc/Configuration  
ADD fastqc/* /etc/fastqc/Configuration/  
  
RUN mkdir $DOCS && mkdir $DATA && mkdir $WORK && mkdir /coursehome  
#RUN mkdir $DOCS && mkdir $DATA && mkdir $WORK  
# Paper & course notes(pdf) use less to read from command-line  
# RUN wget -O paper.pdf $DOCS http://f1000research.com/articles/1-2/v2/pdf  
# RUN wget -O NGS_tutorial.pdf http://www.walesgenepark.cardiff.ac.uk/wp-
content/uploads/2013/04/1.1-Introductory-NGS.pdf  
ADD Docs\\* $DOCS  
ADD Data\\* $DATA  
ADD GenomeAnalysisTK.jar $SIAB_HOME  
ADD Welcome.txt /etc/motd  
  
ADD entrypoint.sh /scripts/entrypoint.sh  
ADD launchsiab.sh /scripts/launchsiab.sh  
#RUN chmod +x /usr/local/sbin/entrypoint.sh  
RUN chmod +x /scripts/entrypoint.sh && chmod +x /scripts/launchsiab.sh  
# Description of reads data  
#
https://figshare.com/collections/Simulated_Illumina_BRCA1_reads_in_FASTQ_format/1641980  
# obtain reads that we will be using for analysis exercises  
#wget http://files.figshare.com/92198/Brca1Reads_1.1.fastq  
#wget http://files.figshare.com/92203/Brca1Reads_1.2.fastq  
# Download entire set of reads as zip archive  
# https://ndownloader.figshare.com/articles/92338/versions/1  
# download read sets from f1000 cloud (S3) volume  
# RUN wget -O $DATA/Reads_1.1.fastq https://s3-eu-
west-1.amazonaws.com/pstorage-f1000-a46686352/92198/Brca1Reads_1.1.fastq  
# RUN wget -O $DATA/Reads_1.2.fastq https://s3-eu-
west-1.amazonaws.com/pstorage-f1000-a46686352/92203/Brca1Reads_1.2.fastq  
#RUN chown -R $SIAB_USER:$SIAB_GROUP $SIAB_HOME  
EXPOSE 22  
EXPOSE 4200  
VOLUME /coursehome  
  
#USER ngsintro  
ENTRYPOINT ["/scripts/launchsiab.sh"]  
CMD ["/bin/bash"]  


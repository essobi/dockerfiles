FROM cami/interface  
  
# add interface definition  
COPY dockermount.conf /dckr/etc/  
COPY list-spec.sh /dckr/etc/tasks.d/--list-spec  
COPY print_version.sh /dckr/etc/tasks.d/--version  
  
# Folder optionally containing all data uploaded by the user  
ENV DCKR_USERREF $DCKR_MNT/userref  
  
# This variable MUST specify the absolute path, inside the container, of a
file containing the absolute paths of gzipped FASTQ files.  
ENV CONT_FASTQ_FILE_LISTING $DCKR_MNT/input/sample.fq.gz.list  
  
# This variable MUST specify the absolute path, inside the container, of a
file containing the absolute paths of gzipped FASTQ files  
ENV CONT_PAIRED_FASTQ_FILE_LISTING
$DCKR_MNT/input/sample.interleaved.fq.gz.list  
  
# This variable specifies the absolute path of where the FASTA file containing
the contigs can be found  
ENV CONT_CONTIGS_FILE_LISTING $DCKR_MNT/input/contigs.fna.list  
  
# This variable specifies the absolute path of where the file containing the
computed binning and/or taxonomic groups must be created  
ENV CONT_BINNING_FILE $DCKR_MNT/output/sample.camib  
  
# folder containig provided reference data(bases)  
ENV CONT_DATABASES_DIR $DCKR_MNT/camiref  


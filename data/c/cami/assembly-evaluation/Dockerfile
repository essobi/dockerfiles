FROM cami/interface  
# add interface definition  
COPY dockermount.conf /dckr/etc/  
COPY list-spec.sh /dckr/etc/tasks.d/--list-spec  
COPY print_version.sh /dckr/etc/tasks.d/--version  
# Folder optionally containing all data uploaded by the user  
ENV DCKR_USERREF $DCKR_MNT/userref  
# This varaible specifies the absolute path of where the FASTA file containing
the contigs can be found  
ENV CONT_CONTIGS_FILE $DCKR_MNT/input/contigs.fna  
# References  
ENV CONT_REFERENCE_FILE $DCKR_MNT/input/references.fna  
# OUTPUT Dir  
ENV CONT_OUTPUT_DIR $DCKR_MNT/output/  
  


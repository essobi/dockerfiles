FROM swamidass/human-blast  
  
LABEL maintainer "swamidass@gmail.com"  
LABEL version "1.0"  
LABEL website "https://bitbucket.org/swamidass/human-chimp"  
LABEL description "Compare similarity of humand and chimp shotgun reads to
reference human genome."  
  
ARG BLAST_VERSION="2.2.31-4"  
RUN apt-get -qq install -y --no-install-recommends ncbi-blast+=$BLAST_VERSION  
  
ARG NUMBER_TO_BLAST=1000  
ARG BLAST_OPTIONS=""  
ARG
HUMAN_READS=ftp://ftp.ncbi.nih.gov/pub/TraceDB/Personal_Genomics/Watson/fasta_Watson_0.gz  
ARG
CHIMP_READS=ftp://ftp.ncbi.nih.gov/pub/TraceDB/pan_troglodytes/fasta.pan_troglodytes.004.gz  
  
# download files in the repository here  
RUN curl -s https://bitbucket.org/swamidass/human-chimp/get/default.tar.gz |
tar xzvf - --strip-components=1  
  
# fetch and BLAST human reads first  
RUN curl -s $HUMAN_READS | gunzip | python filter.py $NUMBER_TO_BLAST >
human_reads.fna  
RUN blastn $BLAST_OPTIONS -db human -query human_reads.fna -max_target_seqs 1
-outfmt "7 pident qlen length sstart stitle" \  
| python get_1_blast.py > human_results.txt  
  
# fetch and BLAST chimp reads next  
RUN curl -s $CHIMP_READS | gunzip | python filter.py $NUMBER_TO_BLAST >
chimp_reads.fna  
RUN blastn $BLAST_OPTIONS -db human -query chimp_reads.fna -max_target_seqs 1
-outfmt "7 pident qlen length sstart stitle" \  
| python get_1_blast.py > chimp_results.txt  
  
RUN python summarize_blast.py human_results.txt  
RUN python summarize_blast.py chimp_results.txt  


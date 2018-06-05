#################################################################  
# Dockerfile  
# Software: miRcheck  
# Software Version:  
# Description: miRcheck and various perl scripts useful in identfying plant
miRNA genes.  
# Website: http://bartellab.wi.mit.edu/softwareDocs/  
# Files: http://bartellab.wi.mit.edu/softwareDocs/miRcheck.tar  
# Tags: Proteomics|Genomics|General  
# Provides: miRcheck  
#  
# Run : perl /programs/miRcheck/script_you_need [options]  
# Run :  
# If needed, copy new models in model folder  
# Copy:  
# Modifications: Few files have been modified during installation to add
option or to update files with current OS.  
#################################################################  
  
# Base docker image  
FROM ubuntu:14.04  
MAINTAINER test@armadillo.uqam  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Install miRcheck and dependencies  
RUN apt-get clean  
  
# Prepare installation  
RUN apt-get -qq update \  
&& apt-get -qqy install \  
\--no-install-recommends \  
software-properties-common \  
wget \  
g++ \  
emboss=6.6.0-1 \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install vienna for fold_inverted_repeats.pl  
RUN apt-add-repository -y ppa:j-4/vienna-rna > /dev/null 2>&1 \  
&& apt-get -qq update \  
&& apt-get -qqy install \  
vienna-rna \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Program Directory  
RUN mkdir -p /programs \  
  
# Install scan_for_matches  
RUN cd /programs \  
&& wget --quiet http://www.theseed.org/servers/downloads/scan_for_matches.tgz
\  
&& tar -xzf scan_for_matches.tgz \  
&& cd scan_for_matches \  
&& gcc -O -o scan_for_matches ggpunit.c scan_for_matches.c \  
&& chmod +x scan_for_matches \  
&& chmod 777 scan_for_matches \  
&& ln -sv scan_for_matches /usr/bin/scan_for_matches \  
&& rm -f ../scan_for_matches.tgz  
  
ENV PATH="$PATH:/programs/scan_for_matches"  
  
# Get miRcheck  
RUN cd /programs \  
&& wget --quiet http://bartellab.wi.mit.edu/softwareDocs/miRcheck.tar \  
&& tar -xf miRcheck.tar \  
&& mv ./_miRcheck_scripts ./miRcheck \  
&& rm -f miRcheck.tar  
  
# Update miRcheck lib localization  
RUN cd /programs/miRcheck \  
&& sed -i 's/\/home2\/mjonesrh/\/programs/g' evaluate_miRNA_candidates.pl \  
&& sed -i 's/\/home2\/mjonesrh/\/programs/g' extract_einverted_20mers.pl \  
&& sed -i 's/\/home2\/mjonesrh/\/programs/g' fold_inverted_repeats.pl \  
&& sed -i 's/\/home2\/mjonesrh\/_miRNA_search\/_scripts\///g'
fold_inverted_repeats.pl \  
&& sed -i 's/\/home2\/mjonesrh/\/programs/g' retrieve_genomic_regions.pl \  
&& sed -i 's/\/home2\/mjonesrh/\/programs/g' run_einverted.pl \  
&& sed -i 's/\/home2\/mjonesrh\/exe\/linuxexe\/RNAfold_original/RNAfold/g'
miRcheck.pm \  
&& sed -i 's/\/home2\/mjonesrh/\/programs/g' test_mircheck.pl  
  
# Add options in extract_einverted_20mers.pl  
RUN cd /programs/miRcheck \  
&& cp extract_einverted_20mers.pl extract_einverted_20mers.pl_source \  
&& sed -i '26i \  
while (@ARGV){\n\  
$thisarg = shift @ARGV;\n\  
if ($thisarg eq "-unpair" ) {$MAX_UNPAIR=shift @ARGV;} \n\  
if ($thisarg eq "-star_unpair" ) {$MAX_STAR_UNPAIR=shift @ARGV;} \n\  
if ($thisarg eq "-size_diff" ) {$MAX_SIZEDIFFERENCE=shift @ARGV;} \n\  
if ($thisarg eq "-mir_bulge") {$MAX_MIR_GAP=shift @ARGV;} \n\  
if ($thisarg eq "-star_bulge") {$MAX_STAR_GAP=shift @ARGV;} \n\  
if ($thisarg eq "-fback_min") {$MIN_FBACK_SIZE=shift @ARGV;} \n\  
if ($thisarg eq "-ass") {$MAX_MIR_AS_BULGE=shift @ARGV;} \n\  
if ($thisarg eq "-min_unpair") {$MIN_UNPAIR=shift @ARGV;} \n\  
if ($thisarg eq "-bp_ext") {$BP_EXTENSION=shift @ARGV;} \n\  
if ($thisarg eq "-max_one_nt") {$MAX_ONE_NT=shift @ARGV;} \n\  
if ($thisarg eq "-max_two_nt") {$MAX_TWO_NT=shift @ARGV;} \n\  
if ($thisarg eq "-block") {$BLOCK =shift @ARGV;} \n\  
} \n\n\  
if (not($out)){print "Script that calls miRcheck on folded inverted repeats to
identify 20mer miRNA candidates \n\  
usage: extract_einverted_20mers.pl sample_IRs_f sample_IRs_f_20mers
\\n";exit;} \n\  
' extract_einverted_20mers.pl  
  
# Add options in fold_inverted_repeats.pl  
RUN cd /programs/miRcheck \  
&& cp fold_inverted_repeats.pl fold_inverted_repeats.pl_source \  
&& sed -i '14i \  
\  
while (@ARGV){\n\  
$thisarg = shift @ARGV;\n\  
if ($thisarg eq "-flanking_nt" ) {$FLANKING_NT=shift @ARGV;} \n\  
} \n\n\  
if (not($outfile)){print "Script to retrieve genomic sequences of inverted
repeats identified by run_einverted.pl and fold with RNAfold \\n\  
usage: fold_inverted_repeats.pl sample_IRs sample_genome.fa sample_IRs_f \\n\  
sample_IRs is run_einverted.pl output file \\n\  
sample_genome.fa is genome file that run_einverted.pl was run on \\n\  
Output is saved in sample_IRs_f. \\n";exit;} \n\  
' fold_inverted_repeats.pl  
  
# Add options in run_einverted.pl  
RUN cd /programs/miRcheck \  
&& cp run_einverted.pl run_einverted.pl_source \  
&& sed -i '28i \  
\  
while (@ARGV){\n\  
$thisarg = shift @ARGV;\n\  
if ($thisarg eq "-win" ) {$WIN=shift @ARGV;} \n\  
if ($thisarg eq "-step" ) {$step=shift @ARGV;} \n\  
if ($thisarg eq "-min_pct" ) {$MIN_PCT=shift @ARGV;} \n\  
if ($thisarg eq "-min_arm") {$MIN_ARM=shift @ARGV;} \n\  
if ($thisarg eq "-gap") {$GAP=shift @ARGV;} \n\  
if ($thisarg eq "-tresh") {$THRESH=shift @ARGV;} \n\  
if ($thisarg eq "-m") {$M=shift @ARGV;} \n\  
if ($thisarg eq "-mm") {$MM=shift @ARGV;} \n\  
if ($thisarg eq "-dist") {$DIST=shift @ARGV;} \n\  
} \n\n\  
if (not($outfile)){print "Script to run einverted (emboss) to find inverted
repeats in genome-sized sequences. Breaks genomic sequences up into
overlapping fragments and calls einverted on each fragment.\\n \  
usage: run_einverted.pl sample_genome.fa genIR [options]\\n";exit;} \n\  
' run_einverted.pl  
  
# Add options in run_patscan.pl  
RUN cd /programs/miRcheck \  
&& cp run_patscan.pl run_patscan.pl_source \  
&& sed -i 's/ARGV\[5\]/ARGV\[2\]/' run_patscan.pl \  
&& sed -i '10i \  
$mismatches = 0; \n\  
$deletions = 0; \n\  
$insertions = 0; \n\  
\  
while (@ARGV){\n\  
$thisarg = shift @ARGV;\n\  
if ($thisarg eq "-mismatches" ) {$mismatches=shift @ARGV;} \n\  
if ($thisarg eq "-deletions" ) {$deletions =shift @ARGV;} \n\  
if ($thisarg eq "-insertions" ) {$insertions=shift @ARGV;} \n\  
} \n\n\  
if (not($outfile)){print "usage: simple_patscan.pl query.fa database.fa
outfile -mismatches 0 -deletions 0 -insertions 0 \\n";exit;} \n\  
\n\  
' run_patscan.pl  
  
# Add options in retrieve_genomic_regions.pl  
RUN cd /programs/miRcheck \  
&& cp retrieve_genomic_regions.pl retrieve_genomic_regions.pl_source \  
&& sed -i".bak" '4,12d' retrieve_genomic_regions.pl \  
&& sed -i '4i \  
# usage: retrieve_genomic_regions.pl sample_miRNA_matches sample_genome.fa
sample_miRNA_matches_genomic -win window_size \n\  
\  
$hitfile =$ARGV[0]; # list of sequences and genomic coorinates\n\  
$genome = $ARGV[1]; #Fasta file of genomic sequence\n\  
$outfile = $ARGV [2]; #name of outputfile\n\  
$WIN = 0; # number of flanking nucleotides to add to each side of putative
miRNA \n\  
\  
while (@ARGV){\n\  
$thisarg = shift @ARGV;\n\  
if ($thisarg eq "-win" ) {$WIN=shift @ARGV;} \n\  
} \n\n\  
\n\  
if (not($outfile)){print "Retrieves genomic regions containing matches
identifed by run_patscan.pl. \\n\  
usage: retrieve_genomic_regions.pl sample_miRNA_matches sample_genome.fa
sample_miRNA_matches_genomic [options]\\n";exit;} \n\  
' retrieve_genomic_regions.pl  
  
# Make miRcheck files executable  
RUN chmod -R +x /programs/miRcheck  
  
# Create data directory  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
# Set workdir  
WORKDIR /data  


  
# Galaxy - usegalaxy.org clone  
#  
# VERSION 0.1  
FROM bgruening/galaxy-stable:dev  
MAINTAINER Bjoern A. Gruening, bjoern.gruening@gmail.com  
ENV GALAXY_CONFIG_BRAND usegalaxy.org Clone  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name subtract_query
--panel-section-name 'Join,_Subtract_and_Group'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name indel_realigner
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name table_recalibration
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name picard --panel-
section-name 'NGS:_Picard_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
filter_transcripts_via_tracking --panel-section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name varscan_version_2
--panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name rcve --panel-section-
name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfbedintersect
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name tophat_fusion_post
--panel-section-name 'NGS:_RNA-seq'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name weblogo3 --panel-
section-name 'Motif_Tools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
sam_bitwise_flag_filter --panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
best_regression_subsets --panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name histogram --panel-
section-name 'Graph/Display_Data'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fasta_filter_by_length
--panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name cluster --panel-
section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_manipulation
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name cuffcompare --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastqtofasta --panel-
section-id 'NGS_QC'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o aaronquinlan --name bedtools --panel-
section-name 'BEDTools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastq_quality_converter --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bamtools --panel-
section-name 'NGS:_BAM_Tools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name join --panel-section-
id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastx_nucleotides_distribution --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o nick --name allele_counts --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_calmd
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name short_reads_trim_seq
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name tophat2 --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o iuc --name stringtie --panel-section-
name 'NGS:_RNA-seq'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_quality_boxplot
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name complement --panel-
section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name variant_annotator
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_bedcov
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfannotategenotypes
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name bcftools_view
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name lastz --panel-section-
name 'NGS:_Mapping'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_sort --panel-
section-name 'NGS:_SAMtools'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o guru-ananda --name heatmap --panel-
section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o boris --name phylorelatives --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name tabular_to_fastq
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name linear_regression
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name hgv_fundo --panel-
section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name variant_select
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name windowsplitter
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name variant_combine
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name indels_3way --panel-
section-name 'Regional_Variation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name gmaj --panel-section-
name 'Graph/Display_Data'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfleftalign --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name hgv_hilbertvis
--panel-section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name flanking_features
--panel-section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name freebayes --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name ctd_batch --panel-
section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fasta_compute_length
--panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_filter --panel-
section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name cuffdiff --panel-
section-name 'NGS:_RNA-seq'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastqc --panel-
section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcf2tsv --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fasta_formatter
--panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o tyty --name structurefold --panel-
section-name 'RNA_Structure_Prediction'" \  
"--url https://toolshed.g2.bx.psu.edu -o guru-ananda --name rhmm --panel-
section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name clustalw --panel-
section-name 'Multiple_Alignments'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name gi2taxonomy --panel-
section-name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name dgidb_annotator
--panel-section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcftools_annotate
--panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o pcingola --name snpeff --panel-
section-name 'snpEff'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name getindelrates_3way
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name emboss_5 --panel-
section-name 'EMBOSS'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name depth_of_coverage
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name freebayes_wrapper
--panel-section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_quality_filter
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
canonical_correlation_analysis --panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name sicer --panel-section-
name 'NGS:_Peak_Calling'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name annotation_profiler
--panel-section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name pileup_parser --panel-
section-name 'NGS:_SAMtools'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name unified_genotyper
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name
cloudmap_variant_discovery_mapping --panel-section-name
'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bamtools_filter
--panel-section-name 'NGS:_BAM_Tools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name featurecounter
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bamtools_split
--panel-section-name 'NGS:_BAM_Tools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_groomer --panel-
section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_mpileup
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastx_clipper --panel-
section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name tabular_to_fasta
--panel-section-name 'FASTA_manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name scatterplot --panel-
section-name 'Graph/Display_Data'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name getindels_2way
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fasta_to_tabular
--panel-section-name 'Convert_Formats'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastq_masker_by_quality --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name variant_recalibrator
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name maf_cpg_filter
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name plot_from_lda --panel-
section-name 'Statistics'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastqtofasta --panel-
section-name 'Convert_Formats'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_idxstats
--panel-section-name 'NGS:_SAMtools'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name
ems_variant_density_mapping --panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfsort --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastx_barcode_splitter
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
kernel_canonical_correlation_analysis --panel-section-name
'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastq_trimmer_by_quality --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name gffread --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcffilter --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name analyze_covariates
--panel-section-name 'NGS:_GATK_Tools_(beta)'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
variant_apply_recalibration --panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bwa_wrappers --panel-
section-name 'NGS:_Mapping'" \  
"--url https://toolshed.g2.bx.psu.edu -o boris --name getalleleseq --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name t2t_report --panel-
section-name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name coverage --panel-
section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name divide_pg_snp --panel-
section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfcheck --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastx_renamer --panel-
section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_to_fasta
--panel-section-name 'Convert_Formats'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_slice_bam
--panel-section-name 'NGS:_SAMtools'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name quality_filter
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastx_trimmer --panel-
section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
microsats_alignment_level --panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_combiner
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfannotate --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name variant_eval --panel-
section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name t2ps --panel-section-
name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name picard --panel-
section-name 'NGS:_Picard'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtool_filter2
--panel-section-name 'NGS:_SAMtools'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfcommonsamples
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfbreakcreatemulti
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfselectsamples
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name
snp_mapping_using_wgs --panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastq_paired_end_splitter --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name weightedaverage
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bwa --panel-section-
name 'NGS:_Mapping'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfvcfintersect
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o miller-lab --name genome_diversity
--panel-section-name 'Genome_Diversity'" \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name
check_snpeff_candidates --panel-section-name 'snpEff'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastx_collapser
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfallelicprimitives
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name lca_wrapper --panel-
section-name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fasta_concatenate_by_species --panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_to_tabular
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name cuffnorm --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfaddinfo --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfhethom --panel-
section-name 'NGS:_VCF_Manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name count_covariates
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_stats
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name sam2interval --panel-
section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
principal_component_analysis --panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name pileup_interval
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfgenotypes --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o boris --name hetbox --panel-section-
name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name variants_validate
--panel-section-name 'NGS:_GATK_Tools_(beta)'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name partialr_square
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastx_reverse_complement --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bowtie2 --panel-
section-name 'NGS:_Mapping'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name table_annovar --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name sam_to_bam --panel-
section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfflatten --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fasta_to_tabular
--panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfgeno2haplo --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bam_to_sam --panel-
section-name 'NGS:_SAMtools'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fasta_nucleotide_changer --panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastx_artifacts_filter
--panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfdistance --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name concat --panel-
section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
short_reads_figure_score --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name snpfreq --panel-
section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name correlation --panel-
section-name 'Statistics'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name cufflinks --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name column_maker --panel-
section-name 'Text_Manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name substitutions --panel-
section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_trimmer --panel-
section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfcombine --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name megablast_wrapper
--panel-section-name 'NGS:_Mapping'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_stats --panel-
section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bowtie_wrappers
--panel-section-name 'NGS:_Mapping'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastx_collapser
--panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_reheader
--panel-section-name 'NGS:_SAMtools'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastx_quality_statistics --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name mutate_snp_codon
--panel-section-name 'Evolution'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastq_paired_end_joiner --panel-section-id 'NGS_QC'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name subtract --panel-
section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name xy_plot --panel-
section-name 'Graph/Display_Data'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name get_flanks --panel-
section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
kernel_principal_component_analysis --panel-section-name 'Regional_Variation'"
\  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name basecoverage --panel-
section-id 'bxops'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name cuffquant --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name variant_filtration
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name poisson2test --panel-
section-name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name intersect --panel-
section-id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name print_reads --panel-
section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name merge --panel-section-
id 'bxops'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name ucsc_custom_track
--panel-section-name 'Graph/Display_Data'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name cuffmerge --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfprimers --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_flagstat
--panel-section-name 'NGS:_SAMtools'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name dna_filtering --panel-
section-name 'Filter_and_Sort'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name substitution_rates
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name generate_pc_lda_matrix
--panel-section-name 'Statistics'" \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name
cloudmap_in_silico_complementation --panel-section-name
'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o blankenberg --name
naive_variant_caller --panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_rmdup
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
logistic_regression_vif --panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name samtools_split
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcffixup --panel-
section-name 'NGS:_VCF_Manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name megablast_xml_parser
--panel-section-name 'NGS:_Mapping'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name find_diag_hits
--panel-section-name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name lda_analysis --panel-
section-name 'Statistics'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcftools_slice
--panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name macs --panel-section-
name 'NGS:_Peak_Calling'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name microsats_mutability
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcf2pgsnp --panel-
section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfrandomsample
--panel-section-name 'NGS:_VCF_Manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
realigner_target_creator --panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o guru-ananda --name karyotype_plot
--panel-section-name 'Regional_Variation'"  
# Mark folders as imported from the host.  
VOLUME ["/export/", "/data/", "/var/lib/docker"]  
# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)  
EXPOSE :80  
EXPOSE :21  
EXPOSE :8800  
# Autostart script that is invoked during container start  
CMD ["/usr/bin/startup"]  


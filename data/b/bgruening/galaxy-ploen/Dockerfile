# Galaxy - MPI Plön Edition  
#  
# VERSION 0.1  
FROM bgruening/usegalaxy  
MAINTAINER Bjoern A. Gruening, bjoern.gruening@gmail.com  
ENV GALAXY_CONFIG_BRAND MPI Ploen  
RUN add-tool-shed --url 'http://gigatoolshed.net/' --name 'GigaSience Tool
Shed'  
RUN add-tool-shed --url 'https://testtoolshed.g2.bx.psu.edu/' --name 'Test
Tool Shed'  
# Install tools from giga tool shed  
RUN install-repository \  
"--url http://gigatoolshed.net/ -o peterli --name allpaths --panel-section-
name Assembly_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name soapdenovo2 --panel-section-
name Assembly_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name soapdenovo1 --panel-section-
name Assembly_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name pca --panel-section-name
Varian_Analysis_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name diversity_pi --panel-
section-name Varian_Analysis_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name
assignment_of_optimal_breeding_pairs --panel-section-name Varian_Analysis_exp"
\  
"--url http://gigatoolshed.net/ -o peterli --name inbreeding_and_kinship
--panel-section-name Varian_Analysis_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name
offspring_heterozygosity_pedigree --panel-section-name Varian_Analysis_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name offspring_heterozygosity
--panel-section-name Varian_Analysis_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name select_snps --panel-section-
name Varian_Analysis_exp" \  
"--url http://gigatoolshed.net/ -o peterli --name snp2vcf --panel-section-name
Varian_Analysis_exp"  
# non-standard tools from main  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu/ -o bobbledavidson --name beagle4_0
--panel-section-name Varian_Analysis_exp" \  
"--url https://toolshed.g2.bx.psu.edu/ -o edward-kirton --name
velvet_toolsuite --panel-section-name Assembly_exp" \  
"--url https://toolshed.g2.bx.psu.edu/ -o dereeper --name package_plink_1_07
--panel-section-name Varian_Analysis_exp" \  
"--url https://toolshed.g2.bx.psu.edu/ -o dereeper --name sniplay --panel-
section-name Varian_Analysis_exp" \  
"--url https://toolshed.g2.bx.psu.edu/ -o dereeper --name tassel5 --panel-
section-name Varian_Analysis_exp" \  
"--url https://toolshed.g2.bx.psu.edu/ -o drosofff --name msp_cap3 --panel-
section-name Assembly_exp" \  
"--url https://toolshed.g2.bx.psu.edu/ -o iuc --name package_bcftools_1_2
--panel-section-name Varian_Analysis_exp" \  
"--url https://toolshed.g2.bx.psu.edu/ -o subazini --name ngsaligners --panel-
section-name Assembly_exp"  
# exome  
# Install GATK2, samtools and  
RUN install-repository \  
"--url http://toolshed.g2.bx.psu.edu/ -o iuc --name gatk2 --panel-section-name
GATK2" \  
"--url http://toolshed.g2.bx.psu.edu/ -o devteam --name suite_samtools_0_1_19
--panel-section-name SAMTools" \  
"--url http://toolshed.g2.bx.psu.edu/ -o devteam --name freebayes --panel-
section-name Freebayes"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu/ --name variant_filtration --owner
devteam"  
RUN install-repository \  
"--url http://toolshed.g2.bx.psu.edu/ -o bgruening --name deeptools --panel-
section-name deepTools" \  
"--url http://toolshed.g2.bx.psu.edu/ -o devteam --name
data_manager_bwa_index_builder"  
RUN install-repository \  
"--url http://toolshed.g2.bx.psu.edu/ -o iuc --name vt_variant_tools --panel-
section-name VCFtools" \  
"--url http://toolshed.g2.bx.psu.edu/ -o devteam --name suite_vcflib_14_08
--panel-section-name VCFtools" \  
"--url http://toolshed.g2.bx.psu.edu/ -o iuc --name snpeff --panel-section-
name SNPEff"  
# Install GEMINI and BED tools  
RUN install-repository \  
"--url http://toolshed.g2.bx.psu.edu/ -o iuc --name
data_manager_gemini_database_downloader" \  
"--url http://toolshed.g2.bx.psu.edu/ -o iuc --name gemini --panel-section-
name VariantSelection" \  
"--url http://toolshed.g2.bx.psu.edu/ -o iuc --name bedtools --panel-section-
name BEDtools"  
# master main clone  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name subtract_query
--panel-section-name 'Join,_Subtract_and_Group'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name indel_realigner
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name table_recalibration
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfallelicprimitives
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name picard --panel-
section-name 'NGS:_Picard_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
filter_transcripts_via_tracking --panel-section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name varscan_version_2
--panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name rcve --panel-section-
name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfbedintersect
--panel-section-name 'NGS:_VCF_Manipulation'"  
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
section-name 'Operate_on_Genomic_Intervals'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcffixup --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_manipulation
--panel-section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastqtofasta --panel-
section-name 'NGS:_QC_and_manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o aaronquinlan --name bedtools --panel-
section-name 'BEDTools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastq_quality_converter --panel-section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name bamtools --panel-
section-name 'NGS:_BAM_Tools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name join --panel-section-
name 'Operate_on_Genomic_Intervals'" \  
"--url https://toolshed.g2.bx.psu.edu -o nick --name allele_counts --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name short_reads_trim_seq
--panel-section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name tophat2 --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o iuc --name stringtie --panel-section-
name 'NGS:_RNA-seq'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_quality_boxplot
--panel-section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name complement --panel-
section-name 'Operate_on_Genomic_Intervals'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfprimers --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfsort --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfannotategenotypes
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name bcftools_view
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name lastz --panel-section-
name 'NGS:_Mapping'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o guru-ananda --name heatmap --panel-
section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfdistance --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o boris --name phylorelatives --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name tabular_to_fastq
--panel-section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name linear_regression
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name hgv_fundo --panel-
section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name windowsplitter
--panel-section-name 'Regional_Variation'" \  
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
--panel-section-name 'Operate_on_Genomic_Intervals'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name freebayes --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name ctd_batch --panel-
section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fasta_compute_length
--panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_filter --panel-
section-name 'NGS:_QC_and_manipulation'"  
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
section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name tabular_to_fasta
--panel-section-name 'FASTA_manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name
ems_variant_density_mapping --panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfaddinfo --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfannotate --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
kernel_canonical_correlation_analysis --panel-section-name
'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastq_trimmer_by_quality --panel-section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name gffread --panel-
section-name 'NGS:_RNA-seq'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcffilter --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name analyze_covariates
--panel-section-name 'NGS:_GATK_Tools_(beta)'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o boris --name getalleleseq --panel-
section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name t2t_report --panel-
section-name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name coverage --panel-
section-name 'Operate_on_Genomic_Intervals'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name divide_pg_snp --panel-
section-name 'Phenotype_Association'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfcheck --panel-
section-name 'NGS:_VCF_Manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfgenotypes --panel-
section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name quality_filter
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
microsats_alignment_level --panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_combiner
--panel-section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name t2ps --panel-section-
name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name picard --panel-
section-name 'NGS:_Picard'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfbreakcreatemulti
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfselectsamples
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name
snp_mapping_using_wgs --panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fastq_paired_end_splitter --panel-section-name 'NGS:_QC_and_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name weightedaverage
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcfvcfintersect
--panel-section-name 'NGS:_VCF_Manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o miller-lab --name genome_diversity
--panel-section-name 'Genome_Diversity'" \  
"--url https://toolshed.g2.bx.psu.edu -o gregory-minevich --name
check_snpeff_candidates --panel-section-name 'snpEff'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name lca_wrapper --panel-
section-name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
fasta_concatenate_by_species --panel-section-name 'FASTA_manipulation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name fastq_to_tabular
--panel-section-name 'NGS:_QC_and_manipulation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name count_covariates
--panel-section-name 'NGS:_GATK_Tools_(beta)'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name sam2interval --panel-
section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
principal_component_analysis --panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name pileup_interval
--panel-section-name 'NGS:_SAMtools'" \  
"--url https://toolshed.g2.bx.psu.edu -o boris --name hetbox --panel-section-
name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name variants_validate
--panel-section-name 'NGS:_GATK_Tools_(beta)'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name mutate_snp_codon
--panel-section-name 'Evolution'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name subtract --panel-
section-name 'Operate_on_Genomic_Intervals'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
kernel_principal_component_analysis --panel-section-name 'Regional_Variation'"
\  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name basecoverage --panel-
section-name 'Operate_on_Genomic_Intervals'"  
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
"--url https://toolshed.g2.bx.psu.edu -o devteam --name
logistic_regression_vif --panel-section-name 'Regional_Variation'"  
RUN install-repository \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name find_diag_hits
--panel-section-name 'Metagenomic_analyses'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name lda_analysis --panel-
section-name 'Statistics'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcftools_slice
--panel-section-name 'NGS:_Variant_Analysis'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name microsats_mutability
--panel-section-name 'Regional_Variation'" \  
"--url https://toolshed.g2.bx.psu.edu -o devteam --name vcf2pgsnp --panel-
section-name 'Phenotype_Association'"  
# deepseq  
#RUN install-repository \  
#"--url http://testtoolshed.g2.bx.psu.edu/ -o iuc --name package_deseq2_1_6_1"
\  
#"--url http://testtoolshed.g2.bx.psu.edu/ -o bgruening --name deseq2" \  
#"--url http://toolshed.g2.bx.psu.edu/ -o lparsons --name htseq_count" \  
#"--url http://toolshed.g2.bx.psu.edu/ -o devteam --name
suite_cufflinks_2_2_1"  
# Mark folders as imported from the host.  
VOLUME ["/export/", "/data/", "/var/lib/docker"]  
# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)  
EXPOSE :80  
EXPOSE :21  
EXPOSE :8800  
# Autostart script that is invoked during container start  
CMD ["/usr/bin/startup"]  


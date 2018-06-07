FROM continuumio/miniconda:4.4.10  
MAINTAINER Alejandro Barrera <alejandro.barrera@duke.edu>  
  
ENV DEEPTOOLS_VERSION=3.0.1  
RUN conda install -c bioconda deeptools=${DEEPTOOLS_VERSION}  
  
# Default command to execute at startup of the container  
ENV DEEPTOOLS_SUBCOMMANDS="multiBamSummary multiBigwigSummary correctGCBias
bamCoverage bamCompare bigwigCompare computeMatrix plotCorrelation plotPCA
plotFingerprint bamPEFragmentSize computeGCBias plotCoverage plotHeatmap
plotProfile"  
CMD echo "deepTools subcommands:\n\t$DEEPTOOLS_SUBCOMMANDS"  


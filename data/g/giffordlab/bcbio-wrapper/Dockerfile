# The giffordlab/bcbio-nextgen container is an automated build that  
# uses our clean fork of bcbio-nextgen to get upstream images. The  
# automated build for this repository is set up to automatically  
# rebuild when that image is updated.  
FROM giffordlab/bcbio-nextgen  
  
MAINTAINER Matt Edwards "matted@mit.edu"  
# Fix Ensemble tools.  
RUN sudo sed -i
's/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,\n
\"saccharomyces_cerevisiae_vep_\$API_VERSION.tar.gz\"\,/g'
/usr/local/bin/vep_install.pl  
RUN sudo sed -i
's/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,\n
\"canis_familiaris_vep_\$API_VERSION.tar.gz\"\,/g'
/usr/local/bin/vep_install.pl  
RUN sudo sed -i
's/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,\n
\"drosophila_melanogaster_vep_\$API_VERSION.tar.gz\"\,/g'
/usr/local/bin/vep_install.pl  
RUN sudo sed -i
's/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,\n
\"xenopus_tropicalis_vep_\$API_VERSION.tar.gz\"\,/g'
/usr/local/bin/vep_install.pl  
RUN sudo sed -i
's/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,/\"homo_sapiens_vep_\$API_VERSION.tar.gz\"\,\n
\"caenorhabditis_elegans_vep_\$API_VERSION.tar.gz\"\,/g'
/usr/local/bin/vep_install.pl  
  
RUN sed -i 's/250/2000/g' `readlink -m /usr/local/bin/fastqc`  
  
# Bring bcbio back to stable version, just to match releases a bit better.  
RUN mkdir -p /mnt/biodata/galaxy  
RUN /usr/local/share/bcbio-nextgen/anaconda/bin/bcbio_nextgen.py upgrade -u
stable --isolate --tools  
  
# Only needed to make older versions of snpEff coexist a bit better.  
RUN mkdir -p /usr/local/share/java/snpeff  
RUN ln -s /usr/local/share/snpEff.config
/usr/local/share/java/snpeff/snpEff.config  
  
RUN apt-get update -qq && \  
apt-get install -y emacs23-nox nano  
  
ADD align_bcbio.sh /usr/local/bin/align_bcbio.sh  
  
# Right now we run a shell script that calls bcbio a few times, so this won't
work.  
# Leaving it commented-out to maintain backwards compatibility.  
# ENTRYPOINT ["/usr/local/bin/align_bcbio.sh"]  
ADD docker_signal_wrapper/run_wrapper.py /usr/local/bin/run_wrapper.py  
  
ENTRYPOINT ["/usr/bin/python", "/usr/local/bin/run_wrapper.py"]  


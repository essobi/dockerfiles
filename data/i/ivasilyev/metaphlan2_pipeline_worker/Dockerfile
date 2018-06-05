################## BASE IMAGE ######################  
FROM ivasilyev/bwt_filtering_pipeline_worker  
  
################## METADATA ######################  
LABEL base.image="ivasilyev/bwt_filtering_pipeline_worker"  
LABEL pipeline="metaphlan2"  
LABEL name="metaphlan2_pipeline_worker"  
LABEL description="Docker image containing all required packages to run
MetaPhlAn2"  
LABEL website="https://bitbucket.org/biobakery/metaphlan2"  
LABEL
documentation="https://bitbucket.org/biobakery/biobakery/wiki/metaphlan2"  
LABEL license="GPL-2.0"  
LABEL tags="Genomics"  
LABEL maintainer="Ilya Vasilyev <u0412u0418u042e@gmail.com>"  
  
################## INSTALLATION ######################  
# Base image CLI: docker run --rm -v /data:/data -it
ivasilyev/bwt_filtering_pipeline_worker bash  
  
# Clone the MetaPhlAn2 repository and add it to PATH:  
RUN cd ~/scripts && \  
hg clone https://bitbucket.org/biobakery/metaphlan2 && \  
cd metaphlan2 && \  
echo "export PATH=$PATH:${PWD}" | tee -a ~/.bashrc  
  
# Get the new MetaPhlAn2 scripts & customize previous mapping script  
RUN cd ~/scripts && \  
git clone https://github.com/ivasilyev/biopipelines-docker.git && \  
rm -f pipeline_wrapper.py && \  
sed -i "s|'bowtie', |'bowtie', '--sam-nohead', '--sam-nosq\', |g" nBee.py && \  
sed -i "s|'bowtie2', |'bowtie2', '--no-hd', '--no-sq', '--no-unal', '--very-
sensitive', |g" nBee.py && \  
mv biopipelines-docker/metaphlan2_pipeline/worker/pipeline_wrapper.py . && \  
rm -rf biopipelines-docker && \  
chmod -R +x ~/scripts  
  
# Let to MetaPhlAn2 prepare the environment  
#RUN python ~/scripts/metaphlan2/metaphlan2.py --install && \  
# rm -f ~/scripts/metaphlan2/databases/mpa_v20_m200.tar
~/scripts/metaphlan2/databases/mpa_v20_m200.fna.bz2  
  
# Get the MetaPhlAn2 reference sequences database  
#RUN mkdir /reference/metaphlan2 && \  
# cd /reference/metaphlan2 && \  
# wget --quiet
https://bitbucket.org/biobakery/metaphlan2/downloads/mpa_v20_m200.tar && \  
# tar xopf mpa_v20_m200.tar && \  
# bzip2 -d mpa_v20_m200.fna.bz2 && \  
# python3 ~/scripts/cook_the_reference.py -h -i mpa_v20_m200.fna -o
/reference/metaphlan2/index && \  
# rm -f mpa_v20_m200.tar  
  
# Directories to mount  
VOLUME ["/data", "/config", "/reference"]  
  
# Overwrite this with 'CMD []' in a dependent Dockerfile  
# CMD ["/bin/bash"]  
CMD ["python3", "/home/docker/scripts/pipeline_wrapper.py"]  
  
# Setup the default directory  
WORKDIR /home/docker  
  
# Manual build command: docker build -t metaphlan2_pipeline_worker . && docker
tag metaphlan2_pipeline_worker ivasilyev/metaphlan2_pipeline_worker:latest &&
docker push ivasilyev/metaphlan2_pipeline_worker:latest  


FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
python2.7 \  
wget \  
unzip \  
mdbtools \  
rsync \  
openjdk-6-jre-headless \  
&& apt-get autoremove \  
&& apt-get clean  
  
# install Bioformats  
RUN wget http://downloads.openmicroscopy.org/bio-
formats/5.0.2/artifacts/bftools.zip  
RUN mkdir /bftools; cd bftools; unzip ../bftools.zip; rm ../bftools.zip  
ENV PATH $PATH:/bftools  
  
# run as non-root user  
RUN adduser lmu  
  
# create share volumes for data, add empty files to prevent volumes belonging
to root  
RUN mkdir /input /output /archive  
#RUN touch /input/ph /output/ph /archive/ph  
#RUN chown -R lmu:lmu /input /output /archive  
#VOLUME ["/input", "/output", "/archive"]  
# run the conversion script when container is run  
ENTRYPOINT ["python2.7", "stage_cellomics2tiff.py"]  
  
# add source and test directories  
ADD python /python  
ADD test /test  
WORKDIR python  
  
# run as root for now...  
#USER lmu  


FROM openjdk:8u151-jre-slim-stretch  
# NOTE: It is tricky to make this using alpine linux, as GenomicsDBImport
requires  
# glibc and alpine doesn't have this installed by default.  
# One task that could be done is to make this work - if so, any docker  
# container will need to pass the test described here:  
# https://github.com/broadinstitute/gatk/issues/4124#issuecomment-356988842  
LABEL author="th10@sanger.ac.uk"  
  
RUN apt-get -q=2 update && \  
apt-get -q=2 install -y --no-install-recommends wget libblas3 libgfortran3
liblapack3 libgomp1 && \  
apt-get autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp && \  
mkdir gatk && \  
cd gatk && \  
wget
https://github.com/broadinstitute/gatk/releases/download/4.0.0.0/gatk-4.0.0.0.zip
&& \  
echo "bcbda01d226d44459daaf7dc1ed2109ae4bfd9f8 gatk-4.0.0.0.zip" | sha1sum -c
- && \  
unzip gatk-4.0.0.0.zip && \  
mkdir /gatk && \  
mv gatk-4.0.0.0/gatk-package-4.0.0.0-local.jar /gatk/gatk.jar && \  
rm -rf /tmp/gatk  


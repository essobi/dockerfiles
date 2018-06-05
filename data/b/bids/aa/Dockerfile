FROM bids/base_freesurfer  
  
RUN apt-get update && \  
apt-get install -y curl && \  
curl -sSL http://neuro.debian.net/lists/trusty.us-tn.full >>
/etc/apt/sources.list.d/neurodebian.sources.list && \  
apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9 &&
\  
apt-get update && \  
apt-get remove -y curl && \  
apt-get install -y fsl-core && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure environment  
ENV FSLDIR=/usr/share/fsl/5.0  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
ENV PATH=/usr/lib/fsl/5.0:$PATH  
ENV FSLMULTIFILEQUIT=TRUE  
ENV POSSUMDIR=/usr/share/fsl/5.0  
ENV LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH  
ENV FSLTCLSH=/usr/bin/tclsh  
ENV FSLWISH=/usr/bin/wish  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
  
# Prepare for downloads  
RUN apt-get update -y && apt-get install -y wget unzip  
RUN mkdir /usr/local/software  
RUN mkdir /opt/Download  
  
# aa - compile with dependecies  
RUN wget -O /opt/Download/mcr.zip
http://uk.mathworks.com/supportfiles/MCR_Runtime/R2012b/MCR_R2012b_glnxa64_installer.zip  
RUN mkdir /opt/Download/mcr  
RUN unzip /opt/Download/mcr.zip -d /opt/Download/mcr  
RUN wget -O /opt/Download/MCR_installer_input.txt
https://googledrive.com/host/0B9T4a0ktPmB1R2FJRjVNa19JVTQ/MCR_installer_input.txt
#
https://ndownloader.figshare.com/files/5588213?private_link=025fa9f2e33725713eb0  
RUN /opt/Download/mcr/install -inputFile /opt/Download/MCR_installer_input.txt  
  
RUN wget -O /opt/Download/aa.tar.gz
https://googledrive.com/host/0B9T4a0ktPmB1R2FJRjVNa19JVTQ/automaticanalysis5.tar.gz
#https://ndownloader.figshare.com/files/5590577?private_link=eee1c8631ce8697f7133  
RUN tar -xzf /opt/Download/aa.tar.gz -C /opt  
  
ADD aap_parameters_defaults.xml /opt/aap_parameters_defaults.xml  
ADD aap_parameters_defaults_CRN.xml /opt/aap_parameters_defaults_CRN.xml  
  
# Cleanup  
RUN rm -rf /opt/Download  
  
# Test  
COPY test/BIDS114_aa.m /opt/test/BIDS114_aa.m  
COPY test/BIDS114_tasklist.xml /opt/test/BIDS114_tasklist.xml  
  
# Entry  
RUN mkdir /opt/bin  
ADD run.sh /opt/bin/run.sh  
ADD look_for_arg.sh /opt/bin/look_for_arg.sh  
RUN chmod +x /opt/bin/*  
  
COPY version /version  
  
ENTRYPOINT ["/opt/bin/run.sh"]  


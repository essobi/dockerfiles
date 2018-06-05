FROM ubuntu  
MAINTAINER Eva Ramon <eva.ramon@swisscom.com>  
  
# Environment settings and defaults if not passed  
ENV CUSTOMER_ID="customer"  
ENV CUSTOMER_KEY="key"  
ENV SIGNATURE_TYPE=sign  
ENV DIGEST_METHOD=SHA256  
ENV VERBOSITY=2  
# Environment settings (internal use)  
ENV WORK=/opt/work  
ENV CFG=$WORK/itext.cfg  
ENV FOLDER_IN=$WORK/in  
ENV FOLDER_OUT=$WORK/out  
ENV ITEXT=/opt/itext-ais  
  
# Install Base System  
RUN \  
apt-get update && DEBIAN_FRONTEND=noninteractive \  
apt-get install -y default-jre bash git && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install AIS iText module  
RUN git clone https://github.com/SCS-CBU-CED-IAM/itext-ais.git $ITEXT  
  
# Add files  
ADD config.sh $WORK/config.sh  
ADD watch.sh $WORK/watch.sh  
ADD sign.sh $WORK/sign.sh  
RUN chmod +x $WORK/*.sh  
  
# Expose volume  
VOLUME $WORK  
  
# Run  
WORKDIR $WORK  
CMD $WORK/config.sh;$WORK/watch.sh  


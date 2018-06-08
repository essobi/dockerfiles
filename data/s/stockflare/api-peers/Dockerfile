FROM stockflare/base:slim  
  
# Install the latest AWS cli - needed for S3 command line actions in scripts  
RUN \  
mkdir -p /aws && \  
apk -Uuv add ruby-irb groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  


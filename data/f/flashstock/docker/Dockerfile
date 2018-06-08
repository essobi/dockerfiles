FROM docker:17.09  
  
RUN apk add --no-cache \  
bash \  
git \  
jq \  
openssh-client \  
python \  
zip  
  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps \  
curl \  
; \  
\  
if ! curl -o awscli-bundle.zip "https://s3.amazonaws.com/aws-cli/awscli-
bundle.zip"; then \  
echo >&2 "error: failed to download 'awscli' from S3"; \  
exit 1; \  
fi; \  
\  
unzip awscli-bundle.zip; \  
\  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws; \  
\  
rm awscli-bundle.zip; \  
\  
apk del .fetch-deps; \  
\  
aws --version  
  
CMD ["bash"]  


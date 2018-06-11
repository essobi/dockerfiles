#docker pull pivotalgreenhouse/bosh-cli  
FROM golang  
  
#install jq  
RUN wget -q https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
-O /usr/local/bin/jq && chmod +x /usr/local/bin/jq  
  
# gcloud CLI  
RUN apt-get update && apt-get install -y apt-transport-https && \  
echo "deb https://packages.cloud.google.com/apt cloud-sdk-jessie main" | tee
-a /etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update && \  
apt-get install -y google-cloud-sdk  
  
# bosh Golang CLI  
RUN version_number=$(curl 'https://github.com/cloudfoundry/bosh-
cli/releases/latest' 2>&1 | egrep -o '([0-9]+\\.[0-9]+\\.[0-9]+)') && \  
curl "https://s3.amazonaws.com/bosh-cli-artifacts/bosh-
cli-${version_number}-linux-amd64" -o /usr/local/bin/bosh && \  
chmod 755 /usr/local/bin/bosh  
  


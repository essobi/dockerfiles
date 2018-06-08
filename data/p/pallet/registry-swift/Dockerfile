# Add swift support to the official Registry image  
# Run a docker registry backed by a Swift datastore.  
#  
# /usr/bin/docker run --rm \  
# -e SETTINGS_FLAVOR=swift \  
# -e OS_CONTAINER=docker-registry \  
# -e OS_USERNAME=your-username \  
# -e OS_PASSWORD=your-password \  
# -e OS_AUTH_URL=https://identity.api.rackspacecloud.com/v2.0/ \  
# -e OS_REGION_NAME=DFW \  
# -e OS_TENANT_NAME=MossoCloudFS_nnnnn \  
# -p 5000:5000 \  
# --name registry \  
# registry-swift  
  
FROM registry:0.7.2  
MAINTAINER Hugo Duncan <hugo@palletops.com>  
  
# Add the swift support  
RUN ["pip", "install", "docker-registry-driver-swift", "python-
keystoneclient"]  


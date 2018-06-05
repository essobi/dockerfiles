FROM hashicorp/terraform:0.11.7  
MAINTAINER "Stuart Auld <sauld@cozero.com.au>"  
  
# Add zip (for building null resources), chamber, buildkite provider  
  
ENV CHAMBER_VERSION=v1.15.0  
ENV BUILDKITE_PROVIDER_VERSION=0.0.2  
  
RUN \  
apk --no-cache add zip \  
&& curl -L
https://github.com/segmentio/chamber/releases/download/$CHAMBER_VERSION/chamber-$CHAMBER_VERSION-
linux-amd64 > /usr/bin/chamber \  
&& curl -L https://cozero-public-resources.s3.amazonaws.com/terraform-
provider-buildkite > /bin/terraform-provider-buildkite \  
&& chmod +x /usr/bin/chamber \  
&& chmod +x /bin/terraform-provider-buildkite  


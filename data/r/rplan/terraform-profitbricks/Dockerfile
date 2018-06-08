FROM hashicorp/terraform  
MAINTAINER "Actano GmbH"  
ARG PROFITPRICKS_PROVIDER_VERSION=1.0.5  
RUN curl -L https://github.com/profitbricks/terraform-provider-
profitbricks/releases/download/v${PROFITPRICKS_PROVIDER_VERSION}/terraform-
provider-profitbricks-v${PROFITPRICKS_PROVIDER_VERSION}-linux-amd64.tar.gz >
terraform-provider-profitbricks-v${PROFITPRICKS_PROVIDER_VERSION}-linux-
amd64.tar.gz && \  
tar xfvz terraform-provider-
profitbricks-v${PROFITPRICKS_PROVIDER_VERSION}-linux-amd64.tar.gz -C /bin && \  
rm -f terraform-provider-profitbricks-v${PROFITBRICKS_PROVIDER_VERSION}.tar.gz  


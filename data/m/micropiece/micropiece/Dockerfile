ARG baseimage_version=v1.4  
FROM micropiece/micropiece-dockerbase:${baseimage_version}  
  
ARG micropiece_version=master  
ARG VCS_REF  
ARG BUILD_DATE  
  
RUN echo "VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}",
micropiece_version: "${micropiece_version}  
  
LABEL maintainer="frank.foerster@ime.fraunhofer.de" \  
description="Container for the microPIECE package" \  
version=${micropiece_version} \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/microPIECE-team/microPIECE"  
  
RUN apt update && apt install --yes --no-install-recommends git && \  
git clone \--branch ${micropiece_version} https://github.com/microPIECE-
team/microPIECE.git /opt/microPIECE && \  
rm -rf /opt/microPIECE/.git && \  
rm -rf /var/lib/apt/lists/*  
ENV PATH=/opt/microPIECE/:"$PATH"  


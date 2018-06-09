FROM java:openjdk-8  
ENV RENJIN_VERSION=0.9.2580  
# Install requirements and download & install .deb packge for Renjin  
WORKDIR /tmp  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
# Renjin requirements which are not resolved automatically:  
libblas3 \  
java-wrappers \  
&& curl -LO -#
https://nexus.bedatadriven.com/service/local/repositories/renjin-
release/content/org/renjin/renjin-debian-package/$RENJIN_VERSION/renjin-
debian-package-$RENJIN_VERSION.deb  
RUN dpkg -i renjin-debian-package-$RENJIN_VERSION.deb  
  
# Add image metadata  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
LABEL org.label-
schema.license="https://github.com/bedatadriven/renjin/blob/master/LICENSE.txt"
\  
org.label-schema.vendor="BeDataDriven, Dockerfile provided by Daniel Nüst" \  
org.label-schema.name="Renjin" \  
org.label-schema.description="JVM-based interpreter for the R language for the
statistical analysis." \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.renjin.version="0.9.2580" \  
org.label-schema.schema-version="rc1" \  
maintainer="Daniel Nüst <daniel.nuest@uni-muenster.de>"  
CMD ["renjin"]  


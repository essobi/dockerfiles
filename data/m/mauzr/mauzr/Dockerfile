FROM mauzr/base:imaging  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.schema-version=1.0 \  
org.label-schema.name=mauzr/mauzr:imaging \  
org.label-schema.vcs-url=https://github.com/mauzr/mauzr \  
org.label-schema.vcs-ref=${VCS_REF} \  
org.label-schema.build-date=${BUILD_DATE}  
  
ENV VCS_REF ${VCS_REF}  
RUN wget -qO- https://github.com/mauzr/mauzr/archive/${VCS_REF}.tar.gz | \  
tar xz -C / && mv /mauzr* /mauzr && \  
pip3 --no-cache install -U -e /mauzr  


FROM wernight/kubectl:1.6.1  
  
# add gettext for running envsubst  
USER root  
RUN set -x && \  
apk add \--update --no-cache gettext  
  
USER kubectl  


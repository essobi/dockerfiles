FROM busybox  
  
# If you were diligent, you would confirm this hash matches what's at  
# https://github.com/Yelp/dumb-init/releases/download/v1.2.1/sha256sums  
ENV DUMB_INIT_VERSION=1.2.1 \  
DUMB_INIT_SHA256=057ecd4ac1d3c3be31f82fc0848bf77b1326a975b4f8423fe31607205a0fe945  
  
RUN wget -q https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 -O /dumb-init && \  
chmod a+x /dumb-init  
RUN echo "${DUMB_INIT_SHA256} */dumb-init" | sha256sum -c -  
  
FROM scratch  
LABEL maintainer="David M. Lee, II <leedm777@yahoo.com>"  
COPY \--from=0 /dumb-init /  


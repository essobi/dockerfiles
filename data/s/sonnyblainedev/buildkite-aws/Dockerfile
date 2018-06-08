FROM buildkite/agent:beta  
  
ENV AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}  
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}  
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates curl groff less
coreutils && \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  


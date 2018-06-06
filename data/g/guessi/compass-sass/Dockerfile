FROM ruby:2.5-alpine3.7  
ENV BUILD_BASE /opt/workdir  
RUN apk add --no-cache gcc libc-dev make \  
&& gem install compass \  
&& mkdir -p ${BUILD_BASE}/css \  
${BUILD_BASE}/sass  
COPY sass-convert config.rb ${BUILD_BASE}/  
WORKDIR ${BUILD_BASE}  


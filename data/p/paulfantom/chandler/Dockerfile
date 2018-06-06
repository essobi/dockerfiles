FROM ruby:alpine  
  
LABEL maintainer="Whizark https://github.com/whizark"  
  
ENV CHANDLER_VERSION=latest \  
CHANDLER_WORKDIR=/chandler \  
CHANDLER_GITHUB_API_TOKEN=YOUR_GITHUB_API_TOKEN \  
PAGER=cat  
  
RUN apk add --no-cache git  
  
RUN if [[ "$CHANDLER_VERSION" == "latest" ]]; then \  
gem install chandler --no-document; \  
else \  
gem install chandler -v "${CHANDLER_VERSION}" \--no-document; \  
fi  
  
RUN if [[ ! -d "${CHANDLER_WORKDIR}" ]]; then \  
mkdir -p "${CHANDLER_WORKDIR}"; \  
fi  
  
WORKDIR ${CHANDLER_WORKDIR}  
  
ENTRYPOINT ["chandler"]  


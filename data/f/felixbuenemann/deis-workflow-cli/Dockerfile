FROM alpine:3.6  
MAINTAINER felix.buenemann@gmail.com  
  
ARG DEIS_WORKFLOW_CLI_VERSION=v2.18.0  
RUN apk add --no-cache bash curl git jq openssh-client \  
&& curl -fsSLO https://raw.githubusercontent.com/deis/deis.io/gh-pages/deis-
cli/install-v2.sh \  
&& bash install-v2.sh $DEIS_WORKFLOW_CLI_VERSION \  
&& mv deis /usr/bin/ \  
&& rm install-v2.sh \  
&& INSTALLED_VERSION="`deis version`" \  
&& test "$DEIS_WORKFLOW_CLI_VERSION" = stable \  
-o "$DEIS_WORKFLOW_CLI_VERSION" = "$INSTALLED_VERSION"  
  
COPY deis /usr/local/bin/  
COPY git /usr/local/bin/  
  
CMD ["deis"]  


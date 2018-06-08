FROM node:8.9.1-alpine  
  
MAINTAINER Manala <contact@manala.io>  
  
USER root  
  
# Packages  
RUN apk add --no-cache su-exec bash curl make git  
  
# Dumb init  
ENV DUMB_INIT_VERSION="1.2.1"  
RUN curl -fsSL https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 -o /usr/local/bin/dumb-init && \  
chmod +x /usr/local/bin/dumb-init  
  
# Goss  
ENV GOSS_VERSION="0.3.5"  
RUN curl -fsSL https://goss.rocks/install | GOSS_VER=v${GOSS_VERSION} sh  
  
# Entrypoint  
COPY entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["entrypoint.sh"]  
  
# Default command  
CMD ["/bin/bash"]  
  
# Working directory  
WORKDIR /srv  
  
########  
# User #  
########  
ARG USER_ID  
ARG GROUP_ID  
  
ENV USER_DEFAULT="lint" \  
USER_ID="${USER_ID:-1000}" \  
GROUP_DEFAULT="lint" \  
GROUP_ID="${GROUP_ID:-1000}"  
RUN deluser --remove-home node && \  
addgroup -g ${GROUP_ID} ${GROUP_DEFAULT} && \  
adduser -D -s /bin/bash -g ${USER_DEFAULT} -u ${USER_ID} -G ${GROUP_DEFAULT}
${USER_DEFAULT}  
  
##########  
# Custom #  
##########  
# Npm packages  
ENV STYLELINT_VERSION="7.10.1" \  
STYLELINT_SCSS_VERSION="1.4.3" \  
STYLELINT_CONFIG_STANDARD_VERSION="16.0.0" \  
STYLELINT_CONFIG_ELAO_VERSION="0.4.1" \  
STYLELINT_FORMATTER_RELATIVE_JUNIT_VERSION="0.0.2" \  
STYLEFMT_VERSION="5.3.2"  
RUN npm --global install \  
stylelint@${STYLELINT_VERSION} \  
stylelint-scss@${STYLELINT_SCSS_VERSION} \  
stylelint-config-standard@${STYLELINT_CONFIG_STANDARD_VERSION} \  
stylelint-config-elao@${STYLELINT_CONFIG_ELAO_VERSION} \  
stylelint-formatter-relative-
junit@${STYLELINT_FORMATTER_RELATIVE_JUNIT_VERSION} \  
stylefmt@${STYLEFMT_VERSION} \  
&& rm -rf /root/.npm  


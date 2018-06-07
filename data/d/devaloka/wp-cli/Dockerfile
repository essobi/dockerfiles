FROM php:7-alpine  
  
LABEL maintainer="Whizark https://github.com/whizark"  
  
ENV WP_CLI_VERSION=latest \  
WP_CLI_OWNER=wp-cli \  
WP_CLI_UID=1000 \  
WP_CLI_GROUP=www-data \  
WP_CLI_GID=82 \  
WP_CLI_WORKDIR=/wp-cli \  
PAGER=cat  
  
RUN if [[ "$WP_CLI_VERSION" == "latest" ]]; then \  
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar; \  
else \  
curl -L -o wp-cli.phar "https://github.com/wp-cli/wp-
cli/releases/download/v{$WP_CLI_VERSION}/wp-cli-${WP_CLI_VERSION}.phar"; \  
fi \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
RUN if ! getent group "${WP_CLI_GROUP}" >/dev/null 2>&1; then \  
addgroup -g "${WP_CLI_GID}" -S "${WP_CLI_GROUP}"; \  
fi \  
&& if ! id "$1" >/dev/null 2>&1; then \  
adduser -G "${WP_CLI_GROUP}" -S -D -H -u "${WP_CLI_UID}" "${WP_CLI_OWNER}"; \  
fi \  
&& if [[ ! -d "${WP_CLI_WORKDIR}" ]]; then \  
mkdir -p "${WP_CLI_WORKDIR}"; \  
chown -R "${WP_CLI_OWNER}":"${WP_CLI_GROUP}" "${WP_CLI_WORKDIR}"; \  
fi  
  
WORKDIR ${WP_CLI_WORKDIR}  
  
USER ${WP_CLI_OWNER}  
  
ENTRYPOINT ["/usr/local/bin/wp"]  


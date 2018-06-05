FROM php:7.0-alpine  
  
# Required by phpcbf  
RUN apk add --no-cache patch  
  
# To build under proxy, use: docker build --build-arg "http_proxy=$http_proxy"  
RUN if test -n "$http_proxy"; then pear config-set http_proxy "$http_proxy";
fi  
  
RUN pear install PHP_CodeSniffer-2.7.0  
  
# Install the WordPress rules  
ENV WPCS_VERSION 0.10.0  
ADD https://github.com/WordPress-Coding-Standards/WordPress-Coding-
Standards/archive/${WPCS_VERSION}.zip /wpcs.zip  
RUN unzip /wpcs.zip -d / && \  
phpcs --config-set installed_paths /WordPress-Coding-Standards-${WPCS_VERSION}  


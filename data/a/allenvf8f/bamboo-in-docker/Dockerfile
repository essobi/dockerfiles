FROM openjdk:alpine  
  
LABEL maintainer="Allen Vaillienourt <allen.vaillienourt@forty8fiftylabs.com>"  
  
ARG BAMBOO_VERSION=6.4.1  
ENV BAMBOO_INSTALL=/opt/atlassian/bamboo  
ENV BAMBOO_HOME=/var/atlassian/bamboo  
  
RUN set -xe \  
&& apk add --update --no-cache bash which gzip vim curl openssh php7 php7-cli
php7-phar docker \  
&& rm -rf /var/cache/apk/*  
  
# Adding PHP support and unit testing for Bamboo agent  
RUN wget -O phpunit https://phar.phpunit.de/phpunit-7.phar \  
&& chmod +x phpunit \  
&& mv phpunit /usr/local/bin/phpunit  
  
RUN addgroup -g 50000 bamboo && adduser bamboo -u 50000 -G bamboo -s /bin/sh
-D  
  
RUN set -xe \  
&& mkdir -p "${BAMBOO_HOME}" \  
&& mkdir -p "${BAMBOO_INSTALL}" \  
&& chown -R bamboo:bamboo "${BAMBOO_INSTALL}"/ \  
&& chown -R bamboo:bamboo "${BAMBOO_HOME}"/  
  
#USER bamboo  
RUN set -x \  
&& curl -Ls
"https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz" | tar -xz --directory "${BAMBOO_INSTALL}"
\--strip-components=1 --no-same-owner \  
&& echo "bamboo.home=/var/atlassian/bamboo" >> ${BAMBOO_INSTALL}/atlassian-
bamboo/WEB-INF/classes/bamboo-application.properties  
  
EXPOSE 8085 54663  
VOLUME [ "/var/atlassian/bamboo", "/opt/atlassian/bamboo/logs" ]  
  
WORKDIR $BAMBOO_HOME  
  
CMD ["/opt/atlassian/bamboo/bin/start-bamboo.sh", "-fg"]  
  


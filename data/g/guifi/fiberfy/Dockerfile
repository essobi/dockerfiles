# Set the base image  
FROM debian:stretch  
  
LABEL net.guifi.vendor="Fundacio guifi.net"  
LABEL version="1.0"  
LABEL description="This docker image is ready for \  
developing with guifi.net fiberfy."  
LABEL maintainer="roger.garcia@guifi.net"  
  
ENV NODE_ROOT_DIR /usr/share/node  
ENV FIBERFY_UNIX_USER fiberfy  
ENV FIBERFY_USER_ID 1000  
ENV FIBERFY_USER_GID 1000  
ENV FIBERFY_GIT_REPO https://github.com/guifi/fiberfy-server.git  
ENV FIBERFY_GIT_BRANCH sails  
  
RUN apt-get update && apt-get dist-upgrade -y \  
&& apt-get install -y curl wget git gnupg gosu python pkg-config \  
libcairo2-dev libjpeg62-turbo-dev libpango1.0-dev libgif-dev \  
mariadb-client \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Installing nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | xargs -0 bash -c \  
&& apt-get install -y nodejs  
  
# Installing sails globally  
RUN npm install sails -g  
  
# Installing database waterline-auto tool  
RUN npm install waterline-auto -g  
  
# Preparing development dir  
RUN mkdir -p /usr/share/node/  
  
# Creating UNIX User for development (security reasons)  
RUN groupadd --gid "${FIBERFY_USER_GID}" "${FIBERFY_UNIX_USER}" && \  
useradd \  
\--uid ${FIBERFY_USER_ID} \  
\--gid ${FIBERFY_USER_GID} \  
\--create-home \  
\--shell /bin/bash \  
${FIBERFY_UNIX_USER}  
  
# Define Volume for Drupal  
VOLUME ${NODE_ROOT_DIR}/fiberfy  
  
# Copy entrypoints  
COPY ./docker-entrypoint.sh /  
COPY ./fiberfy-entry.pl /  
  
# Copying script for setting userid and gid (host)  
COPY user-mapping.sh /  
RUN chmod u+x user-mapping.sh  
  
WORKDIR ${NODE_ROOT_DIR}/fiberfy  
  
EXPOSE 3000  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/bin/bash"]  


FROM node:8.1.4  
  
ARG AS_USER=root  
ARG AS_UID=0  
ARG AS_GID=0  
  
ENV APPDIR /usr/src/app  
ENV DEBIAN_FRONTEND noninteractive  
ENV REUID_UID 2342  
  
# Packages  
RUN apt-get update \  
&& apt-get install -y netcat \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#RUN [ ${AS_UID} -gt 500 -a $(getent passwd ${AS_UID}) ] && \  
# { REUID_USER=$(getent passwd ${AS_UID} | awk -F: '{print $1}') \  
# && usermod -u ${REUID_UID} ${REUID_USER} \  
# && find / -path /proc -prune -o -uid ${AS_UID} -exec chown ${REUID_USER} {}
\; -print \  
# && echo "-----> Changed UID for ${REUID_USER} to ${REUID_UID}"; \  
# } || { echo -n ""; } \  
# && [ ${AS_USER} != 'root' ] && { \  
# useradd ${AS_USER} -u ${AS_UID} -g ${AS_GID}; \  
# } || { echo -n ""; } \  
# && echo "-----> Preparing for user [`id ${AS_USER}`]" \  
# && mkdir -p ${APPDIR} \  
# && mkdir -p /home/${AS_USER} \  
# && chown ${AS_USER} ${APPDIR} /home/${AS_USER}  
  
#USER ${AS_USER}  
WORKDIR ${APPDIR}  
  
# install dependencies  
COPY package.json ${APPDIR}  
COPY yarn.lock ${APPDIR}  
RUN yarn install  
  
# Linting  
COPY .eslintrc ${APPDIR}  
COPY .eslintignore ${APPDIR}  
  
# javascript ES2017 syntax for testing  
COPY .babelrc ${APPDIR}  
  
# TEST runner setup  
# COPY setup-jasmine-env.js ${APPDIR}  
  
# Entrypoint related  
COPY docker/entrypoint.sh /entrypoint.sh  
COPY docker/entrypoint.d /entrypoint.d  
  
# Applicatin sources  
COPY / ${APPDIR}  
  
ENTRYPOINT ["/usr/src/app/docker/entrypoint.sh"]  
# CMD ["npm", "start"]  


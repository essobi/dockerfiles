# Adapted from a solution maintained by Tudor Marghidanu  
FROM ubuntu:xenial  
LABEL maintainer="Perfumister <hey@perfumister.com>"  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y \  
apt-utils build-essential locales git curl \  
perl pinto  
RUN locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales  
RUN apt-get autoclean  
  
ENV PINTO_REPOSITORY_ROOT=/var/lib/pinto/repository/default \  
PINTO_USERNAME=pinto \  
PINTO_AUTHOR_ID=pinto  
  
RUN rm -rf ${PINTO_REPOSITORY_ROOT} && \  
mkdir -p ${PINTO_REPOSITORY_ROOT}  
  
COPY ./entrypoint.sh /  
RUN chmod a+x /entrypoint.sh  
  
EXPOSE 3111  
VOLUME [ "${PINTO_REPOSITORY_ROOT}" ]  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "pintod" ]  


FROM ubuntu:trusty  
  
MAINTAINER Tudor Marghidanu  
  
ENV PINTO_REPOSITORY_ROOT /opt/pinto  
ENV PINTO_USERNAME pinto  
ENV PINTO_AUTHOR_ID pinto  
  
RUN apt-get update; apt-get install -y build-essential curl  
  
RUN curl -sL http://cpanmin.us | perl - App::cpanminus  
RUN cpanm --notest Pinto  
  
RUN mkdir -p ${PINTO_REPOSITORY_ROOT}  
  
EXPOSE 3111  
VOLUME [ "${PINTO_REPOSITORY_ROOT}" ]  
  
COPY ./entrypoint.sh /  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "pintod" ]  


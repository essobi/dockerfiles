FROM debian:jessie  
  
CMD ["remmina"]  
  
ENTRYPOINT ["remmina"]  
  
RUN apt-get update \  
&& apt-get install -y remmina  
  
ARG BUILD_DATE  
ARG GIT_SHA  
ARG SCHEMA=org.label-schema  
ARG SITE=site.gruen  
  
LABEL ${SCHEMA}.build-date=${BUILD_DATE} \  
${SCHEMA}.vcs-ref=${GIT_SHA} \  
${SCHEMA}.vendor="gruen" \  
${SCHEMA}.name="remmina" \  
${SITE}.author="Darren Green <darren@gruen.site>" \  
${SITE}.tag="debian-jessie"  
  


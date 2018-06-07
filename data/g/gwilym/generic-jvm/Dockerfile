ARG BASEREPO=openjdk  
ARG BASETAG=8u131-jre-alpine  
FROM ${BASEREPO}:${BASETAG}  
ARG BASEREPO  
ENV BASEREPO="${BASEREPO}"  
ARG BASETAG  
ENV BASETAG="${BASETAG}"  
COPY include /usr/local/docker-generic-jvm  
RUN /usr/local/docker-generic-jvm/build.sh "${BASEREPO}" "${BASETAG}"  
CMD ["/usr/local/docker-generic-jvm/bootstrap.sh", "${BASEREPO}",
"${BASETAG}"]  


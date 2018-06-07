FROM python:3-alpine3.6  
MAINTAINER Sylvain Desbureaux <sylvain@desbureaux.fr>  
  
ARG VCS_REF="1cf58e3"  
ARG BUILD_DATE="2018-02-15T16:06:39Z"  
  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/adrienverge/yamllint" \  
org.label-schema.url="https://yamllint.readthedocs.io/" \  
org.label-schema.name="YAML Lint" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="GPLv3" \  
org.label-schema.build-date=$BUILD_DATE  
  
WORKDIR /yaml  
  
RUN pip install yamllint && \  
rm -rf ~/.cache/pip  
  
CMD ["yamllint", "--version"]  


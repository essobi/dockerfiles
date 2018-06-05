FROM jruby:9.1.17.0-jre-alpine  
  
# cf.:  
# - https://docs.docker.com/docker-cloud/builds/advanced/#environment-
variables-for-building-and-testing  
# - https://medium.com/microscaling-systems/labelling-automated-builds-on-
docker-hub-f3d073fb8e1  
# - https://docs.docker.com/docker-cloud/builds/advanced/#override-build-test-
or-push-commands  
ARG BUILD_DATE  
ARG VCS_REF  
ARG DOCKER_TAG  
  
# cf.: http://label-schema.org/rc1/  
LABEL author="Awesome Incremented <marcel.koertgen@gmail.com>"\  
org.label-schema.build-date="${BUILD_DATE}" \  
org.label-schema.name="awesomeinc/elastic_provisioner" \  
org.label-schema.description="Import & export Elasticsearch data, e.g. Kibana
dashboards & configuration." \  
org.label-schema.usage="https://github.com/awesome-
inc/elastic_provisioner/blob/master/README.md" \  
org.label-schema.url="https://hub.docker.com/r/awesomeinc/elastic_provisioner"
\  
org.label-schema.vcs-url="https://github.com/awesome-inc/elastic_provisioner"
\  
org.label-schema.vcs-ref="${VCS_REF}" \  
org.label-schema.vendor="Awesome Inc" \  
org.label-schema.version="${DOCKER_TAG}" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.cmd="docker run
awesomeinc/elastic_provisioner:${DOCKER_TAG}"  
# TODO: even more labels...  
  
WORKDIR /app  
  
ADD . ./  
  
ENTRYPOINT [ "ruby" ]  
  
CMD [ "provision.rb" ]  


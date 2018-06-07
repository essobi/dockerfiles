FROM docker:17.10.0-ce-dind  
  
ARG version="0.1.0-dev"  
ARG build_date="unknown"  
ARG commit_hash="unknown"  
ARG vcs_url="unknown"  
ARG vcs_branch="unknown"  
  
ENV DOCKER_COMPOSE_VERSION 1.17.1  
  
LABEL org.label-schema.vendor="softonic" \  
org.label-schema.name="stack-running" \  
org.label-schema.description="Waits until a stack is running" \  
org.label-schema.usage="/src/README.md" \  
org.label-schema.url="https://github.com/softonic/docker-stack-
running/blob/master/README.md" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$commit_hash \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$build_date \  
org.label-schema.docker.cmd="docker run --rm \  
-v /var/run/docker.sock:/var/run/docker.sock:ro \  
-e TIMEOUT=30 \  
-e EXPECTED_SERVICES=3 \  
-e STACK_NAME=myStack \  
softonic/stack-is-up" \  
org.label-schema.docker.params="TIMEOUT=Max number of seconds before assume
something gone wrong \  
EXPECTED_SERVICES=Number of expected services running \  
STACK_NAME=Stack name used when launching the compose file \  
VERBOSE=Output container name if activated (1 for active, 0 for disabled.
Defaults to 0)"  
  
COPY ./get-stack-running.sh /get-stack-running.sh  
  
WORKDIR /project  
  
CMD ["/get-stack-running.sh"]  


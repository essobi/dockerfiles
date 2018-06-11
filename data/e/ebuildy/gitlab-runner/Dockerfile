FROM debian:8.5  
ARG VERSION=1.6.0  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-
init_1.0.2_amd64 \  
/usr/bin/dumb-init  
  
ADD https://gitlab-ci-multi-runner-
downloads.s3.amazonaws.com/v${VERSION}/binaries/gitlab-ci-multi-runner-linux-
amd64 \  
/usr/local/bin/gitlab-ci-multi-runner  
  
RUN chmod +x /usr/bin/dumb-init /usr/local/bin/gitlab-ci-multi-runner  
  
VOLUME /opt/gitlab/runner  
  
ENTRYPOINT ["dumb-init", "gitlab-ci-multi-runner"]  


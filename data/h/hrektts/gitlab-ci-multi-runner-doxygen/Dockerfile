FROM sameersbn/gitlab-ci-multi-runner:1.1.4-5  
MAINTAINER mps299792458@gmail.com  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y doxygen graphviz \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /home/gitlab_ci_multi_runner/doc \  
&& chown gitlab_ci_multi_runner:gitlab_ci_multi_runner
/home/gitlab_ci_multi_runner/doc  
  
WORKDIR "${GITLAB_CI_MULTI_RUNNER_HOME_DIR}"  
  
ENV RUNNER_DESCRIPTION=doxygen  
ENV RUNNER_EXECUTOR=shell  
ENV RUNNER_TAG_LIST="doxygen"  
ENV RUNNER_LIMIT=1  
ENV RUNNER_TOKEN=  
ENV CI_SERVER_URL=  


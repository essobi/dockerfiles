# Trigger.  
FROM jenkins  
  
RUN /usr/local/bin/install-plugins.sh docker-plugin docker-slaves docker-
build-step bitbucket bitbucket-oauth \  
github github-oauth ghprb github-branch-source workflow-aggregator \  
chef-identity chef-tracking uno-choice deployment-notification terraform
pipeline-graph-analysis \  
workflow-support workflow-job job-dsl git-changelog git-notes tracking-git
ansicolor \  
branch-api clone-workspace-scm disk-usage email-ext envinject extended-choice-
parameter extensible-choice-parameter \  
git git-client graphiteIntegrator greenballs jquery junit-attachments mask-
passwords mesos \  
metrics metrics-diskusage metrics-graphite multiple-scms packer parameterized-
trigger pegdown-formatter \  
promoted-builds publish-over-ssh rake ruby ruby-runtime scm-api scm-sync-
configuration simple-theme-plugin \  
slack ssh-credentials timestamper token-macro vagrant xshell  
  
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  
  
# if we want to install via apt  
USER root  
RUN apt-get update && apt-get install -y groovy  
RUN cd /usr/local/bin; wget
https://releases.hashicorp.com/terraform/0.8.2/terraform_0.8.2_linux_amd64.zip;
unzip -j terraform_*.zip; rm terraform_*.zip  
  
# USER jenkins # drop back to the regular jenkins user - good practice  


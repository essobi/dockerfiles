FROM centos:7  
LABEL INSTALL="docker run --rm --privileged --entrypoint=bash -v /:/host -e
HOST=/host -e IMAGE=IMAGE -e NAME=NAME IMAGE /bin/install.sh"  
LABEL UNINSTALL="docker run --rm --privileged --entrypoint=bash -v /:/host -e
HOST=/host -e IMAGE=IMAGE -e NAME=NAME IMAGE /bin/uninstall.sh"  
  
RUN curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-
runner/script.rpm.sh | bash && yum -y install gitlab-runner-10.8.0  
ADD atomic /  
  
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]  
ENTRYPOINT ["/usr/bin/gitlab-runner"]  


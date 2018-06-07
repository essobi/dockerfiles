FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y curl && \  
curl https://packagecloud.io/install/repositories/ayufan/gitlab-ci-multi-
runner/script.deb | sudo bash && \  
apt-get install -y gitlab-ci-multi-runner && \  
rm -rf /var/lib/apt/lists/*  
  
ADD digitallyseamless_root_ca.crt /usr/local/share/ca-
certificates/DIGITALLY_SEAMLESS_ROOT_CA.crt  
RUN update-ca-certificates --fresh  
  
WORKDIR /home/gitlab_ci_multi_runner  
  
ENTRYPOINT ["gitlab-ci-multi-runner"]  
CMD ["run"]  


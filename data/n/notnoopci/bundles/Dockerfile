FROM node:latest  
  
# make Apt non-interactive  
RUN echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90circleci \  
&& echo 'APT::Get::force-Yes "true";' >> /etc/apt/apt.conf.d/90circleci \  
&& echo 'DPkg::Options "--force-confnew";' >> /etc/apt/apt.conf.d/90circleci  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get install -y \  
git mercurial \  
locales sudo openssh-client ca-certificates tar gzip parallel \  
net-tools netcat jq unzip zip  
  
# Set timezone to UTC by default  
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime  
  
# Use unicode  
RUN locale-gen C.UTF-8 || true  
ENV LANG=C.UTF-8  
RUN groupadd --gid 3434 circleci \  
&& useradd --uid 3434 --gid circleci --shell /bin/bash --create-home circleci
\  
&& echo 'circleci ALL=NOPASSWD: ALL' >> /etc/sudoers.d/50-circleci \  
&& echo 'Defaults env_keep += "DEBIAN_FRONTEND"' >> /etc/sudoers.d/env_keep  
  
# BEGIN IMAGE CUSTOMIZATIONS  
# END IMAGE CUSTOMIZATIONS  
USER circleci  
  
CMD ["/bin/sh"]  


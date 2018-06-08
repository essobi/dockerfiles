FROM cloudbees/jnlp-slave-with-java-build-tools  
MAINTAINER Jeremy T. Bouse <Jeremy.Bouse@SterlingTS.com>  
  
USER root  
  
# Add Microsoft .Net Core repository  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
/etc/apt/trusted.gpg.d/microsoft.gpg \  
&& echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-
ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list  
  
# Install Docker and setup docker GID group membership for jenkins  
# Install jQuery and create jq-linux64 symlink  
# Insdtall nuget, mono and .Net core SDK  
# Upgrade aws-cli  
RUN apt -qqy update \  
&& apt -qqy upgrade \  
&& pip install --upgrade awscli \  
&& apt -qqy autoremove \  
&& addgroup --system --gid 497 docker \  
&& apt -qqy --no-install-recommends install docker.io jq nuget dotnet-
sdk-2.0.0 \  
&& usermod -a -G docker jenkins \  
&& usermod -a -G staff jenkins \  
&& ln -sf /usr/bin/jq /usr/bin/jq-linux64 \  
&& rm -rf /var/lib/apt/lists/*  
  
USER jenkins


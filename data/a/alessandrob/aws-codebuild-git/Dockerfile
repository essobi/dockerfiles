FROM debian:stretch  
  
RUN apt-get update \  
&& apt-get install -y \  
curl git ssh-client python-pip \  
&& pip install awscli \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
# Install codebuild extras  
RUN set -x \  
&& curl -fsSL -o /usr/local/bin/codebuild-extras
https://raw.githubusercontent.com/alessandrobologna/aws-codebuild-
extras/master/install \  
&& chmod +x /usr/local/bin/codebuild-extras  
  
ADD docker-entrypoint /  
ADD git-tagger /usr/local/bin/git-tagger  
RUN chmod +x /usr/local/bin/git-tagger  
  
ENTRYPOINT ["/docker-entrypoint"]


FROM n0ts/docker-aws  
  
MAINTAINER Naoya Nakazawa <naoya.n@gmail.com>  
  
RUN set -x \  
&& apk --no-cache add openssh \  
  
&& curl -o /usr/local/bin/circleci https://circle-
downloads.s3.amazonaws.com/releases/build_agent_wrapper/circleci \  
&& chmod +x /usr/local/bin/circleci  
  
ENTRYPOINT ["dockerd-entrypoint.sh"]  
CMD []  


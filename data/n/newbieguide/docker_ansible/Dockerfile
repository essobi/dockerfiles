FROM docker  
  
ENV TIME_ZONE Europe/London  
ENV PATH /root/.local/bin:$PATH  
  
RUN apk update \  
&& apk upgrade \  
&& apk add \--update bash && rm -rf /var/cache/apk/* \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/v3.6/community" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/v3.6/main" >>
/etc/apk/repositories \  
&& apk --update add unzip \  
&& apk add \--no-cache curl \  
&& apk add ca-certificates \  
&& apk add openntpd \  
&& apk add tzdata \  
&& echo "${TIME_ZONE}" > /etc/timezone \  
&& ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime  
  
RUN apk --update add ansible  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \--user \  
&& pip install docker-py \  
&& pip install awscli --upgrade --user \  
&& aws --version  
  
RUN pip install boto \  
&& pip install boto3  
  
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-
cli/ecs-cli-linux-amd64-latest \  
&& chmod +x /usr/local/bin/ecs-cli \  
&& ecs-cli --version  


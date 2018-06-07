FROM alpine:3.5  
MAINTAINER Hoa Duong <duongxuanhoa@gmail.com>  
  
RUN apk add --update --no-cache g++ make python tmux curl nodejs bash openssh-
client git py-pip python-dev \  
&& rm -rf /var/cache/apk/*  
  
RUN git clone -b master --single-branch git://github.com/c9/core.git
/opt/cloud9 \  
&& curl -s -L https://raw.githubusercontent.com/c9/install/master/link.sh |
bash \  
&& /opt/cloud9/scripts/install-sdk.sh \  
&& rm -rf /opt/cloud9/.git \  
&& rm -rf /tmp/* \  
&& npm cache clean  
  
RUN pip install -U pip \  
&& pip install -U virtualenv \  
&& virtualenv --python=python2 $HOME/.c9/python2 \  
&& source $HOME/.c9/python2/bin/activate \  
&& mkdir /tmp/codeintel \  
&& pip install --download /tmp/codeintel codeintel==0.9.3 \  
&& cd /tmp/codeintel \  
&& tar xf CodeIntel-0.9.3.tar.gz \  
&& mv CodeIntel-0.9.3/SilverCity CodeIntel-0.9.3/silvercity \  
&& tar czf CodeIntel-0.9.3.tar.gz CodeIntel-0.9.3 \  
&& pip install -U --no-index --find-links=/tmp/codeintel codeintel \  
&& rm -rf /tmp/codeintel/*.gz /tmp/codeintel/*.whl  
  
RUN mkdir /workspace  
  
VOLUME /workspace  
  
WORKDIR /workspace  
  
ENV USERNAME username  
ENV PASSWORD password  
  
EXPOSE 8000  
ENTRYPOINT ["sh", "-c", "/usr/bin/node /opt/cloud9/server.js -l 0.0.0.0 -p
8000 -w /workspace -a $USERNAME:$PASSWORD"]  


FROM alpine  
LABEL "alpine-hubot 1.0"  
  
MAINTAINER Brandon Evers  
  
# Install dependencies  
RUN apk update && apk upgrade \  
&& apk add redis \  
&& apk add nodejs nodejs-npm \  
&& apk add python \  
&& apk add curl \  
&& curl -sS https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install awscli \  
&& npm install -g npm \  
&& npm install -g coffee-script \  
&& npm install -g yo generator-hubot \  
&& apk --purge -v del py-pip \  
&& rm -rf /var/cache/apk/*  
  
# Create hubot user  
RUN adduser -h /hubot -s /bin/bash -S hubot  
USER hubot  
WORKDIR /hubot  
  
# Install hubot  
RUN yo hubot --owner="Brandon Evers <bevers222@gmail.com>" \--name="ada"
\--description="A Detection Algorithm" \--defaults --adapter=slack  
COPY package.json package.json  
RUN npm install  
ADD hubot/hubot-scripts.json /hubot/  
ADD hubot/external-scripts.json /hubot/  
COPY scripts scripts/  
  
ENV HUBOT_SLACK_TOKEN xoxb-164473103668-pf24YScuu9wJpiczcUEazBY3  
ENV HUBOT_AUTH_ADMIN U4DGCGX36  
ENV HUBOT_CYCLE_TZ_NAME America/Chicago  
  
EXPOSE 80  
# And go  
ENTRYPOINT ["/bin/sh", "-c", "bin/hubot --adapter slack"]  


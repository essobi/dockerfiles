FROM alpine:3.4  
RUN apk update &&\  
apk upgrade &&\  
apk add build-base ansible docker git py-pip nodejs rsync zip &&\  
apk add --update libffi-dev python-dev openssl-dev &&\  
npm install -g yo generator-hubot &&\  
adduser -u 497 -h /mmmbot -D hubot hubot &&\  
pip install awscli boto boto3 credstash virtualenv  
USER hubot  
WORKDIR /mmmbot  
RUN yo hubot --owner="mmmbot <mmmbot42@gmail.com>" \--name="mmmbot"
\--description="like but also unlike, the band" \--adapter slack --defaults  
RUN npm install --save
https://github.com/mGageTechOps/hubot-s3-brain/tarball/master &&\  
npm install hubot-jenkins-enhanced --save &&\  
npm install shelljs --save &&\  
npm install hubot-alias --save  
ADD external-scripts.json .  
ADD build-pb.coffee ./scripts/build-pb.coffee  
ADD build-docker.coffee ./scripts/build-docker.coffee  
ADD build-lambda.coffee ./scripts/build-lambda.coffee  
CMD HUBOT_SLACK_TOKEN=$(credstash -r ${CREDSTASH_REGION} get -n
${CREDSTASH_REF_SLACKTOKEN}) \  
HUBOT_GOOGLE_CSE_ID=$(credstash -r ${CREDSTASH_REGION} get -n
${CREDSTASH_REF_CSE_ID}) \  
HUBOT_GOOGLE_CSE_KEY=$(credstash -r ${CREDSTASH_REGION} get -n
${CREDSTASH_REF_CSE_KEY}) \  
bin/hubot --adapter slack  


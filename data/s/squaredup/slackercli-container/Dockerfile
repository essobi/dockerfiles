FROM python:3  
RUN pip install slacker-cli  
  
ENV SLACK_TOKEN "InvalidToken"  
ENV MESSAGE "Hello world"  
ENV CHANNEL "builds"  
ENV NAME "jenkins"  
ENV EMOJI_AVATAR ":hammer:"  
CMD echo $MESSAGE | slacker -c $CHANNEL -t $SLACK_TOKEN -n $NAME -i
$EMOJI_AVATAR


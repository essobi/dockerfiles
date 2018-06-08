FROM ubuntu:12.04  
MAINTAINER Oliver Letterer <oliver.letterer@sparrow-labs.de>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y curl && apt-get clean  
  
ENV API_KEY my_api_key  
ENV DOMAIN my_domain.com  
ENV HOST my_host  
ENV SUBJECT started  
ENV BODY Action is required  
  
CMD /bin/bash -c "curl -s --user 'api:$API_KEY'
https://api.mailgun.net/v2/$DOMAIN/messages -F from='$HOST@$DOMAIN' -F
to='oliver.letterer@sparrow-labs.de' -F subject='$SUBJECT' -F text='$BODY'"  


#########################################################  
## ##  
## _ ##  
## __ _ _ __ __ _(_)_ __ ___ ##  
## / _` | '__/ _` | | '_ \ / _ \ ##  
## | (_| | | | (_| | | | | | __/ ##  
## \\__, |_| \\__,_|_|_| |_|\\___| ##  
## |___/ ##  
## ##  
## ##  
##-----------------------------------------------------##  
## ##  
## ssl-auto Docker By Mathieu Lescaudron ##  
## ##  
## V 1.0 Created on 25/11/2017 ##  
## ##  
#########################################################  
  
# INTRODUCTION  
#  
# Letsencrypt with certbot who generate or update domain for you  
  
# BUILD INSTRUCTION  
#  
# docker build -t graine/ssl-auto:latest .  
  
# RUN INSTRUCTION  
#  
# docker run -ti -v /home/ubuntu/config/letsencrypt:/etc/letsencrypt -v
/tmp:/config graine/ssl domain.com you@mail.com  
  
FROM certbot/certbot  
  
RUN apk add --update curl && rm -rf /var/cache/apk/*  
  
WORKDIR /home  
  
ADD generate.sh /generate  
RUN chmod +x /generate  
  
ENTRYPOINT [ "/generate" ]


FROM nouchka/hackmyresume-web as builder  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
LABEL org.label-schema.vcs-
url="https://github.com/nouchka/japromis.katagena.com"  
LABEL version="latest"  
  
ENV RESUME_JSON_URL
https://raw.githubusercontent.com/nouchka/japromis.katagena.com/master/fr.json  
ENV OUTPUT_TEMPLATE kendall  
ENV EMAIL docker@katagena.com  
ENV PHONE +33602030405  
ENV ADDRESS 25 Rue Delphin Loche  
  
COPY resume-start.sh /resume-start.sh  
COPY resume.json /usr/share/nginx/html/resume.json  
RUN /resume-start.sh  
  
FROM nginx  
COPY \--from=builder /var/www/html /usr/share/nginx/html  


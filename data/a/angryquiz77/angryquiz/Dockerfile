FROM tomcat:7.0.82-jre8-alpine  
  
MAINTAINER AngryQuiz <angryquiz77@gmail.com>  
  
ENV QUESTION_REST_URL \  
https://github.com/angryquiz/maven-repo/raw/master/com/question/rest/question-
rest/1.0.0/question-rest-1.0.0.war  
  
ENV QUESTION_BANK_URL \  
https://github.com/angryquiz/maven-
repo/raw/master/com/questionbank/app/question-bank/1.0.0/question-
bank-1.0.0.war  
  
ENV QUESTION_SETENV_URL \  
https://raw.githubusercontent.com/angryquiz/docker/master/setenv.sh  
  
ENV QUESTION_FRONTEND_URL \  
https://github.com/angryquiz/maven-repo-
branches/raw/angryquiz-1.0.0/com/question/static/question-
static/1.0.0/question-static-1.0.0.war  
  
  
RUN set -eux; \  
\  
apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
openssl \  
; \  
\  
success=; \  
for url in $QUESTION_REST_URL; do \  
if wget -O question-rest.war "$url"; then \  
success=1; \  
break; \  
fi; \  
done; \  
[ -n "$success" ]; \  
\  
success=; \  
for url in $QUESTION_BANK_URL; do \  
if wget -O question-bank.war "$url"; then \  
success=1; \  
break; \  
fi; \  
done; \  
[ -n "$success" ]; \  
\  
success=; \  
for url in $QUESTION_SETENV_URL; do \  
if wget -O setenv.sh "$url"; then \  
success=1; \  
break; \  
fi; \  
done; \  
[ -n "$success" ]; \  
\  
success=; \  
for url in $QUESTION_FRONTEND_URL; do \  
if wget -O ROOT.war "$url"; then \  
success=1; \  
break; \  
fi; \  
done; \  
[ -n "$success" ]; \  
\  
cp $CATALINA_HOME/question-rest.war $CATALINA_HOME/webapps; \  
cp $CATALINA_HOME/question-bank.war $CATALINA_HOME/webapps; \  
rm -rf $CATALINA_HOME/webapps/ROOT; \  
cp $CATALINA_HOME/ROOT.war $CATALINA_HOME/webapps; \  
cp $CATALINA_HOME/setenv.sh $CATALINA_HOME/bin; \  
\  
rm $CATALINA_HOME/question-rest.war; \  
rm $CATALINA_HOME/question-bank.war; \  
rm $CATALINA_HOME/ROOT.war; \  
[ -n "$success" ];  
  
  
  
  
  


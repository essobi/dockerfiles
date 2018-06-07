FROM frolvlad/alpine-oraclejdk8:slim  
  
MAINTAINER think@hotmail.de  
  
RUN apk --update add ruby ruby-dev build-base ruby-rdoc ruby-irb ca-
certificates openssl \  
&& gem install gherkin_language json --no-format-exec \  
&& echo "Feature: Empty" > /tmp/empty.feature \  
&& gherkin_language /tmp/empty.feature \  
&& rm /tmp/empty.feature \  
&& apk del ruby-dev build-base ruby-rdoc ruby-irb ca-certificates openssl \  
&& rm -rf /var/cache/apk \  
&& (cd /tmp/LanguageTool*/org/languagetool/resource/ && ls -1 . | grep -v en |
xargs rm -rf)  
  
ENTRYPOINT ["gherkin_language"]  
CMD ["--help"]  


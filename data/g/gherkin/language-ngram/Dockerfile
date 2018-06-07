FROM gherkin/ngram-data:20150817  
  
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
xargs rm -rf) \  
&& mkdir -p /tmp/ngrams-en-20150817 \  
&& ln -s /ngrams /tmp/ngrams-en-20150817/en  
  
ENTRYPOINT ["gherkin_language", "--ngram"]  
CMD ["--help"]  


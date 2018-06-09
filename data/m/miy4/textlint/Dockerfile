FROM gliderlabs/alpine:3.4  
MAINTAINER miy4 <miy4t7l@gmail.com>  
  
ENV TEXTLINT_VERSION=7.1.4  
RUN apk add --no-cache nodejs \  
&& npm install -g textlint@${TEXTLINT_VERSION} \  
&& npm install -g \  
textlint-rule-preset-jtf-style \  
textlint-rule-max-ten \  
textlint-rule-no-doubled-joshi \  
textlint-rule-no-mix-dearu-desumasu \  
textlint-rule-sentence-length \  
textlint-rule-spellcheck-tech-word  
  
ENTRYPOINT ["textlint"]  
CMD ["-h"]  


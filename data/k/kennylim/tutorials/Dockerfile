FROM docs/base:latest  
MAINTAINER Mary Anthony <mary@docker.com> (@moxiegirl)  
  
# To get the git info for this repo  
COPY . /src  
  
COPY . /docs/content/  
  
# Sed to process GitHub Markdown  
# 1-2 Remove comment code from metadata block  
# 3 Change ](/word to ](/project/ in links  
# 4 Change ](word.md) to ](/project/word)  
# 5 Remove .md extension from link text  
# 6 Change ](../ to ](/project/word)  
# 7 Change ](../../ to ](/project/ --> not implemented  
#  
#  
RUN find /docs/content -type f -name "*.md" -exec sed -i.old \  
-e '/^<!.*metadata]>/g' \  
-e '/^<!.*end-metadata.*>/g' {} \;  


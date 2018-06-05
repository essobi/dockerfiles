FROM benlubar/dwarffortress:dfhack-0.44.10-r1  
  
ENV DF_AI_VERSION=0.44.10-r1 \  
DF_AI_ARCHIVE_NAME=df-ai-0.44.10-r1-linux-64-4.8.tar.gz \  
DF_AI_ARCHIVE_SHA1=0763a4e6882c5f6e6086a81b47e569bc61d666d8 \  
DF_AI_ASSETS_SHA1=3b3af0e1914e332de4a40288ccb7a816fec26ae3 \  
WEBLEGENDS_VERSION=0.44.10-r1 \  
WEBLEGENDS_ARCHIVE_NAME=weblegends-0.44.10-r1-linux-64-4.8.tar.gz \  
WEBLEGENDS_ARCHIVE_SHA1=e664e6dc6f0261e499988d175d6bfd1c47a0528b  
  
RUN curl -LSo df-ai.tar.gz https://github.com/BenLubar/df-
ai/releases/download/${DF_AI_VERSION}/${DF_AI_ARCHIVE_NAME} \  
&& curl -LSo df-ai-assets.zip https://github.com/BenLubar/df-
ai/releases/download/${DF_AI_VERSION}/df-ai-assets.zip \  
&& curl -LSo weblegends.tar.gz
https://github.com/BenLubar/weblegends/releases/download/${WEBLEGENDS_VERSION}/${WEBLEGENDS_ARCHIVE_NAME}
\  
&& (echo "${DF_AI_ARCHIVE_SHA1} *df-ai.tar.gz"; \  
echo "${DF_AI_ASSETS_SHA1} *df-ai-assets.zip"; \  
echo "${WEBLEGENDS_ARCHIVE_SHA1} *weblegends.tar.gz") | sha1sum -c \  
&& tar -xzvf df-ai.tar.gz -C hack/plugins \  
&& unzip df-ai-assets.zip \  
&& tar -xzvf weblegends.tar.gz -C hack/plugins \  
&& rm -f df-ai.tar.gz df-ai-assets.zip weblegends.tar.gz \  
&& echo "enable df-ai" >> dfhack.init  
  
EXPOSE 5080  


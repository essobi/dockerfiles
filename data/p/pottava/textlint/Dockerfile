# textlint with reStructuredText support  
# docker run --rm -it -v $(pwd):/work pottava/textlint:10.2-rst .  
FROM pottava/textlint:10.2  
  
RUN yarn global add textlint-plugin-rst@0.1.1 \  
&& rm -rf /usr/local/share/.cache  
  
RUN apk --no-cache add python3 \  
&& pip3 install docutils-ast-writer  


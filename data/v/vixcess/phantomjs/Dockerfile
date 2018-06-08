FROM wernight/phantomjs:2  
LABEL maintainer="Shiqiao Du <lucidfrontier.45@gmail.com>"  
  
USER root  
  
RUN set -ex \  
&& pkgs=' \  
fontconfig \  
fonts-takao \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ${pkgs} \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY index.js /  
  
CMD ["phantomjs", "index.js"]  


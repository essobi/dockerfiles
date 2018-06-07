FROM node:6-slim  
LABEL maintainer="Shiqiao Du <lucidfrontier.45@gmail.com>"  
  
RUN set -ex \  
&& pkgs=' \  
bzip2 \  
fontconfig \  
fonts-takao \  
tar \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ${pkgs} \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV ACCEPT_HIGHCHARTS_LICENSE YES  
RUN npm install highcharts-export-server -g  
  
ENV WORKERS 4  
CMD highcharts-export-server --enableServer 1 --host 0.0.0.0 --port 3000
--workers $WORKERS  


# nginx is based on debia image  
FROM nginx  
  
MAINTAINER "Walter dos Santos Filho" <walter AT dcc.ufmg.br>  
  
# Install Nodejs  
RUN apt-get update && apt-get install -y \  
python2.7 \  
curl \  
gnupg2 \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get update && apt-get install -y nodejs \  
&& curl -o- -L https://yarnpkg.com/install.sh | bash \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CITRON_HOME=/usr/local/citron  
ENV CITRON_GVIZ_HOME=/usr/local/citron/lib/gviz  
  
COPY . $CITRON_HOME  
COPY extras/entrypoint.sh $CITRON_HOME  
COPY extras/update_env.py /usr/local/bin  
COPY extras/nginx.conf.sample /etc/nginx/conf.d/default.conf  
  
WORKDIR $CITRON_GVIZ_HOME  
RUN $HOME/.yarn/bin/yarn  
  
WORKDIR $CITRON_HOME  
RUN $HOME/.yarn/bin/yarn \  
&& ./node_modules/ember-cli/bin/ember build --prod  
  
EXPOSE 8080  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  
  


FROM alpine  
  
LABEL io.brasil="Brasil IO" \  
io.brasil.cli="foo" \  
version="0.1" \  
description="Imagem do Brasil.io para executar os código de extração de
dados." \  
maintainer="luiz@thenets.org"  
  
# Main dependencies  
RUN apk --no-cache add \  
python3 py3-pip git bash \  
python3-dev build-base gcc libxml2-dev libxslt-dev  
  
# Envs  
ENV HOME=/app \  
USER=brasilio  
  
# Setup Python  
WORKDIR $HOME  
RUN set -x \  
# Add user  
&& adduser -D -u 1000 -s /bin/bash $USER \  
# Setup virtualenv  
&& python3 -m pip install pip --upgrade \  
&& python3 -m pip install virtualenv \  
# Set permissions  
&& chown -R 1000.1000 $HOME  
  
# Copy files  
ADD entrypoint.sh $HOME/  
RUN set -x \  
# Add entrypoint file  
&& chmod +x $HOME/entrypoint.sh \  
# Create 'app' dir and empty file  
&& mkdir -p $HOME/src \  
&& echo 'print("Volume não foi montado em /app/src")' > $HOME/src/empty.py \  
# HACK to fix volumes permissions  
&& mkdir -p $HOME/env $HOME/src $HOME/package \  
# Set permissions  
&& chown -R 1000.1000 $HOME  
  
# Config  
USER $USER  
CMD ["/app/entrypoint.sh"]  
VOLUME ["$HOME/env", "$HOME/src", "$HOME/package"]


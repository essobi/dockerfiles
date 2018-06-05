FROM elixir:1.5-alpine  
  
LABEL author.name="Rodrigo Zampieri Castilho"  
LABEL author.email="rodrigo.zampieri@gmail.com"  
LABEL repository.url="https://bitbucket.org/rcastilho/cloud-assistant"  
  
ENV MIX_ENV=prod\  
PORT=4000\  
KUBE_LATEST_VERSION="v1.8.4"  
RUN apk add --update ca-certificates \  
&& apk add --update -t deps curl \  
&& curl -L https://storage.googleapis.com/kubernetes-
release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o
/usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl \  
&& apk del --purge deps \  
&& rm /var/cache/apk/*  
  
RUN mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez --force  
  
RUN mkdir /cloud_assistant \  
&& mkdir /root/.kube  
  
COPY . /cloud_assistant  
  
WORKDIR /cloud_assistant  
  
RUN mix local.hex --force \  
&& mix local.rebar --force \  
&& mix deps.get --only prod \  
&& mix compile \  
&& mix phoenix.digest  
  
CMD mix phoenix.server  


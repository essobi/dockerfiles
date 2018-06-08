# Phoenix v1.2  
#  
# docker run --rm pottava/phoenix:1.2  
# docker run --rm -it pottava/phoenix:1.2 hex.info  
FROM pottava/elixir:1.4  
ENV PHENIX_VERSION=1.2.4  
RUN apk --no-cache add erlang-crypto==19.3.0-r3 \  
erlang-syntax-tools==19.3.0-r3 \  
erlang-parsetools==19.3.0-r3 \  
erlang-eunit==19.3.0-r3 \  
  
# Install dependencies  
&& apk --no-cache add nodejs nodejs-npm inotify-tools \  
  
# Install Hex  
&& mix local.hex --force \  
  
# Install Phoenix archive  
&& mix archive.install --force \  
https://github.com/phoenixframework/archives/raw/master/phoenix_new-${PHENIX_VERSION}.ez  
  
ENTRYPOINT ["mix"]  
CMD ["phoenix.server"]  


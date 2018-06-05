FROM baden/elixir  
MAINTAINER Denys Batrak baden.i.ua@gmail.com  
  
RUN mkdir /node && \  
cd /node && \  
curl -O https://nodejs.org/dist/v4.4.7/node-v4.4.7-linux-x64.tar.xz && \  
tar xf ./node-v4.4.7-linux-x64.tar.xz && \  
rm ./node-v4.4.7-linux-x64.tar.xz  
  
ENV PATH /node/node-v4.4.7-linux-x64/bin/:${PATH}  
  
ENV DEBIAN_FRONTEND="noninteractive"  
RUN apt-get update -qq && \  
apt-get install -y inotify-tools && \  
apt-get -qq clean  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN mix local.hex --force && \  
mix local.rebar --force && \  
mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez --force  
  
# Install some for user composer  
RUN USER_ID=1000 GROUP_ID=1000 /entrypoint.sh true && \  
runuser -u composer -- mix local.hex --force && \  
runuser -u composer -- mix local.rebar --force && \  
runuser -u composer -- mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez --force  
  
ARG PORT=4000  
ENV PORT=${PORT}  
  
EXPOSE ${PORT}  
  
CMD ["bash"]  


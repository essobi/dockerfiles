FROM debian:jessie  
  
RUN sed -i "s/httpredir.debian.org/ftp.cn.debian.org/" /etc/apt/sources.list  
RUN apt-get update && apt-get --yes install wget golang  
RUN wget -qO - https://dl.senorsen.com/pub/package/linux/senorsen.public.key |
apt-key add -  
RUN wget https://dl.senorsen.com/pub/package/linux/senorsen.list -O
/etc/apt/sources.list.d/senorsen.list  
RUN apt-get update && apt-get --yes install git-auto-pull  
  
ENV GOPATH /srv/go  
RUN go get -v github.com/urfave/cli  
  
COPY src /srv/git-auto-pull-entry  
WORKDIR /srv/git-auto-pull-entry  
RUN go build -o entry  
  
COPY .ssh /root/.ssh  
  
ENTRYPOINT ["/srv/git-auto-pull-entry/entry"]  


FROM phusion/baseimage:latest  
  
ARG proxy  
  
# Install useful packages  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends ca-certificates wget software-
properties-common  
RUN add-apt-repository ppa:gophers/archive  
RUN apt-get update  
RUN wget -qO- https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get -y --no-install-recommends install build-essential libfontconfig
curl ca-certificates git nodejs  
  
# Install golang 1.9  
RUN apt-get install -y golang-1.9-go  
  
# Build & install grafana  
RUN git clone https://github.com/DanCech/grafana.git -b
graphiteDynamicFunctions /src/github.com/grafana/grafana  
WORKDIR /src/github.com/grafana/grafana  
RUN export PATH=$PATH:/usr/lib/go-1.9/bin && \  
go run build.go setup  
RUN npm install -g yarn  
RUN if [ "x$proxy" != "x" ] ; then yarn config set proxy $proxy ; fi  
RUN if [ "x$proxy" != "x" ] ; then yarn config set https-proxy $proxy ; fi  
RUN yarn install --pure-lockfile  
RUN npm run build  
  
# Add gosu and remove useless files  
RUN curl -L https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 >
/usr/sbin/gosu  
RUN chmod +x /usr/sbin/gosu  
RUN dpkg -P --force-all golang-1.9-go  
RUN apt-get autoremove -y  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
  
VOLUME ["/var/lib/grafana", "/var/log/grafana", "/etc/grafana"]  
  
EXPOSE 3000  
ADD ./run.sh /run.sh  
RUN chmod +x /run.sh  
ENTRYPOINT ["/run.sh"]


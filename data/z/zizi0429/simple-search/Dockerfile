FROM alpine  
  
USER root  
RUN apk update \  
&& apk --no-cache add \  
bash \  
ca-certificates \  
ruby \  
ruby-dev \  
gcc \  
g++ \  
make \  
ruby-rdoc \  
ruby-irb \  
python \  
py-pip \  
gettext \  
&& update-ca-certificates \  
&& gem install fluentd \  
&& fluent-gem install fluent-plugin-elasticsearch \  
&& pip install requests \  
&& apk del \  
ruby-dev \  
gcc \  
g++ \  
make \  
py-pip  
  
RUN mkdir /home/fluent  
WORKDIR /home/fluent  
COPY fluent fluent  
COPY plugins plugins  
COPY bin bin  
  
RUN adduser -D -g '' -u 1000 -h /home/fluent fluent  
RUN chown -R fluent:fluent /home/fluent  
USER fluent  
  
EXPOSE 24224  
CMD ["/bin/bash", "./bin/run.sh"]  


FROM nginx:stable-alpine  
MAINTAINER Ivan Bojko <ivan.bojko@heptaedre.com>  
  
# Timezone  
ENV TIMEZONE Europe/Paris  
  
# Install the NGINX Amplify Agent  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache \  
openrc \  
tzdata ca-certificates wget python python-dev py-configobj git util-linux
procps gcc musl-dev linux-headers && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py --ignore-installed --user && \  
~/.local/bin/pip install setuptools --upgrade --user && \  
rm -rf nginx-amplify-agent && \  
git clone "https://github.com/nginxinc/nginx-amplify-agent" && \  
cd nginx-amplify-agent && \  
~/.local/bin/pip install --upgrade \  
\--target=amplify --no-compile \  
-r packages/requirements && \  
python setup.py install && \  
cp nginx-amplify-agent.py /usr/bin && \  
mkdir -p /var/log/amplify-agent && \  
chmod 755 /var/log/amplify-agent && \  
mkdir -p /var/run/amplify-agent && \  
chmod 755 /var/run/amplify-agent && \  
rm -rf ~/.local && \  
apk del ca-certificates wget python-dev py-configobj git gcc musl-dev linux-
headers tzdata &&\  
rm -rf /var/cache/apk/* &&\  
mkdir -p /etc/amplify-agent  
  
COPY ./conf.d/agent.conf /etc/amplify-agent/agent.conf  
COPY ./log-rotation.sh /log-rotation.sh  
COPY ./entrypoint.sh /entrypoint.sh  
  
EXPOSE 80  
EXPOSE 443  
RUN chmod +x /log-rotation.sh; \  
chmod +x /entrypoint.sh; \  
chmod +r /proc;  
  
# TO set/override API_KEY and AMPLIFY_IMAGENAME when starting an instance:  
# docker run --name my-nginx1 -e API_KEY='..effc' -e
AMPLIFY_IMAGENAME="service-name" -d nmhung1210/nginx-alpine-amplify  
ENTRYPOINT ["/entrypoint.sh"]  


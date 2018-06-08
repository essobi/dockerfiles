# basti1253/meteor-docker-dev  
FROM node:4.6  
MAINTAINER Sebastian Sauer <info@dynpages.de>  
  
ENV REFRESHED_AT="2016-02-25" \  
METEOR_VERSION=1.4.3.1 \  
USER=node \  
USERID=1000 \  
PORT=3000 \  
TERM=xterm-256color  
  
RUN ([ $USERID -ne 1000 ] \  
&& groupadd --gid $USERID $USER \  
&& useradd --uid $USERID \--gid $USERID \--shell /bin/bash --create-home) \  
|| true;  
  
USER $USER  
RUN mkdir -p /home/$USER/app \  
&& cd /home/$USER \  
&& curl -SL https://install.meteor.com/ | \  
sed -e "s/^RELEASE=.*/RELEASE=\"\$METEOR_VERSION\"/" | \  
sh  
  
USER root  
  
ADD meteor-run /usr/local/bin/  
  
RUN chmod a+x /usr/local/bin/meteor-run \  
&& cp "/home/$USER/.meteor/packages/meteor-tool/1.4.3_1/mt-
os.linux.x86_64/scripts/admin/launch-meteor" /usr/local/bin/meteor \  
&& chmod a+x /usr/local/bin/meteor;  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends locales \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen && /usr/sbin/locale-gen;  
  
USER $USER  
VOLUME [ /home/$USER/app ]  
  
WORKDIR /home/$USER/app  
  
EXPOSE 3000  
CMD [ "/usr/local/bin/meteor-run" ]  


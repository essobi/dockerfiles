# GAZE  
# Turnkey Open Media Center  
# __ .-.  
# .-"` .`'. /\\\|  
# _(\\-/)_" , . ,\ /\\\\\/ =o O=  
# {(=o^O=)} . ./, |/\\\\\/  
# `-.(Y).-` , | , |\\.-`  
# /~/,_/~~~\,__.-` =O o=  
# ////~ // ~\\\  
# ==`==` ==` ==`  
# gaze.monokal.io  
FROM python:3.6.1-alpine  
  
# Alpine packages to install.  
ENV APK_PACKAGES \  
alpine-sdk \  
libffi-dev \  
openssl-dev \  
tzdata  
  
# PyPI packages to install.  
ENV PIP_PACKAGES \  
docker \  
docker-compose \  
termcolor \  
jinja2 \  
tabulate  
  
# Install the Alpine packages.  
RUN apk --no-cache add $APK_PACKAGES  
  
# Configure the system time.  
RUN apk add tzdata && \  
cp /usr/share/zoneinfo/Europe/London /etc/localtime && \  
echo "Europe/London" > /etc/timezone && \  
apk del tzdata  
  
# Install the PyPI packages.  
RUN pip install $PIP_PACKAGES  
  
# Drop gazectl in place.  
RUN mkdir -p /opt/gazectl  
  
WORKDIR /opt/gazectl  
  
COPY gazectl .  
  
ENTRYPOINT ["python", "gazectl.py"]  


# Flindt Build Stage  
# Build the frontend code and get only the built artifacts  
  
# Inherit the smallest Node LTS image possible  
##############################################  
FROM node:8-alpine AS flindt-fe-build  
  
# Set a known working directory  
###############################  
WORKDIR /app  
  
# Install missing dependencies  
##############################  
  
RUN apk --update add --no-cache \  
git  
  
# Clone the Frontend repository and build it  
############################################  
RUN git clone https://github.com/wearespindle/flindt-front-end.git . \  
&& npm i \  
&& npm run build  
  
# ---- Artifacts can be found now in /app/build ---- #  
  
# Flindt Run Stage  
# Use supervisord to keep the backend up and running, coupled with the
Frontend code served via nginx  
  
# Inherit the smallest Nginx image possible  
###########################################  
  
FROM nginx:alpine  
  
# Environment variables  
#######################  
  
# Flindt Database connection  
ENV FLINDT_DB_HOST localhost  
ENV FLINDT_DB_NAME flindt  
ENV FLINDT_DB_USER flindt  
ENV FLINDT_DB_PASS flindt  
  
# Flindt OAuth with Google Plus  
ENV FLINDT_SOCIAL_AUTH_GOOGLE_PLUS_KEY
SomeSecretKey.apps.googleusercontent.com  
  
# Flindt CORS Whitelist  
ENV FLINDT_CORS_ORIGIN_WHITELIST localhost:8000  
  
# Flindt Frontend Hostname  
ENV FLINDT_FRONTEND_HOSTNAME localhost  
  
# Flindt Debug log ( 0 = disabled, 1 = enabled )  
ENV FLINDT_DEBUG 0  
  
# Copy required files and fix permissions  
#########################################  
  
COPY src/ /root/  
  
# Install runtime dependencies  
##############################  
  
RUN apk --update add --no-cache \  
python3 \  
mariadb-client-libs \  
# Supervisor Daemon  
supervisor  
  
# Install build dependencies  
############################  
  
RUN apk add --no-cache --virtual .build-deps \  
python3-dev \  
mariadb-dev \  
build-base \  
jpeg-dev \  
zlib-dev \  
linux-headers \  
git  
  
# Fetch the backend code and install dependencies  
#################################################  
  
RUN git clone https://github.com/wearespindle/flindt.git /app \  
&& cd /app/backend \  
&& pip3 install --upgrade pip \  
&& pip3 install -r requirements.txt  
  
# Copy the Frontend to the expected Nginx folder  
################################################  
  
COPY --from=flindt-fe-build /app/build /var/www  
  
# Cleanup  
#########  
  
RUN apk del .build-deps \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& rm -rf /var/cache/apk/*  
  
# Replace default configurations  
################################  
  
RUN rm /etc/supervisord.conf \  
&& mv /root/supervisord.conf /etc \  
&& cp -Rf /root/nginx/* /etc/nginx \  
&& rm -Rf /root/nginx  
  
# Allow redirection of stdout to docker logs  
############################################  
  
RUN ln -sf /proc/1/fd/1 /var/log/docker.log  
  
# Expose required ports  
#######################  
  
EXPOSE 80  
  
# Change Shell  
##############  
  
SHELL ["/bin/bash", "-c"]  
  
# Set the entry point to init.sh  
###########################################  
  
ENTRYPOINT /root/init.sh  


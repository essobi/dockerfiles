FROM alpine:latest  
  
# Define build time arguments  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
# Use UID 1000 if not passed as a build argument  
ARG UID=1000  
  
RUN set -ex \  
\  
# Install dependencies  
&& apk add \--no-cache \  
python \  
groff \  
less \  
py-pip \  
\  
# Install AWS CLI  
&& pip --no-cache-dir install awscli==$VERSION \  
\  
# Clean up  
&& apk del py-pip \  
\  
# Add aws user  
&& adduser -D -u $UID aws  
  
WORKDIR /home/aws  
  
USER aws  
  
CMD ["help"]  
ENTRYPOINT ["aws"]  
  
# Define image metadata (https://microbadger.com/labels)  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license=MIT \  
org.label-schema.name="aws-cli" \  
org.label-schema.version=$VERSION \  
org.label-schema.url=https://github.com/aws/aws-cli \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/nbrownuk/docker-aws-cli.git" \  
org.label-schema.vcs-type=Git  


FROM alpine:latest  
  
# no ARGs for now  
# For example could add support for 32bit  
#LETS copy your exisitng site into the container when its ran  
#ENV www=site  
#OK nevermind nice try..  
# Create the user/group to run hugo  
ENV HUGO_USER=hugo \  
HUGO_UID=1000 \  
HUGO_GID=1000 \  
HUGO_HOME=/hugo  
  
RUN addgroup -S $HUGO_USER -g ${HUGO_GID} \  
&& adduser -S \  
-g $HUGO_USER \  
-h $HUGO_HOME \  
-u ${HUGO_UID} \  
$HUGO_USER  
  
# Package upgrades at start, get necessary programs  
RUN apk update && apk upgrade \  
&& apk add --no-cache wget bash git curl tar  
  
WORKDIR /  
  
# AWESOME, we can pull the latest 64bit linux release without defining a
version  
RUN wget $(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest
| grep '\http.*Linux-64bit.tar.gz' | cut -d\" -f4)  
  
# Setup Hugo envrionment  
RUN mkdir -p /app/site && tar xzf *.tar.gz -C /usr/local/bin \  
&& rm -fr *tar.gz \  
&& chmod +x /usr/local/bin/hugo \  
#Guess we don't need this line, maybe in the future if example site doesn't
exist && /app/site/hugo new site /app/site \  
&& git clone https://github.com/gcushen/hugo-academic.git /app/themes/academic
\  
&& cp -av /app/themes/academic/exampleSite/* /app/site \  
&& chown -R hugo:hugo /app  
  
#Copy your site files into container.. ok lets not do this  
#COPY ${www} /app/site  
# CLEAN UP, makes the image nice and small again  
RUN apk del wget git curl tar \  
&& rm /var/cache/apk/*  
  
USER $HUGO_USER  
  
EXPOSE 1313  
WORKDIR /app/site  
  
#VOLUME ["/app/site"]  
ENTRYPOINT ["hugo"]  
  
# We can ignore this line, cos testing CMD ["/app/site/hugo server --watch"]  


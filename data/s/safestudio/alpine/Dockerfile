FROM alpine:3.7  
RUN apk update --no-cache && apk upgrade --update --no-cache  
  
# Install language pack  
RUN apk add --update --no-cache ca-certificates wget  
  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub  
RUN wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.27-r0/glibc-2.27-r0.apk  
RUN wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.27-r0/glibc-bin-2.27-r0.apk  
RUN wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.27-r0/glibc-i18n-2.27-r0.apk  
  
RUN apk add glibc-2.27-r0.apk glibc-bin-2.27-r0.apk glibc-i18n-2.27-r0.apk  
RUN apk add --update --no-cache glibc-bin-2.27-r0.apk glibc-i18n-2.27-r0.apk
tzdata tar curl bash  
  
# Iterate through all locale and install it  
# Note that locale -a is not available in alpine linux, use `/usr/glibc-
compat/bin/locale -a` instead  
RUN /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN ln -fs /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime  
  
RUN addgroup -g 1000 safestudio && adduser -D -u 1000 -G safestudio safestudio  
  
RUN rm -rf /var/cache/apk/*  


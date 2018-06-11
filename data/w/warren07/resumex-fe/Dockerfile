FROM nginx  
  
COPY dist /usr/share/nginx/html  
  
# #FROM alpine:3.6  
# FROM gliderlabs/alpine  
# MAINTAINER Warren Veerasingam <umesh.veerasingam@pearson.com>  
  
# #install bash and add certs  
# RUN apk update && apk --no-cache add ca-certificates wget bash  
  
# #install node  
# RUN apk add --update nodejs nodejs-npm  
  
# #install nginx  
# RUN apk --no-cache add nginx  
  
#RUN apk add openrc --no-cache  
  
# # Tell openrc its running inside a container, till now that has meant LXC  
# RUN sed -i 's/#rc_sys=""/rc_sys="lxc"/g' /etc/rc.conf  
# # # Tell openrc loopback and net are already there, since docker handles the
networking  
# RUN echo 'rc_provide="loopback net"' >> /etc/rc.conf  
# # # no need for loggers  
# RUN sed -i 's/^#\\(rc_logger="YES"\\)$/\1/' /etc/rc.conf  
# # # can't get ttys unless you run the container in privileged mode  
# RUN sed -i '/tty/d' /etc/inittab  
# # # can't set hostname since docker sets it  
# RUN sed -i 's/hostname $opts/# hostname $opts/g' /etc/init.d/hostname  
# # # can't mount tmpfs since not privileged  
# RUN sed -i 's/mount -t tmpfs/# mount -t tmpfs/g' /lib/rc/sh/init.sh  
# # # can't do cgroups  
# RUN sed -i 's/cgroup_add_service /# cgroup_add_service /g'
/lib/rc/sh/openrc-run.sh  
# # clean apk cache  
# RUN rm -rf /var/cache/apk/*  
  
# CMD ["/sbin/init"]  
# Create env for files  
ENV APP=/app  
  
# # Create a directory where our app will be placed  
# RUN mkdir -p $APP  
  
# # Change directory so that our commands run inside this new directory  
# WORKDIR $APP  
  
# # Copy dependency definitions  
# #COPY package.json $WORKDIR  
# COPY . $WORKDIR  
  
# # Install dependecies  
# RUN npm install  
  
# # try building prod  
# RUN npm build  
  
# # try building prod  
# RUN chmod +x run_application.sh  
# CMD ["./run_application.sh"]  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  
  
  
  
  
  
  


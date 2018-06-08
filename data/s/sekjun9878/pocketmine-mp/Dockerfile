# Dockerfile  
# For PocketMine/PocketMine-MP  
#  
# Please make sure you set up port forwarding with these options:  
# -p <HOST_IP>:19132:19132 -p 1270.0.1:19132:19132/udp  
FROM ubuntu:14.04  
MAINTAINER Michael Yoo <michael@yoo.id.au>  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y wget curl  
  
# Use dedicated server user  
# Use /bin/false to disable login  
# /bin/false is used over /sbin/nologin to also reject SSH connections
(/sbin/nologin allows SSH)  
# Permissions need to be set separately because this is a system account (they
are not automatically set)  
RUN mkdir /home/pocketmine-mp  
RUN useradd --comment PocketMine-MP --system --shell /bin/false \--create-home
--home /home/pocketmine-mp pocketmine-mp  
RUN chown -R pocketmine-mp:pocketmine-mp /home/pocketmine-mp  
RUN chmod -R 750 /home/pocketmine-mp  
  
USER pocketmine-mp  
  
WORKDIR /home/pocketmine-mp  
  
RUN wget -q -O - http://get.pocketmine.net/ | bash  
  
EXPOSE 19132  
EXPOSE 19132/udp  
  
# (Note that the server will run as the service user, NOT root!)  
ENTRYPOINT ["/home/pocketmine-mp/bin/php5/bin/php", "/home/pocketmine-
mp/PocketMine-MP.phar"]  
CMD ["--no-wizard"]


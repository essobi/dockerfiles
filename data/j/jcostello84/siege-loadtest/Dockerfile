FROM debian:wheezy  
MAINTAINER Jonathan Costello<jcostello84@gmail.com>  
  
#Install dependencies.  
RUN apt-get -y update && apt-get install -y vim curl siege && apt-get clean &&
rm -rf /var/lib/apt/lists/*  
RUN ulimit -c -m -s -t unlimited  
  
#Uncomment the lines below, if you would like to set them once, instead of
setting them each time.  
ENV DOMAIN https://www.<example>.com  
ENV URL_LIST /  
ENV ETC_HOSTS 192.168.1.1 local.dev.example.com admin-local.dev.example.com
admin.local.dev.example.com assets-local.dev.example.com  
#ENV LOGIN_URL <https://www.SET_BASE_URL.com/login_end_point>  
#ENV USERNAME <username>  
#ENV PASSWORD <password>  
#Add directory where the docker containers  
ADD opt /opt  
ADD entry.sh /entry.sh  
  
ENTRYPOINT ["/entry.sh"]  
CMD ["-v", "-l", "-c10", "-r10"]  


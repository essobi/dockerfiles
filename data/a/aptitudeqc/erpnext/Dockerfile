FROM ubuntu:14.04  
MAINTAINER Aptitude Technologies <support@aptitudetech.net>  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV MSQ_PASS demopass  
ENV HOSTNAME erpnext.aptitudetech.net  
ENV FRAPPE_USER frappe  
ENV FRAPPE_BRANCH master  
ENV BENCH_BRANCH master  
ENV ADMIN_PASS admin  
ENV SITE_NAME site1.local  
  
ENV ERPNEXT_APPS_JSON
https://raw.githubusercontent.com/frappe/bench/master/install_scripts/erpnext-
apps-master.json  
RUN useradd $FRAPPE_USER && mkdir /home/$FRAPPE_USER && chown -R
$FRAPPE_USER.$FRAPPE_USER /home/$FRAPPE_USER  
  
WORKDIR /home/$FRAPPE_USER  
COPY setup.sh /  
RUN bash /setup.sh  
EXPOSE 80  


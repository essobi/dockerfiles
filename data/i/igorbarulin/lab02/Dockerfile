FROM centos:6  
MAINTAINER "Igor Barulin" <igorbarulin@gmail.com>  
ENV container docker  
RUN yum -y install rsyslog; \  
echo Отчет Барулин Игорь z2442k > report; \  
echo --- >> report; \  
echo Определить список установленных сервисов >> report; \  
echo >> report; \  
chkconfig --list >> report; \  
echo --- >> report; \  
echo Определить список сервисов, запускаемых в 3-ем режиме работы >> report; \  
echo >> report; \  
/sbin/chkconfig --level 3 --list >> report; \  
echo --- >> report; \  
echo Определить параметры сетевых интерфейсов >> report; \  
echo >> report; \  
ifconfig >> report; \  
echo --- >> report; \  
echo Определить статические маршруты сети >> report; \  
echo >> report; \  
route >> report; \  
echo --- >> report; \  
echo Удалить статический маршрут по-умолчанию >> report; \  
echo >> report; \  
route del default; \  
route >> report; \  
echo --- >> report; \  
echo Определить состояние сетевого сервиса >> report; \  
echo >> report; \  
service network status >> report; \  
echo --- >> report; \  
echo Остановить сетевой сервис >> report; \  
echo >> report; \  
/etc/init.d/network stop; \  
service network status >> report; \  
echo --- >> report; \  
echo Определить статические маршруты сети с отключенным сервисом >> report; \  
route >> report; \  
echo --- >> report; \  
echo Вновь активировать сетевой интерфейс >> report; \  
echo >> report; \  
service network start; \  
route >> report; \  
echo --- >> report; \  
echo Отключить сетевой интерфейс командой ifconfig >> report; \  
echo >> report; \  
ifconfig eth0 down; \  
ifconfig >> report; \  
echo --- >> report; \  
echo Получить состояние сетевого сервиса во всех режимах работы >> report; \  
echo >> report; \  
chkconfig --list network >> report;  
CMD cat report  


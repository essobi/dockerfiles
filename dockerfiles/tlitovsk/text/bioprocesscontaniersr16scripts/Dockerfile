FROM tlitovsk/bioprocesscontaniersr16:latest
MAINTAINER Anatoly Litovsky <anatolylit@gmail.com>
MAINTAINER Anna Litovsky <anna.makhlina@mail.huji.ac.il>
ENV container docker 

RUN apt-get install -y gawk mawk
RUN pip install pip --upgrade
RUN pip install flask-WTF

COPY run.sh /root/run.sh
RUN chmod +x /root/run.sh

COPY mothur-run.sh /root/mothur-run.sh
RUN chmod +x /root/mothur-run.sh

COPY qiime-run.sh /root/qiime-run.sh
RUN chmod +x /root/qiime-run.sh

COPY default.sh /root/default.sh
RUN chmod +x /root/default.sh

ADD webinterface /root/webinterface

EXPOSE 5000
CMD "/root/default.sh"

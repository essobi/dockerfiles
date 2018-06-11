FROM fedora:latest  
MAINTAINER James H Nguyen <james.nguyen@gmail.com>  
  
RUN dnf -y update && dnf clean all  
RUN dnf -y install git \  
ansible \  
sudo \  
&& dnf clean all  
  
# environment  
ENV WORKSPACE_USER ${WORKSPACE_USER:-gcloud}  
  
# add an gcloud user and allow it to sudo  
RUN useradd -m luser && echo 'luser ALL=NOPASSWD: ALL' > /etc/sudoers.d/luser  
  
# switch to user  
USER luser  
ENV HOME /home/luser  
ENV PATH /home/luser/google-cloud-sdk/bin:${PATH}  
ENV CLOUDSDK_PYTHON /usr/bin/python  
  
# install gcloud  
RUN curl -o /tmp/google-cloud-sdk.tar.gz \  
https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz \  
&& tar -C /home/luser -zxf /tmp/google-cloud-sdk.tar.gz \  
&& /home/luser/google-cloud-sdk/install.sh \  
\--usage-reporting false \  
\--bash-completion true \  
\--rc-path /home/luser/.bashrc \  
\--path-update true \  
&& rm -rf /tmp/google-cloud-sdk.tar.gz  
  
VOLUME /data /home/luser/.config/gcloud /home/luser/.ssh  
  
CMD /bin/bash  
  
#build image:  
# $ docker build -t fedora-workspace .  
  
#data volume usage:  
# $ docker create -d convoy --opt o=size5GB --name mydatavol  
# $ docker create -d convoy --opt o=size100MB --name mygcloudconfigvol  
# $ docker run -v mydatavol:/data -v
mygcloudconfigvol:/home/luser/.config/gcloud [-v
c:/Users/James/Docker/data/Gitlab/home/.ssh:/home/luser/.ssh] --name
myworkspace -it ipv1337/fedora-workspace  
#data volume container usage:  
# $ docker create -v /data --name data-volume fedora /bin/true  
# $ docker create -v /home/luser/.config/gcloud --name gcloud-config-volume
fedora /bin/true  
# $ docker run --volumes-from data-volume --volumes-from gcloud-config-volume
[-v c:/Users/<username>/Docker/data/Gitlab/home/.ssh:/home/luser/.ssh] --name
workspace -it ipv1337/fedora-workspace  
#backup volume:  
# $ docker run --rm --volumes-from data-volume -v
c:/Users/James/Downloads:/backup fedora tar cvf /backup/data-volume.tar /data  
# $ docker run --rm --volumes-from gcloud-config-volume -v
c:/Users/James/Downloads:/backup fedora tar cvf /backup/gcloud-config-
volume.tar /home/luser/.config/gcloud  
#restore volume:  
# $ docker run --rm --volumes-from myworkspace -v $(pwd):/backup fedora bash
-c "cd /data && tar xvf /backup/data-volume.tar --strip 1"  
# $ docker run --rm --volumes-from myworkspace -v $(pwd):/backup fedora bash
-c "cd /home && tar xvf /backup/gcloud-config-volume.tar --strip 1"  
#find unused volumes:  
# $ docker volume ls -f dangling=true  
#using workspace:  
# $ docker-compose run workspace /bin/bash (creates new container)  
# or  
# $ docker start workspace  
# $ docker attach workspace  


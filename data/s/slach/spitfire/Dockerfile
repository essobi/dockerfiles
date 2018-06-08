#  
# Dockerfile  
#  
FROM base/archlinux  
MAINTAINER Sebastian Lach <root@slach.eu>  
  
# upgrade os  
RUN pacman -Syy --noconfirm archlinux-keyring  
RUN pacman -Sqyyu --noconfirm --noprogressbar && pacman-db-upgrade  
RUN pacman -U --noconfirm /var/cache/pacman/pkg/ca-certificates-
utils-*.pkg.tar.xz  
  
# environment  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
ENV ANSIBLE_FORCE_COLOR=true  
  
RUN pacman -Sq --noconfirm --noprogressbar python2 ansible git  
RUN echo -e "localhost\tansible_connection=local
ansible_python_interpreter=/usr/bin/python2" > /etc/ansible/hosts  
  
# ansible on build  
ONBUILD ADD . /etc/ansible  
ONBUILD RUN /usr/bin/ansible-galaxy install -r /etc/ansible/requirements/*.yml  
ONBUILD RUN /usr/bin/ansible-playbook /etc/ansible/*.yml  


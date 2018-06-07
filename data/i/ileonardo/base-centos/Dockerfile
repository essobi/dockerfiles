# x) - docker build -t ileonardo/base-centos .  
# y) - Às Instruções fica nas Dependências e no final do arquivo: [REGRA] # z)  
### Base da Imagem  
FROM centos:7  
### Autor  
MAINTAINER iLeonardo Carvalho <i.leonardo.c.c@outlook.com>  
  
### Dependências  
ENV container docker  
  
# Diretório definido para executar os comandos  
WORKDIR ~/  
  
# Pacotes Essenciais  
RUN yum -y update; yum clean all  
  
# Configuração  
RUN yum -y install systemd epel-release net-tools iputils vim curl; yum clean
all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
### Start  
VOLUME ["/sys/fs/cgroup"]  
CMD ["/usr/sbin/init"]  
  
# z) docker run -it -e "container=docker" --privileged=true -d --security-opt
seccomp:unconfined --cap-add=SYS_ADMIN -v /sys/fs/cgroup:/sys/fs/cgroup:ro
ileonardo/base-centos bash -c "/usr/sbin/init"  


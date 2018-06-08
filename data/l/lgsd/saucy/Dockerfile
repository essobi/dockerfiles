Base Image Creation:  
  
$ sudo debootstrap saucy saucy > /dev/null  
  
$ sudo tar -C saucy -c . | docker import - lgsd/saucy  
  
$ sudo docker run lgsd/saucy cat /etc/lsb-release  
  
DISTRIB_ID=Ubuntu  
  
DISTRIB_RELEASE=13.10  
  
DISTRIB_CODENAME=saucy  
  
DISTRIB_DESCRIPTION="Ubuntu 13.10"  
  
$ docker push lgsd/saucy


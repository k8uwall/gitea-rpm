docker stop centos7
docker rm centos7
docker run --privileged -d -v `pwd`/build:/build -p 3000:3000 -p 3022:3022 --name centos7 centos:centos7 /sbin/init
docker exec -it centos7 /bin/bash

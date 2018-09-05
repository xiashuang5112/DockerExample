#FROM python:3.6
FROM centos:latest

ENV CMDBSERVERPATH="/data/server"

#ENV PYTHONIOENCODING="UTF-8" \
#    CMDBSERVERPATH="/apps/server" \
#    DATABASE_NAME="dbname" \
#    DATABASE_USER="user" \
#    DATABASE_PASSWORD="********" \
#    DATABASE_SERVICE_HOST="cmdb_mysql" \
#    DATABASE_SERVICE_PORT=3306

MAINTAINER Shaungxi Xia "email@example.com"

# ARG CMDB_USER=cmdb

# ENV HOME /home/$CMDB_USER
# ENV PATH="$HOME/.pyenv/bin:$PATH"

# centos:7.0.1406
# rabbitmq:3.6.16
# python:3.7.0-stretch
# redis:4.0.11

# 暴露端口
EXPOSE 80

WORKDIR $CMDBSERVERPATH
## 复制requirements.txt文件
#COPY $PWD/conf_stag/requirements.txt .
#
#RUN yum -y update && \
#    yum install -y mysql mysql-devel && \
#    yum install https://centos7.iuscommunity.org/ius-release.rpm && \
#    yum -y install python36u python36u-devel python36u-pip && \
#    pip3 install -r requirements.txt
#
## 拷贝源码到指定目录
#COPY ./cmdb $CMDBSERVERPATH
#
#
COPY $PWD/build/entrypoint.sh /
#
## 启动脚本
#WORKDIR /
#RUN sh /data/server/entrypoint.sh
#
#WORKDIR $CMDBSERVERPATH
# 启动服务
#RUN python manage.py runserver 0.0.0.0:80


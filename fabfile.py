from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = "git上的项目地址"

env.user = 'host name'
env.password = 'host password'

env.hosts = ['主机对应的域名']

#一般情况下对应的端口为22
env.port = '22'

def deploy():
    source_folder = '/home/yangxg/sites/zmrenwu.com/django-blog-tutorial' \
                    '部署的项目根目录在服务器上的位置'
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-demo.zmrenwu.com')
    sudo('service nginx reload')